import os
import shlex
import subprocess
import urllib.parse

from backend.utils.file_helper import create_or_get_dir_location
import json

def move_file(source, dest):
    os.replace(source, dest)

def extract_data_from_json(filename):
    data = {
        'emails': [],
        'phone_numbers': []
    }
    f = open(filename)
    rawData = json.load(f)
    for i in rawData:
        data['emails'].extend(i['emails'])
        for numb in i['phones']:
            parsed_phone_number = urllib.parse.unquote(numb)
            data['phone_numbers'].append(parsed_phone_number.strip("\u202a").strip("\u202c"))
    f.close()
    data['emails'] = list(dict.fromkeys(data['emails']))
    data['phone_numbers'] = list(dict.fromkeys(data['phone_numbers']))
    return data


def execute_email_scrapper(domain):
    wd = os.getcwd()
    os.chdir("/home/stefanita/PycharmProjects/Licenta2/backend/email_scrapper/")

    path_to_file = create_or_get_dir_location(domain, 'email_scrapper')
    filename = "emails_and_phones.json"
    process = subprocess.Popen(shlex.split(f"scrapy crawl gather_details -a domain={domain} -o emails_and_phones.json"),
                               stdout=subprocess.PIPE,
                               universal_newlines=True)

    while True:
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output
            data = extract_data_from_json(filename)
            move_file(filename, path_to_file+"/"+filename)
            os.chdir(wd)
            return data