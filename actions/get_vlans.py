# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF AN.Y KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

from lib.actions import ArubaCxBaseAction
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pyaoscx import session,vlan

import requests

logging.basicConfig(level=logging.INFO)

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class getVlans(ArubaCxBaseAction):
    def run(self):
        # Returns a python dictionary of the vlans
        vlan_data1 = vlan.get_all_vlans(self.**session_dict)
        # Logout of the session
        self.session.logout(self.**session_dict)
        return (True, vlans_data1)
