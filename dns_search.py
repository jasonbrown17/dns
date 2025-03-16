#!/usr/bin/python3

'''
Script to perform various DNS query tasks
'''

__author__ = 'Jason Brown'
__email__ = 'jason@jasonbrown.us'
__date__ = '20250316'

import sys
from resolver import sentinel
from dns_records import records

def main():

    '''
    Main function call
    Used to receive option from STDIN
    '''

    if len(sys.argv) < 2:
        print('Type ./dns_search.py --help')
        sys.exit()
    if sys.argv[1].startswith('--'):
        option = sys.argv[1][2:]
        if option == 'help':
            print('Usage ./dns_search.py [option]\n\
                        --a\n\
                        --aaaa\n\
                        --soa\n\
                        --ns\n\
                        --txt\n\
                        --mx\n\
                        --sentinel\n\
                        --version\n\
                ')
        elif option == 'a':
            url_addy = input('Enter in URL: ')
            records.get_a_record(url_addy)
        elif option == 'aaaa':
            url_addy = input('Enter in URL: ')
            records.get_aaaa_record(url_addy)
        elif option == 'soa':
            url_addy = input('Enter in URL: ')
            records.get_soa_server(url_addy)
        elif option == 'ns':
            url_addy = input('Enter in URL: ')
            records.get_ns_server(url_addy)
        elif option == 'mx':
            url_addy = input('Enter in URL: ')
            records.get_mx_records(url_addy)
        elif option == 'txt':
            url_addy = input('Enter in URL: ')
            records.get_txt_records(url_addy)
        elif option == 'sentinel':
            sentinel.main()
        elif option == 'version':
            print('DNS Search 1.0')
        else:
            print('No option selected')

if __name__ == '__main__':


    main()
