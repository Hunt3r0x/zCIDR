#!/usr/bin/env python

import ipaddress
import argparse

def get_ips_from_cidr(cidr):
    ip_list = []
    try:
        network = ipaddress.ip_network(cidr)
        for ip in network.hosts():
            ip_list.append(str(ip))
    except ValueError as e:
        print(f"Error: {e}")
    return ip_list

def main():
    parser = argparse.ArgumentParser(description="Get all IPs from a CIDR range")
    parser.add_argument("-cidr", help="CIDR notation range (e.g., 192.168.1.0/24)", required=True)
    args = parser.parse_args()

    cidr_range = args.cidr

    ips_in_range = get_ips_from_cidr(cidr_range)

    for ip in ips_in_range:
        print(ip)

if __name__ == "__main__":
    main()
