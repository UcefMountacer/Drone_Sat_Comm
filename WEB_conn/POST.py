

import requests

URL = 'https://rockblock.rock7.com/rockblock/MT'
PORT = 45679
IMEI = '300434066803090'
USER = 'nicolai.valenti@gmail.com'
PASS = 'thisisamomentarypass'


def post_to_rock7(Code):

    '''
    post to rock7 then rockblock
    '''

    if Code == None:

        #Nothing
        return 0

    iridium_url = URL
    iridium_local_port = PORT
    imei = IMEI
    username = USER
    password = PASS

    url = iridium_url + "?imei=" + imei + "&username=" + "nicolai.valenti%40gmail.com" + "&username=" + username + "&password=" + password + "&password=" + password +"&data=" + Code
    headers = {"Accept": "text/plain"}
    response = requests.request("POST", url, headers=headers)

    if response.status_code == 200:
        # print('success')
        return 1



