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

class alarmLookup(ArubaCxBaseAction):
    def run(self):
        # Retuens a python dictionary of the vlans
        vlan_url = self.base + '/system/vlans'
        vlans = self.session.get(url=vlan_url,verify=False, timeout=2)
        vlans = json.loads(vlans.text)

        # Logout of the session
        url =  self.base + '/logout'
        response = self.session.post(url=url,cookies= self.cookie,verify=False)
        return (True, vlans)
