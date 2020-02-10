# library to take inline args
import sys
# library to make REST requests
import requests
# regular expressions library
import re
# disable warnings that Web UI site is "insecure"
# needed to avoid connection timeout due to inability to verify server certificate
# from requests.packages.urllib3 import disable_warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# parameters
ver = 'v10.04'
# ver = 'v1'
ip = "10.132.0.215"
user = "admin"
passwd = "plexxi"

# create base address for REST requests (https://<ip>/rest/<ver>/)
base_url = '/'.join(['https:/',  ip])
base_uri = '/'.join([ '', 'rest',  ver,  ])
base =  base_url +  base_uri
# cookie jar to store cookies after login
cookie = requests.cookies.RequestsCookieJar()

print(base)
print(cookie)
s=requests.Session()

def status_handler(status_code):
    """
    determine if the response is good or bad
    :param int status_code: status code of response
    :return: whether response is good
    :rtype: bool
    """
    return (status_code == requests.codes.ok)

def logout():
    """
    logout of switch
    :return: whether logout was successful
    :rtype: bool
    """
    # url = https://<ip>/rest/<ver>/logout
    url =  base + 'logout'
    print("Logging out...")
    response = requests.post(url=url,cookies= cookie,verify=False)
    print(response)
    return  status_handler(response.status_code)

login = {'username': user, 'password': passwd}
print(login)
# url = https://<ip>/rest/<ver>/login
url =  base + '/login'
print(url)

print("Logging in...")
response = s.post(url=url,params=login,verify=False)
print(response)

# determine if login was successful
status =  status_handler(response.status_code)
# set cookie if login is successful
if (status):
    cookie.set('id', response.cookies['id'], domain= ip)
    print(status)
    print(cookie)

url =  base + '/logout'
print(url)

print("Logging out...")
response = s.post(url=url,cookies=cookie,verify=False)
print(response)

'''


'''
