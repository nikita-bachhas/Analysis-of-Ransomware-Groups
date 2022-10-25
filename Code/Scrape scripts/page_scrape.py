import requests
import random
import re
import subprocess
import tldextract

session = requests.session()
session.proxies = {'http':  'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}

    	
    
for i in range(1, 5):
	url = "http://hl66646wtlp2naoqnhattngigjp5palgqmbwixepcjyq5i534acgqyad.onion/index.php?page=" + str(i)
	scrapeData = session.get(url).text
	textFile = open("./snatch/page" + str(i) + ".txt","w")
	textFile.write(scrapeData)
	textFile.close()
