import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
s=requests.Session()
# cookie jar to store cookies after login
cookie = requests.cookies.RequestsCookieJar()
# Set URL
base_url = '/'.join(['https:/','10.132.0.213'])
# base_uri = '/'.join([ '', 'rest','v1',  ])
base_uri = '/'.join([ '', 'rest','v10.04',  ])
base =  base_url +  base_uri
url =  base + '/login'

# Set User/pass
login = {'username': 'admin', 'password': 'siesta3'}
# Send REST to login
response = s.post(url=url,params=login,verify=False)
print 'did you auth?'
print response

# Send vlan to the AurbaCX switch
vlan_data={}
vlan_data['name'] = 'bob'
vlan_data['description'] = 'super duper vlan'
vlan_data['id'] = '666'
vlan_data['admin'] = 'up'
print vlan_data
# create the vlans url
vlan_url = base + '/system/vlans'
print vlan_url
print len(vlan_url)

# Post to the Aruba CX switch
response = s.post(url=vlan_url,data=json.dumps(vlan_data),verify=False)
print response

# Logout of the session
url =  base + '/logout'
logout = s.post(url=url,cookies=cookie,verify=False)
