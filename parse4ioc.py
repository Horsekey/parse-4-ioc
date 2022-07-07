#!/usr/bin/env python3

import os
import requests
import sys
import csv
import socket


#input zeek log location,
#
#give argument to check ip, url, or hash
#
#normalize zeek data
#
#query APIs


def normalizeIPS(fileLocation):
  files = [fileLocation]

  # NEED TO LOOP THROUGH THE FILES AND ADD TO FILE JUST TEMP

  unique_values = []

  with open('conn.log','r') as infile:
    ips = [ cols[2:3] for cols in csv.reader(infile, delimiter="\t") ]

    for i in ips:
      try:
          socket.inet_aton((''.join(i)))
          if i not in unique_values:
            unique_values.append(i)
      except socket.error:
        continue
  return unique_values

def normalizeHash():
  print("test")

def main(ips):

  url = "https://threatfox-api.abuse.ch/api/v1/"
  for ip in ips:
    #print(''.join(ip))
    payload = {"query" : "search_ioc", "search_term" : (''.join(ip)) }
    headers = {'Content-Type': 'application/json'}
    
    response = requests.request("POST", url, headers=headers, json=payload)

    if "no_result" in response.text:
      print("NO RESULT")
    else:
      print("RESULT")
      print(response.json())

if __name__ == '__main__':
  main(normalizeIPS())

