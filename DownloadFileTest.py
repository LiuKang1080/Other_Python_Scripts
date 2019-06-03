"""
Download file from a given link.
"""

import urllib

def downloadFile(URL, ZipFilePath):
    urllib.urlretrieve(URL, ZipFilePath)

