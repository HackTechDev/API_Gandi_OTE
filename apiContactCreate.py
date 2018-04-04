#!/usr/bin/python3

import pprint
import xmlrpc.client
import sys
import string
import random

pp = pprint.PrettyPrinter(indent = 4)

api = xmlrpc.client.ServerProxy('https://rpc.ote.gandi.net/xmlrpc/')
# INSERT YOUR OWN API KEY
apikey = '<MY OTE API KEY>'


def get_handle():
    contacts = api.contact.list(apikey)
    pp.pprint(contacts)
    '''
    for contact in contacts:
        #pp.pprint(contact)
        type = contact['type']
        pp.pprint(type)
        pp.pprint('**************')
    #return contacts 
    '''

def generate_domainname(size = 10):
    domainname = '' . join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(size))
    return 'api' + domainname


def create_contact():
    contact_desc = {
                'given': 'First Name',
                'family': 'Last Name',
                'email': 'example@example.com',
                'streetaddr': 'My Street Address',
                'zip': '75011',
                'city': 'Paris',
                'country': 'FR',
                'phone':'+33.123456789',
                'type': 0,
                'password': 'mot2passe'}
    info = api.contact.create(apikey, contact_desc)
    return info


def domain_available(domain):
    d = domain.split('.')
    if len(d) > 1:
        l = [domain]
    else:
        l = []
        for tld in ['.com', '.net', '.org', '.xyz']:
            l.append(domain + tld)

    result = api.domain.available(apikey, l)
    import time
    while result[l[0]] == 'pending':
        time.sleep(0.3)
        result = api.domain.available(apikey, l)
    return result

def create_domain(domain):
    # USER YOUR OWN GANDI HANDLE ASSOCIATED TO YOUR GANDI ACCOUNT
    #GANDI_ACCOUNT = 'SG8593-GANDI'
    GANDI_ACCOUNT = 'SG43-GANDI'
    res = domain_available(domain)
    if res.get(domain) != 'available':
        print(domain)
        print('Not available')
        return
    else:
        print(domain)
        print('Available')


    contact_info = create_contact()
    handle = contact_info.get('handle')
    print('contact created: ' + handle + '\n\n')

    params = {
        'owner': GANDI_ACCOUNT,
        'admin': GANDI_ACCOUNT,
        'bill' : GANDI_ACCOUNT,
        'tech' : GANDI_ACCOUNT,
        'duration':1
    }
    op = api.domain.create(apikey, domain, params) 
    print(op)

def domain_info(domain):
    info = api.domain.info(apikey, domain)
    return info



print("*****************************************************")
print("Domain create")


domainName = generate_domainname() + '.com'
create_domain(domainName)

sys.exit(0)


