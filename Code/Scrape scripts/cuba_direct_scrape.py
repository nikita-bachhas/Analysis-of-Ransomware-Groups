import requests
import random
import re
import subprocess
import tldextract

session = requests.session()
session.proxies = {'http':  'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}

    	
with open("links.txt", "r") as websites:
	content = websites.read().splitlines()
    
for website in range(0, len(content)):
	scrapeData = session.get(content[website]).text
	#url_extract = tldextract.extract(content[website])
	textFile = open("./cuba/" + content[website].split('/')[-2] + ".txt","w")
	textFile.write(scrapeData)
	textFile.close()
