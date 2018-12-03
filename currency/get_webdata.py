# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:49:03 2018

@author: omni 220
"""

import requests

def get_data():
    OECD_url='http://stats.oecd.org/sdmx-json/data/QNA/AUS+AUT.GDP+B1_GE.CUR+VOBARSA.Q/all?startTime=2009-Q2&endTime=2011-Q4&dimensionAtObservation=allDimensions'
    data=requests.get(OECD_url)
    data1=data.json()
    data2=data.headers
    print('hello111')
    return data2
#for d in data2: print(d, sep ='t')

get_data()