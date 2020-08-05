#!/usr/bin/env python3

# (C) Copyright 2019-2020 Hewlett Packard Enterprise Development LP.
# Apache License 2.0

"""
This workflow performs the following steps:
1. Create a VRF.
    a. Add route distinguisher to created VRF.
      Ex:
        vrf VRFa
            rd 1:1

2. Create two VLANs and SVIs
    a. Add IPv4 address to both SVIs
    b. Add DHCP helper IPv4 addresses to one SVI
    c. Attach both SVIs to VRF
      Ex:
        vlan 888
            name New Name for VLAN 888
            description New Description for VLAN 888
        vlan 999
            name New Name for VLAN 999
            description New Description for VLAN 999
        interface vlan888
            vrf attach VRFa
            description VLAN888 attached to VRFa
            ip address 10.10.88.88/24
        interface vlan999
            vrf attach VRFa
            description VLAN999 attached to VRFa
            ip address 10.10.99.99/24
            ip helper-address 1.1.1.1
            ip helper-address 2.2.2.2

4. Create L2 interface
      Ex:
        interface 1/1/20

5. Set L2 interface to 'access' VLAN mode
      Ex:
        interface 1/1/20
            no shutdown
            no routing
            vlan access 1

6. Assign one VLAN as access VLAN to the L2 interface
      Ex:
        interface 1/1/20
            no shutdown
            no routing
            vlan access 999

7. Print the ARP data for created VRF
      Ex:
        "VRF 'VRFa' ARP entries: []"

8. Modify the VLAN data and print updated data
      Ex:
        "VLAN '999' data: {'admin': 'up', ..., 'voice': False}
        VLAN '888' data: {'admin': 'up', ..., 'voice': False}"

Preconditions:
None
"""

from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pyaoscx import session,vlan

import requests
import os
import yaml
import logging

logging.basicConfig(level=logging.INFO)

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



data = {}
data['switchip']= '10.132.0.213'
data['version'] = 'v10.04'
data['username'] = 'admin'
data['password'] = 'siesta3'


base_url = "https://{0}/rest/{1}/".format(data['switchip'],data['version'])
session_dict = dict(s=session.login(base_url, data['username'], data['password']), url=base_url)
vlan_data1 = vlan.get_all_vlans(**session_dict)
print("VLAN data: %s" % (vlan_data1))
print('Logging Out!')
session.logout(**session_dict)

'''
vlan_data1 = vlan.get_all_vlans(**session_dict)
print('rick')
print(vlan_data1)

    try:
        session_dict = dict(s=session.login(base_url, data['username'], data['password']), url=base_url)

        # Add new VRF with optional route distinguisher to VRF table
        vrf.add_vrf(data['vrfname'], data['vrfrd'], **session_dict)

        vlan.create_vlan_and_svi(data['vlan1id'], data['vlan1name'], data['vlan1portname'], data['vlan1interfacename'],
                                 data['vlan1description'], data['vlan1ip'], data['vrfname'],
                                 data['vlan1portdescription'], **session_dict)

        vlan.create_vlan_and_svi(data['vlan2id'], data['vlan2name'], data['vlan2portname'], data['vlan2interfacename'],
                                 data['vlan2description'], data['vlan2ip'], data['vrfname'],
                                 data['vlan2portdescription'], **session_dict)

        # Add DHCP helper IPv4 addresses for SVI
        dhcp.add_dhcp_relays(data['vlan1portname'], data['vrfname'], data['ipv4helperaddresses'], **session_dict)

        # Add a new entry to the Port table if it doesn't yet exist
        interface.add_l2_interface(data['systemportname'], **session_dict)

        # Update the Interface table entry with "user-config": {"admin": "up"}
        interface.enable_disable_interface(data['systeminterfacename'], **session_dict)

        # Set the L2 port VLAN mode as 'access'
        vlan.port_set_vlan_mode(data['systemportname'], "access", **session_dict)

        # Set the access VLAN on the port
        vlan.port_set_untagged_vlan(data['systemportname'], data['vlan1id'], **session_dict)

        # Print ARP entries of VRF
        arp_entries = arp.get_arp_entries(data['vrfname'], **session_dict)
        print("VRF '%s' ARP entries: %s" % (data['vrfname'], repr(arp_entries)))

        # Modify the created VLANs
        vlan.modify_vlan(data['vlan1id'], "New Name for VLAN %s" % data['vlan1id'],
                         "New Description for VLAN %s" % data['vlan1id'], **session_dict)

        vlan.modify_vlan(data['vlan2id'], "New Name for VLAN %s" % data['vlan2id'],
                         "New Description for VLAN %s" % data['vlan2id'], **session_dict)

        # Print modified VLANs' data
        vlan_data1 = vlan.get_vlan(data['vlan1id'], **session_dict)
        print("VLAN '%d' data: %s" % (data['vlan1id'], repr(vlan_data1)))
        vlan_data2 = vlan.get_vlan(data['vlan2id'], **session_dict)
        print("VLAN '%d' data: %s" % (data['vlan2id'], repr(vlan_data2)))

        '''
