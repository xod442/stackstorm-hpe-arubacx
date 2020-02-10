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

import requests
from st2common.runners.base_action import Action

class ArubaCxBaseAction(Action):
    def __init__(self,config):
        super(ArubaCxBaseAction, self).__init__(config)
        self.client, self.cookie = self._get_client()

    def _get_client(self):
        # create base address for REST requests (https://<ip>/rest/<ver>/)
        s=requests.Session()
        # cookie jar to store cookies after login
        cookie = requests.cookies.RequestsCookieJar()
        # Set URL
        base_url = '/'.join(['https:/',  self.config['ipaddress']])
        base_uri = '/'.join([ '', 'rest', self.config['version'],  ])
        base =  base_url +  base_uri
        url =  base + '/login'
        # Set User/pass
        login = {'username': self.config['username'], 'password': self.config['password']}
        # Send REST to login
        response = s.post(url=url,params=login,verify=False)

        if response.status_code == requests.codes.ok:
            cookie.set('id', response.cookies['id'], domain= ip)
            return client cookie
        else:
            print('Base Action Failure: No cookies for you')
