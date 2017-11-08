import json
import urllib.request
from pprint import pprint


# Enter your API info here. Refer to Incapsula's documentation..
api_id = ""
api_key = ""
site_id = ""

# This will add all of the IP's in the block list.
# Any IP's previously in the list will be replaced.
rule_id = "api.acl.blacklisted_ips"

# change this section to input a file or an ip as an argument
ips = "1.2.3.4,192.168.1.1-192.168.1.100,192.168.1.1/24"

baseUrl = 'https://my.incapsula.com'
json_raw = json
restUrl = '/api/prov/v1/sites/configure/acl'

params = {
    "api_id": api_id,
    "api_key": api_key,
    "site_id": site_id,
    "rule_id": rule_id,
    "ips": ips
}

try:
    data = urllib.parse.urlencode(params)
    data = data.encode('ascii')
    req = urllib.request.Request(baseUrl + restUrl, data)
    with urllib.request.urlopen(req, timeout=10) as response:
        json_raw = json.loads(response.read().decode('utf8'))
        pprint('JSON Response: %s' % json_raw)
        pprint(json_raw)
except urllib.error.URLError as e:
    print('Error:', e)
