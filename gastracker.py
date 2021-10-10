#!/usr/bin/env python3

import json
import requests
import re
import time
import sys

class Tracker:
    def __init__(self):
        # fake headers to bypass cloudflare security
        self.parseArgs()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        self.session = requests.Session()
        self.getSid()
        self.loop()

    def parseArgs(self):
        if len(sys.argv) < 3:
            self.low = 50
            self.average = 100
        else:
            self.low = int(sys.argv[1])
            self.average = int(sys.argv[2])

    def getSid(self):
        req = self.session.get('https://etherscan.io/gastracker', headers=self.headers)
        regex = r"var sid = '(.*)';"
        api_sid = re.findall(regex, req.text)[0]
        self.sid = api_sid

    def loop(self):
        while True:
            req = self.session.get('https://etherscan.io/autoUpdateGasTracker.ashx?sid=' + self.sid, headers=self.headers)
            status_code = req.status_code
            if status_code != 200:
                self.getSid()
                continue
            data = req.json()
            self.data = data;
            self.output()
            time.sleep(5)

    def output(self):
        text = "low: " + self.data['lowPrice'] + ' avg: ' + self.data['avgPrice'] + ' high: ' + self.data['highPrice']
        css_class = "low"
        if int(self.data['avgPrice']) > self.average:
            css_class = "high"
        elif int(self.data['avgPrice']) > self.low:
            css_class = "average"
        out = {'text': text, 'class': css_class}
        print(json.dumps(out), flush=True)

if __name__ == "__main__":
    tracker = Tracker()