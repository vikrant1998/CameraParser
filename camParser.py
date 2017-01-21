"""
--------------------------------------------------------------------------------
Descriptive Name     : camParser.py
Author               : Vikrant Satheesh Kumar
Contact Info         : vsathees@purdue.edu
Date Written         : 1/21/2017
Description          : Parse data on NYC dot website
Command to run script: python camParser.py
Usage                : N/A
Input file format    : N/A
Output               : N/A
Note                 :
Other files required by : This code requires PhantomJS, a headless web browser.
this script and where
located

----For Parsing Scripts---------------------------------------------------------
Website Parsed       : www.dotsignals.org
In database (Y/N)    : Y
Date added to Database : N/A
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
        PHANTOMJS_PATH = '/usr/local/bin/phantomjs'

    browser = webdriver.PhantomJS(PHANTOMJS_PATH)

    # Create a file to store the camera info.
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

        # Finding the image tags using BeautifulSoup
        snapshot_url = soup.find('img').get('src')

        # Checking if the camera is inactive.
        if re.search (r'img/inactive', snapshot_url) == None:
            snapshot_url = re.search(r'(?P<URL>[\w\.\/:\\]*)', snapshot_url).group('URL')
            f.write (content+"#"+str(snapshot_url)+"#"+latitude+"#"+longitude+"#"+"USA#NY#New York\n")

        print (snapshot_url)
        pass

    f.close()
    return

if __name__ == '__main__':
    print ("Getting started")
    nycdot()
