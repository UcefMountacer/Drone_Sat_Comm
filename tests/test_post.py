
import requests

iridium_url = 'https://rockblock.rock7.com/rockblock/MT'
iridium_local_port = 45679
imei = '300434066803090'
username = 'nicolai.valenti@gmail.com'
password = 'thisisamomentarypass'


data = '[254, 30, 43, 1, 1, 24, 226, 133, 203, 42, 0, 0, 0, 0, 60, 96, 89, 26, 63, 11, 45, 7, 113, 195, 0, 0, 132, 0, 242, 0, 40, 0, 215, 71, 3, 6, 57, 244]'
data = data.encode().hex()

url = iridium_url + "?imei=" + imei + "&username=" + "nicolai.valenti%40gmail.com" + "&username=" + username + "&password=" + password + "&password=" + password +"&data=" + data
headers = {"Accept": "text/plain"}
response = requests.request("POST", url, headers=headers)

if response.status_code == 200:
    print('success')
