# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:02:31 2018

@author: omni 220
"""
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


OECD_url='http://stats.oecd.org/sdmx-json/data/QNA/AUS+AUT.GDP+B1_GE.CUR+VOBARSA.Q/all?startTime=2009-Q2&endTime=2011-Q4&dimensionAtObservation=allDimensions'
data=requests.get(OECD_url)
data1=data.json()
data2=data.headers
