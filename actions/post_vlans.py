# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

from lib.actions import ArubaCxBaseAction
import json

class PostVlan(ArubaCxBaseAction):
    def run(self, name=None, description=None, id=None, admin=None):
        # Send clan to the AurbaCX switch
        vlan_data={}
        vlan_data['name'] = name
        vlan_data['description'] = description
        vlan_data['id'] = id
        vlan_data['admin'] = admin

        # create the vlans url
        vlan_url = self.base + '/system/vlans'
        # Post to the Aruba CX switch
        response = self.session.post(url=vlan_url,data=json.dumps(vlan_data),verify=False)
        # Logout of the session
        url =  self.base + '/logout'
        logout = self.session.post(url=url,cookies=self.cookie,verify=False)
        # Validate response
        if response.status_code == 201:
            return(True, response)
        return (False, response.status_code)
