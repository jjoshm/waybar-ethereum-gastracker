#!/usr/bin/env python3
import json
import requests
import re
import time

class Tracker:
    def __init__(self):
        # fake headers to bypass cloudflare security
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        self.session = requests.Session()
        self.average = 0
        self.cssClass = 'average'
        self.getSid()
        self.loop()

    def getSid(self):
        req = self.session.get('https://etherscan.io/gastracker', headers=self.headers)
        regex = r"var sid = '(.*)';"
        api_sid = re.findall(regex, req.text)[0]
        self.sid = api_sid

    def loop(self):
        counter = 0
        sum = 0
        while True:
            req = self.session.get('https://etherscan.io/autoUpdateGasTracker.ashx?sid=' + self.sid, headers=self.headers)
            status_code = req.status_code
            if status_code != 200:
                self.getSid()
                continue
            data = req.json()
            self.data = data
            counter += 1
            sum = sum + int(data['avgPrice'])
            self.average = sum / counter
            self.calcClass()
            self.output()            
            time.sleep(10)

    def calcClass(self):
        cssClass = 'average'
        avgPrice = int(self.data['avgPrice'])
        difference = avgPrice - self.average
        percentage_difference = (avgPrice / 100) * abs(difference)
        if percentage_difference > 10:
            if difference > 0:
                cssClass = 'high'
            else:
                cssClass = 'low'
        self.cssClass = cssClass

    def output(self):
        text = "low: " + self.data['lowPrice'] + ' avg: ' + self.data['avgPrice'] + ' high: ' + self.data['highPrice']
        out = {'text': text, 'class': self.cssClass}
        print(json.dumps(out), flush=True)

if __name__ == "__main__":
    tracker = Tracker()