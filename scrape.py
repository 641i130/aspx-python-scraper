# Disclaimer: This is for educational purposes only and shouldn't be used on sites without permission
# Developed by 641i130

import requests
from bs4 import BeautifulSoup
import numpy as np
import urllib
import urllib2
import cookielib
import shutil
import io
# defines the array of the list of file names
ids = np.genfromtxt("a list of file names",delimiter=",")
# defines the headers of the 'browser' it is using
headers = {
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
#info to login from the post request
login_data = {
"":"",
"":""

}

with requests.Session() as s:
    # defines url
    url = "website url"
    # gets the website using the headers
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html5lib")
    # logins into the website using the login and headers just in case
    r = s.post(url, data=login_data, headers=headers)
    #loop through each part array using the length of the file to download each image
    # optional, changes school but will need a different list of images

    # Used to set cookies of site for certain files only allowed for certain locations
    s.cookies.set('', '', domain='', path='/')

    for id in ids:
        # gets file link with the file name list
        r = s.get("website url file location" + str(int(id)), stream=True)

        # saves image to the folder, images with the name as the file name
        with open('./folder to store files' + str(int(id)) + '.jpg', 'wb') as f:
            r.raw.decode_content = False
            shutil.copyfileobj(r.raw, f)
            print("Downloaded: " + str(int(id)))
