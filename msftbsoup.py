from bs4 import BeautifulSoup #pip3 install BeautifulSoup4
import requests #pip3 install requests
import re # regex
import urllib #downloading
import os.path #filename

#get the website
html = requests.get('https://blogs.msdn.microsoft.com/mssmallbiz/2017/07/11/largest-free-microsoft-ebook-giveaway-im-giving-away-millions-of-free-microsoft-ebooks-again-including-windows-10-office-365-office-2016-power-bi-azure-windows-8-1-office-2013-sharepo/')

#Get it into Beautiful Soup
soup = BeautifulSoup(html.text, 'html.parser')

#parse it, get all the a href
for link in soup.find_all('a'):
    url = link.get('href')
    if re.search(r'http://ligman.me/*', url): # ligman.me is the link to download the books
        print('Downloading' + url)
        
        req = urllib.request.urlopen(url).url
        filename = os.path.basename(req) # get the filename
        urllib.request.urlretrieve(url, filename) #save with filename

        print('Done - ' + filename)
