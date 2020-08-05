#!/usr/bin/env python3

# (C) Copyright 2019-2020 Hewlett Packard Enterprise Development LP.
# Apache License 2.0

from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pyaoscx import session, vlan
import requests
import os

# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


base_url = "https://{0}/rest/{1}/".format('10.132.0.213','v1')
print(base_url)
session_dict = dict(s=session.login(base_url, 'admin', 'siesta3'), url=base_url)
vlan_data1 = vlan.get_all_vlans(**session_dict)
print("VLAN data: %s" % (vlan_data1))
print('Logging Out!')
session.logout(**session_dict)
