#!/usr/bin/env python3

import os
import requests
import sys
import csv
import socket
import argparse


#input zeek log location,
#
#give argument to check ip, url, or hash
#
#normalize zeek data
#
#query APIs

#python3 parse4ioc.py -h [help] -p [path of log files] -t [type of ioc to parse (supported: IPs, DNS, PE files)]


parser = argparse.ArgumentParser(description="This is a test description")

parser.add_argument("--path", 
  "-p", 
  default=os.getcwd(), 
  help="Path to your zeek log files (default: current working directory)"
)

parser.add_argument("--type", 
  "-t", 
  default="A", 
  help="Type of IOC to parse. Options: [I]Ps, [H]ashes, [U]RLs, [A]ll (default: all)"
)

def normalizeIPS(args):
  unique_values = []

  with open(args.path + '\\' + 'conn.log','r') as infile:
    response_ips = [ cols[4:5] for cols in csv.reader(infile, delimiter="\t") ]
    origin_ips = [ cols[2:3] for cols in csv.reader(infile, delimiter="\t") ]

    ips = response_ips + origin_ips

    for i in ips:
      try:
          socket.inet_aton((''.join(i)))
          if i not in unique_values:
            unique_values.append(i)
      except socket.error:
        continue
  return unique_values

def normalizeHash(args):
  print("test")

def queryAPI(ips):
  url = "https://threatfox-api.abuse.ch/api/v1/"
  for ip in ips:
    #print(''.join(ip))
    payload = {"query" : "search_ioc", "search_term" : (''.join(ip)) }
    headers = {'Content-Type': 'application/json'}
    
    response = requests.request("POST", url, headers=headers, json=payload)

    if "no_result" in response.text:
      print("NO RESULT")
    else:
      print(ip)
      print("RESULT")
      print(response.json())

def main(args):

  if args.type == "A":
    queryAPI(normalizeIPS(parser.parse_args()))
    

if __name__ == '__main__':
  main(parser.parse_args())