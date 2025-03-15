import dns.resolver

def get_a_record(url_addy):
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