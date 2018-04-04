#!/usr/bin/python3

import pprint
import xmlrpc.client
import sys

pp = pprint.PrettyPrinter(indent=4)

api = xmlrpc.client.ServerProxy('https://rpc.ote.gandi.net/xmlrpc/')
apikey = '<MY OTE API KEY>'


def create_domain(domain):
    GANDI_ACCOUNT = 'SG43-GANDI'
    #GANDI_ACCOUNT = 'SG8593-GANDI'

    
    params = {
        'owner': GANDI_ACCOUNT,
        'admin': GANDI_ACCOUNT,
        'bill': GANDI_ACCOUNT,
        'tech': GANDI_ACCOUNT,
        'duration':1
    }
    
    op = api.domain.create(apikey, domain, params) 
    print(op)


print("*****************************************************")
print("Create domain")

create_domain('test02.com')


print("*****************************************************")
sys.exit(0)

