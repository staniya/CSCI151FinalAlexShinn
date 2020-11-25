__name__ = 'UrlToJpg'
__author__ = 'Yann-NTECH'
__version__ = 0.3
__date__ = '05-10-2020'
__updated__ = '12-10-2020'

import pandas as pd
from urllib.request import ProxyHandler, build_opener, install_opener, urlretrieve
from urllib.parse import urlparse
from urllib.error import HTTPError
from os import makedirs
from os.path import isdir

# Constants
PROXY_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
FILENAME = '/csvfiles/hip hop.csv'
FILE_PATH = 'pictures/'

# Variables
ReportList = []

# Functions
def getProxy(user_agent):
    '''
    set the proxy to avoid the Forbidden 403 error
    :param user_agent: set User Agent
    :return: None
    '''
    proxy = ProxyHandler({})
    opener = build_opener(proxy)
    opener.addheaders = [('User-Agent', user_agent)]
    install_opener(opener)

def report(list):
    """
    csv report containing url and downloaded image
    :list: data to include in csv
    :return: None
    """
    dl_data = pd.DataFrame(list)
    dl_data.to_csv('report.csv')

def urlToJpg(i, url, file_path):
    """
    convert url file to jpg
    :param i: number of image
    :param url: URL address of a given image
    :param file_path: where to save image downloaded
    :return: None
    """
    try:
        urlParsed = urlparse(url)
        pathName = urlParsed.path
        pathName = pathName.replace('/', '_')
        ReportList.append([url, pathName])
        print('URL : {url} - PICTURE : {pathName} saved'.format(url=url, pathName=pathName))
        full_path = ('{file_path}{pathName}').format(file_path=file_path, pathName=pathName)
        urlretrieve(url=url, filename=full_path)

    except HTTPError as exception:
        ReportList.append([url, exception])
        print('URL : {url} - PICTURE : {exception} saved'.format(url=url, pathName=exception))
        return None

# Program
print('#'*50)
print('################### Url_to_jpg ################### ')
print('#'*50)

# make pictures folder
try:
 makedirs('pictures')
except OSError:
 if not isdir('pictures'):
    raise

# Set proxy
getProxy(PROXY_USER_AGENT)

# Read csv -> urls list
urls = pd.read_csv(FILENAME)

# Save image to dir by iterating urls list
for i, url in enumerate(urls.values):
    urlToJpg(i, url[0], FILE_PATH)

report(ReportList)
print('\nreport.csv edited')
input('\nProcess completed. Press any key to exit')