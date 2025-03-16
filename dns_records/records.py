'''
This module is called from dns_search to query records
'''

import dns.resolver

def get_a_record(url_addy):
    '''
    Get the IP address of the associated A record
    '''
    try:
        query_result = dns.resolver.resolve(url_addy, 'A')
        print('#############')
        print('# A Records #')
        print('#############\n')
        for fqdn in query_result:
            print(fqdn.to_text())
        print('\n')
    except dns.resolver.NoAnswer:
        print('\nNo A records exist for ', url_addy)
    except dns.resolver.NXDOMAIN:
        print('Domain:', url_addy, 'does not exist')

def get_aaaa_record(url_addy):
    '''
    Get the IP address of the associated A record
    '''
    try:
        query_result = dns.resolver.resolve(url_addy, 'AAAA')
        print('################')
        print('# AAAA Records #')
        print('################\n')
        for fqdn in query_result:
            print(fqdn.to_text())
        print('\n')
    except dns.resolver.NoAnswer:
        print('\nNo AAAA records exist for ', url_addy)
    except dns.resolver.NXDOMAIN:
        print('Domain:', url_addy, 'does not exist')

def get_ns_server(url_addy):
    '''
    Return the configured name servers for the domain
    '''
    try:
        query_result = dns.resolver.resolve(url_addy, 'NS')
        print('################')
        print('# Name Servers #')
        print('################\n')
        for fqdn in query_result:
            print(fqdn.to_text())
        print('\n')
    except dns.resolver.NXDOMAIN:
        print('\nDomain ', url_addy, 'does not exist')

def get_soa_server(url_addy):
    '''
    Return the SOA of the domain
    '''
    try:
        query_result = dns.resolver.resolve(url_addy, 'SOA')
        print('######################')
        print('# Start of Authority #')
        print('######################\n')
        for fqdn in query_result:
            print(fqdn.to_text())
        print('\n')
    except dns.resolver.NXDOMAIN:
        print('\nDomain ', url_addy, 'does not exist')

def get_txt_records(url_addy):
    '''
    Return the TXT records of the domain
    '''
    try:
        query_result = dns.resolver.resolve(url_addy, 'TXT')
        print('###############')
        print('# TXT Records #')
        print('###############\n')
        for fqdn in query_result:
            print(fqdn.to_text())
        print('\n')
    except dns.resolver.NXDOMAIN:
        print('\nDomain ', url_addy, 'does not exist')

def get_mx_records(url_addy):
    '''
    Return the MX records of the domain
    '''
    try:
        query_result = dns.resolver.resolve(url_addy, 'MX')
        print('##############')
        print('# MX Records #')
        print('##############\n')
        for fqdn in query_result:
            print(fqdn.to_text())
        print('\n')
    except dns.resolver.NXDOMAIN:
        print('\nDomain ', url_addy, 'does not exist')
