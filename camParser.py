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

def nycdot():
    print ("NYC dot")

    JSonURL = "http://dotsignals.org/new-data.php" # JSON File containing MAP data.
    CameraPopupURL = "http://dotsignals.org/google_popup.php?cid=" # Camera URL access.

    f = open ('nycdot_list', 'w') # Write to an output file.

    #Header Info
    

    #load JSON file into the response to parse.
    response = urllib2.urlopen(JSonURL).read()

    #Parse the given response.
    parsed_json = json.loads(response)



    return

if __name__ == '__main__':
    print ("Getting started")
    nycdot()
