import json
import random
import socket
import urllib.request
import nmap
from backend.utils.file_helper import create_or_get_dir_location
import csv

from backend.wifi_cracking.wifi_cracking_service import try_and_break


def generate_random_ip_list(ip):
    number = 18
    random_ips = []
    ip_prefix_list = ip.split('.')
    ip_prefix = ip_prefix_list[0]+'.'+ ip_prefix_list[1]+'.' + ip_prefix_list[2]
    while number != 0:
        random_suffix = str(random.randint(2, 254))
        while random_suffix == ip_prefix_list[3]:
            random_suffix = str(random.randint(2, 254))
        random_ips.append(ip_prefix+'.'+random_suffix)
        number -= 1
    random_ips.append(ip)
    random_ips_string = ','.join(str(item) for item in random_ips)
    return random_ips_string


def get_ip_for_domain(domain):
    return socket.gethostbyname(domain)


def get_current_host_ip():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return external_ip


def port_scanner(domain):
    private_host_ip = get_current_host_ip()
    target_ip = get_ip_for_domain(domain)
    radom_ips = generate_random_ip_list(private_host_ip)
    nm = nmap.PortScanner()
    nm.scan(target_ip, '1-400',"-sV -D "+radom_ips )
    return nm


def save_scan_csv(nmap_result, domain):
    csv_data = nmap_result.csv()
    path_to_file = create_or_get_dir_location(domain, 'port_scanner')
    with open(f"{path_to_file}/{domain}_scan_output.csv", "w") as external_file:
        external_file.write(csv_data)
        external_file.close()
    data = extract_data_from_csv(f"{path_to_file}/{domain}_scan_output.csv")
    return data

def port_scanner_service(domain):
    nm = port_scanner(domain)
    data = save_scan_csv(nm, domain)
    return data


def extract_data_from_csv(filename):
    data = {
        'port': [],
        'port_type': [],
        'status': [],
        'protocol': [],
        'product': [],
    }
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                data['port'].append(row[4])
                data['port_type'].append(row[5])
                data['status'].append(row[6])
                data['protocol'].append(row[3])
                data['product'].append(row[7])
                line_count += 1
    return data
