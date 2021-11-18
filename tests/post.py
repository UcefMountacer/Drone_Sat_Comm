

import requests

iridium_url = 'https://rockblock.rock7.com/rockblock/MT'
iridium_local_port = 45679
imei = '300434066803090'
username = 'nicolai.valenti@gmail.com'
password = 'thisisamomentarypass'

# data = b"MISSION_ITEM {target_system : 1, target_component : 1, seq : 0, frame : 3, command : 16, current : 2, autocontinue : 1, param1 : 0.0, param2 : 0.0, param3 : 0.0, param4 : 0.0, x : -35.362548828125, y : 149.163818359375, z : 9.979999542236328}".hex()
# data = b'COMMAND_LONG {target_system : 1, target_component : 1, command : 519, confirmation : 0, param1 : 1.0, param2 : 0.0, param3 : 0.0, param4 : 0.0, param5 : 0.0, param6 : 0.0, param7 : 0.0}'.hex()


data = 'COMMAND_LONG {target_system : 1, target_component : 1, command : 519, confirmation : 0, param1 : 1.0, param2 : 0.0, param3 : 0.0, param4 : 0.0, param5 : 0.0, param6 : 0.0, param7 : 0.0}'
data = data.encode().hex()

url = iridium_url + "?imei=" + imei + "&username=" + "nicolai.valenti%40gmail.com" + "&username=" + username + "&password=" + password + "&password=" + password +"&data=" + data
headers = {"Accept": "text/plain"}
response = requests.request("POST", url, headers=headers)

if response.status_code == 200:
    print('success')

