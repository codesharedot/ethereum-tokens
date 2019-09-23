#!/usr/bin/python3
import time
import os
import json
import requests
from bs4 import BeautifulSoup
import csv
import sys
from time import sleep
from time import gmtime, strftime
import re

r  = requests.get("https://etherscan.io/tokens")
data = r.text

soup = BeautifulSoup(data, "html.parser")
table = soup.find('table', attrs={ "class" : "table"})
for row in table.find_all('tr'):
    tag = row.findAll('td')
    if len(tag) >= 7:
        token = tag[1]
        token = re.sub('<[^<]+?>', '', str(token))
        if ")" in token:
            token = token[0:token.index(")")+1]
            print(token)
