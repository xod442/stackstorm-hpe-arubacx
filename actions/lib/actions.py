#!/usr/bin/env python3
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# (C) Copyright 2019-2020 Hewlett Packard Enterprise Development LP.
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

import requests
from st2common.runners.base_action import Action
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import logging

logging.basicConfig(level=logging.INFO)
from pyaoscx import session

class ArubaCxBaseAction(Action):
    def __init__(self,config):
        super(ArubaCxBaseAction, self).__init__(config)
        self.username, self.version, self.switchip, self.password = self._get_client()

    def _get_client(self):
        # self.config['username'] = 'admin'
        # self.config['password'] = 'siesta3'

        base_url = "https://{0}/rest/{1}/".format('10.132.0.213', 'v10.04')
        # base_url = "https://{0}/rest/{1}/".format(self.config['switchip'], self.config['version'])
        print(base_url)
        try:
            session_dict = dict(s=session.login(base_url, 'admin', 'siesta3'), url=base_url)
            # session_dict = dict(s=session.login(base_url, self.config['username'], self.config['password']), url=base_url)
        except Exception as error:
            print('Ran into exception: {}. Logging out..'.format(error))
            session.logout(**session_dict)
        return (session, session_dict)
