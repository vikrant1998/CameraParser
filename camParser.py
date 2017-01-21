"""
--------------------------------------------------------------------------------
Descriptive Name     : camParser.py
Author               : Vikrant Satheesh Kumar
Contact Info         :
Date Written         :
Description          : (eg. Parse cameras on the Atlanta, Georgia traffic camera website)
Command to run script: (eg. python <filename>)
Usage                : (extra requirements to run the script: eg. have to be run within dev server)
Input file format    : (eg. url#description (on each line))
Output               : (eg. <file name> or <on screen>)
Note                 :
Other files required by : N/A
this script and where
located

----For Parsing Scripts---------------------------------------------------------
Website Parsed       : <insert url>
In database (Y/N)    :
Date added to Database :
--------------------------------------------------------------------------------
"""
from bs4 import BeautifulSoup
import urllib2
import re
import sys
import time
import json
from selenium import webdriver
import platform

def nycdot():
    print ("NYC dot")

    JSonURL = "http://dotsignals.org/new-data.php" # JSON File containing MAP data.
    CameraPopupURL = "http://dotsignals.org/google_popup.php?cid=" # Camera URL access.

    if platform.system() == 'Windows':
        PHANTOMJS_PATH = './phantomjs.exe'
    else:
        PHANTOMJS_PATH = './phantomjs'

    browser = webdriver.PhantomJS(PHANTOMJS_PATH)

    f = open ('nycdot_list', 'w') # Write to an output file.

    #Header Info
    f.write ("description#snapshot_url#latitude#longitude#country#city\n")

    #load JSON file into the response to parse.
    response = urllib2.urlopen(JSonURL).read()

    #Parse the given response.
    parsed_json = json.loads(response)

    #get the markers to help parse.
    cameras = parsed_json ['markers']

    for camera in cameras:
        cam_id    = camera['id']
        content   = camera['content']
        latitude  = camera['latitude']
        longitude = camera['longitude']
        url       = CameraPopupURL + cam_id

        browser.get(url)
        soup = BeautifulSoup(browser.page_source)

        snapshot_url = soup.find('img').get('src')
        print (snapshot_url)
        pass

    f.close()
    return

if __name__ == '__main__':
    print ("Getting started")
    nycdot()
