#!/usr/bin/python3

import pprint
import xmlrpc.client
import sys
import time 

pp = pprint.PrettyPrinter(indent=4)

api = xmlrpc.client.ServerProxy('https://rpc.ote.gandi.net/xmlrpc/')
apikey = '<MY OTE API KEY>'
domain = 'api9ll6cpayra.com'

print("*****************************************************")
print("Domain name serveur set")

result =  api.domain.nameservers.set(apikey, domain, ['atest.dns.gandi.net', 'btest.dns.gandi.net', 'ctest.dns.gandi.net'], )
pp.pprint(result)


print("*****************************************************")
sys.exit(0)
