
import requests

iridium_url = 'https://rockblock.rock7.com/rockblock/MT'
iridium_local_port = 45679
imei = '300434066803090'
username = 'nicolai.valenti@gmail.com'
password = 'thisisamomentarypass'


data = 'testing POST to rockblock'
data = data.encode().hex()

url = iridium_url + "?imei=" + imei + "&username=" + "nicolai.valenti%40gmail.com" + "&username=" + username + "&password=" + password + "&password=" + password +"&data=" + data
headers = {"Accept": "text/plain"}
response = requests.request("POST", url, headers=headers)

if response.status_code == 200:
    print('success')
