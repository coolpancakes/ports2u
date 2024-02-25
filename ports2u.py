#  Port scanner I built in python, Version 1.0.0

import argparse
import socket
import sys


def port_scan(ip_address: str, ports: str):
    try:
        port_list = [int(elem) for elem in ports.split(",")]
    except ValueError as e:
        print(f"'{ports}' is not a valid value for a port or range of ports.")
        return
    print('scanning...')
    print('')
    scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scan.settimeout(4)

    for port in port_list:
        data = scan.connect_ex(
            (ip_address, port)
        )
        if data == 0:
            print(f"Port {port} is open.")
        else:
            print(f"Port {port} is closed.")
    print('')
    print('Scan finished! ')


def main_menu():
    parser = argparse.ArgumentParser(prog='ports2u',
                                     description='Scans IP for open ports based on the users input',
                                     usage='ports2u.py -ip IP_HERE -p PORT_HERE or ports2u.py -h for help')
    ip = parser.add_argument('-ip', metavar='--IP',
                             help='Add your IP address here as follows: -ip 192.168.1.0',
                             required=True)

    port = parser.add_argument('-p', metavar='--P',
                               help='Add your ports or port as follows: -p 80,43,53,21'
                               '-p 80', required=True)

    version = parser.add_argument('--version', help='Check the ports2u version',
                                  action='version', version='1.0.0')

    args = parser.parse_args()

    port_scan(args.ip, args.p)


main_menu()
