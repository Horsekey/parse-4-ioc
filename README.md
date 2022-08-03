# parse-4-ioc
Python utility to take zeek log files and parse for different IOCs
> [Reed Huskey](https://horsekey.webflow.io) | July 5, 2022

## Usage

```
  usage: parse4ioc.py [-h] [--path PATH] [--type TYPE]

  utility that parses indicators of compromise from zeek log files, checks them against threat intelligence APIs, and generates a basic report. 

  optional arguments:
    -h, --help            show this help message and exit
    --path PATH, -p PATH  Path to your zeek log files (default: current working directory)
    --type TYPE, -t TYPE  Type of IOC to parse. Options: [I]Ps, [H]ashes, [U]RLs, [A]ll (default: all)
```

## Threat Intelligence APIs

ThreatFox is a free platform from abuse.ch with the goal of sharing indicators of compromise (IOCs) associated with malware with the infosec community, AV vendors and threat intelligence providers.

>  https://threatfox.abuse.ch/

A Fast and Reliable service that enables you to extract IOCs and intelligence from different data sources.

> https://docs.iocparser.com/api-reference/parse-api



## Possible additions

> https://developers.virustotal.com/reference/public-vs-premium-api

> https://cinsscore.com/

### JSON Visualization
> https://shiny.rstudio.com/py/index.html
