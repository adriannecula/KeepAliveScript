import requests
import time


def periodicRequest():
    while True:
        receive = requests.get('http://nab-grinder-converter.herokuapp.com')
        print(receive.status_code)
        time.sleep(600)


periodicRequest()
