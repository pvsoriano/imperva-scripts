import json
import urllib.request
from pprint import pprint
import argparse
import sys

# Enter your API and Site ID info here. Refer to Incapsula's documentation.
api_id = ""
api_key = ""
site_id = ""

# This will add all of the IP's in the block list.
# Any IP's previously in the list will be replaced.
rule_id = "api.acl.blacklisted_ips"

# Setting variables
ip_str = ""
ip_list = []
baseUrl = 'https://my.imperva.com'
json_raw = json
restUrl = '/api/prov/v1/sites/configure/whitelists'

# Check to see if a file is passed
if len(sys.argv) < 1:
	print("Need to supply file.")
else:
	ip_file = sys.argv[1] 
	
# Read the IP's from the file into a list
with open(ip_file, 'r') as f:
	for line in f:
		line = line.strip()
		ip_list.append(line)

# Convert list into string of IP's
ip_str = ','.join(map(str, ip_list))
print(ip_str)

# Set parameters for Incapsula API
params = {
    "api_id": api_id,
    "api_key": api_key,
    "site_id": site_id,
    "rule_id": rule_id,
    "ips": ip_str
}

# Send API request to Incapsula
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
