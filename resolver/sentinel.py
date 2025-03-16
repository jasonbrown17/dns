'''
Sentinel is used to query a singular record across 
several public DNS servers
'''

import csv
import dns.resolver

def get_a_addresses(url_addy):

    '''
    Get a list of A records and display them in SDOUT
    '''

    unique_addresses = []
    nserver = {}
    with open('resolver/dns_servers.csv', 'r', encoding='utf-8') as fqdn:
        for dns_resolver, ip_address in csv.reader(fqdn):
            nserver[dns_resolver] = ip_address

    try:
        print('##################')
        print('# IPv4 Addresses #')
        print('##################\n')
        for x, y in nserver.items():
            resolver = dns.resolver.Resolver(configure=False)
            resolver.nameservers = [y]
            print('#-', x, y, '-#')
            query_result = dns.resolver.resolve(url_addy, 'A')
            print('---------------')
            for fqdn in query_result:
                print(fqdn.to_text())
                unique_addresses.append(fqdn.to_text())
            print('---------------')
        cnt = len(set(unique_addresses))
        print('Total number of unique addresses: ',cnt, '\n')
    except dns.resolver.NoAnswer:
        print('***ERROR*** No A records exist for ', url_addy)

def get_aaaa_addresses(url_addy):

    '''
    Get a list of AAAA records and display them in SDOUT
    '''

    nserver = {}
    unique_addresses = []
    with open('resolver/dns_servers.csv', 'r', encoding='utf-8') as fqdn:
        for dns_resolver, ip_address in csv.reader(fqdn):
            nserver[dns_resolver] = ip_address

    try:
        print('##################')
        print('# IPv6 Addresses #')
        print('##################\n')
        for x, y in nserver.items():
            resolver = dns.resolver.Resolver(configure=False)
            resolver.nameservers = [y]
            print('#-', x, y, '-#')
            query_result = dns.resolver.resolve(url_addy, 'AAAA')
            print('---------------')
            for fqdn in query_result:
                print(fqdn.to_text())
                unique_addresses.append(fqdn.to_text())
            print('---------------')
        cnt = len(set(unique_addresses))
        print('Total number of unique addresses: ',cnt, '\n')
    except dns.resolver.NoAnswer:
        print('\n')
        print('***ERROR*** No AAAA records exist for', url_addy)

def get_ns_server(url_addy):

    '''
    Return the name server records for the URL
    '''

    query_result = dns.resolver.resolve(url_addy, 'NS')
    print('################')
    print('# Name Servers #')
    print('################')
    for fqdn in query_result:
        print(fqdn.to_text())
    print('\n')

def get_soa_server(url_addy):

    '''
    Return Start of Authority for the URL
    '''

    query_result = dns.resolver.resolve(url_addy, 'soa')
    print('######################')
    print('# Start of Authority #')
    print('######################')
    for fqdn in query_result:
        print(fqdn.to_text())
    print('\n')

def get_txt_records(url_addy):

    '''
    Return the TXT records
    '''

    query_result = dns.resolver.resolve(url_addy, 'txt')
    print('###############')
    print('# TXT Records #')
    print('###############')
    for fqdn in query_result:
        print(fqdn.to_text())
    print('\n')

def main():

    '''
    Main function call
    '''

    get_url = input('Enter URL: ')
    get_soa_server(get_url)
    get_ns_server(get_url)
    get_txt_records(get_url)
    get_a_addresses(get_url)
    get_aaaa_addresses(get_url)


if __name__ == '__main__':
    main()
