from bs4 import BeautifulSoup
import csv

dataType = {'Data Type - Databases': ['databases', 'SQL', 'SAP'],
            'Data Type - Applications': ['applications', 'program'],
            'Data Type - Emails': ['emails', 'passwords'], 
            'Data Type - Source Code': ['code'],
            'Data Type - Business Information': ['projects', 'documents', 'resumes', 'contracts', 'commercial', 'insurance', 'statements', 'certificates', 'internal', 'signed'],
            'Data Type - Designs': ['drawings', 'designs', 'media', 'projects'],
            'Data Type - Financial Information': ['financial', 'accounting', 'balances', 'invoices', 'financials', 'tax', 'budgets', 'fiscal', 'bank'],
            'Data Type - Research Information': ['research', 'studies'],
            'Data Type - Employee Information': ['employees', 'personal', 'HR', 'payrolls', 'payroll', 'scans', 'vaccine', 'criminal', 'medication', 'numbers'],
            'Data Type - Customer Information': ['customer', 'address', 'client', 'numbers'],
            'Data Type - Company Information': ['company', 'duration', 'operation'],
            'Data Type - Backup Systems Information': ['backups'],
            'Data Type - Supply Systems Information': ['suppliers'],
            'Data Type - Business Deals Information': ['partners', 'contracts', 'clients', 'negotiations'],
            'Data Type - Manufacturing Information': ['manufacturing'],}


file = open('Cuba_Victims.csv', 'w+', newline='', encoding='utf-8')
writer = csv.writer(file)
headers = (['Count','Company Targeted', 'Publish Date', 'Attacker', 'Industry', 'Latitude', 'Longitude', 'Location of Attack', 'Leak Size (In MB)'])
for key in dataType:
    headers.append(key)
writer.writerow(headers)
file.close()

count = 1

with open("etron.txt") as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

    company = soup.title.string.split()[0]

    info = soup.find_all("div", class_="page-list-files")
    date = "2022-06-01"

    attacker = "Cuba Ransomware"

    industry = "Technology"

    latitude = 24.783953143434864
    longitude = 121.0047218261935

    location = "114, Taiwan, Neihu District, Lane 35, Jihu Rd, 22號2 樓與10樓"

    leaksize = "-"

    datatype1 = 0
    datatype2 = 0
    datatype3 = 0
    datatype4 = 1
    datatype5 = 0
    datatype6 = 0
    datatype7 = 1
    datatype8 = 0
    datatype9 = 1
    datatype10 = 0
    datatype11 = 0
    datatype12 = 0
    datatype13 = 0
    datatype14 = 0
    datatype15 = 0


    
    description = soup.find_all("div", class_="page-list-span")
    for x in description:
        text = x.find('p').text

    file = open('Cuba_Victims.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    rows = ([count,company,date,attacker,industry,latitude,longitude,location,leaksize,datatype1,datatype2,datatype3,datatype4,datatype5,datatype6,datatype7,datatype8,datatype9,datatype10,datatype11,datatype12,datatype13,datatype14,datatype15])
    writer.writerow(rows)
    file.close()
    

with open("r1group.txt") as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

    company = soup.title.string.split()[0]

    info = soup.find_all("div", class_="page-list-files")
    date = "2022-06-22"

    attacker = "Cuba Ransomware"

    industry = "ConsultingServices"
    latitude = 41.89958112691735
    longitude = 12.409410174221735

    location = "Via Monte Carmelo, 5, 00166 Roma RM, Italy"

    leaksize = "-"

    datatype1 = 0
    datatype2 = 0
    datatype3 = 0
    datatype4 = 1
    datatype5 = 0
    datatype6 = 0
    datatype7 = 1
    datatype8 = 0
    datatype9 = 1
    datatype10 = 0
    datatype11 = 0
    datatype12 = 0
    datatype13 = 0
    datatype14 = 0
    datatype15 = 0


    
    description = soup.find_all("div", class_="page-list-span")
    for x in description:
        text = x.find('p').text

    file = open('Cuba_Victims.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    rows = ([count,company,date,attacker,industry,latitude,longitude,location,leaksize,datatype1,datatype2,datatype3,datatype4,datatype5,datatype6,datatype7,datatype8,datatype9,datatype10,datatype11,datatype12,datatype13,datatype14,datatype15])
    writer.writerow(rows)
    file.close()
    
with open("site-technology.txt") as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

    company = soup.title.string.split()[0]

    info = soup.find_all("div", class_="page-list-files")
    date = "2022-07-19"

    attacker = "Cuba Ransomware"

    industry = "Techology"
    latitude = 24.49278984176616
    longitude = 54.361949607354035

    location = "Hamdan Bin Mohammed St - Zone 1 - E3-02 - Abu Dhabi - United Arab Emirates"

    leaksize = "-"

    datatype1 = 0
    datatype2 = 0
    datatype3 = 0
    datatype4 = 1
    datatype5 = 0
    datatype6 = 0
    datatype7 = 1
    datatype8 = 0
    datatype9 = 1
    datatype10 = 0
    datatype11 = 0
    datatype12 = 0
    datatype13 = 0
    datatype14 = 0
    datatype15 = 0


    
    description = soup.find_all("div", class_="page-list-span")
    for x in description:
        text = x.find('p').text

    file = open('Cuba_Victims.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    rows = ([count,company,date,attacker,industry,latitude,longitude,location,leaksize,datatype1,datatype2,datatype3,datatype4,datatype5,datatype6,datatype7,datatype8,datatype9,datatype10,datatype11,datatype12,datatype13,datatype14,datatype15])
    writer.writerow(rows)
    file.close()

with open("skupstina.txt") as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

    company = soup.title.string.split()[0]

    info = soup.find_all("div", class_="page-list-files")
    date = "2022-08-19"

    attacker = "Cuba Ransomware"

    industry = "GovernmentAgency"
    latitude = 42.439979761465885
    longitude = 19.260386797845932

    location = "10 Bulevar Svetog Petra Cetinjskog, Podgorica 81000, Montenegro"

    leaksize = "-"

    datatype1 = 0
    datatype2 = 0
    datatype3 = 0
    datatype4 = 1
    datatype5 = 0
    datatype6 = 0
    datatype7 = 1
    datatype8 = 0
    datatype9 = 1
    datatype10 = 0
    datatype11 = 0
    datatype12 = 0
    datatype13 = 0
    datatype14 = 0
    datatype15 = 0
    
    description = soup.find_all("div", class_="page-list-span")
    for x in description:
        text = x.find('p').text

    file = open('Cuba_Victims.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    rows = ([count,company,date,attacker,industry,latitude,longitude,location,leaksize,datatype1,datatype2,datatype3,datatype4,datatype5,datatype6,datatype7,datatype8,datatype9,datatype10,datatype11,datatype12,datatype13,datatype14,datatype15])
    writer.writerow(rows)
    file.close()

with open("stm-com-tw.txt") as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

    company = soup.title.string.split()[0]

    info = soup.find_all("div", class_="page-list-files")
    date = "2022-07-04"

    attacker = "Cuba Ransomware"

    industry = "Technology"
    latitude = 22.834290032940658
    longitude = 120.30973802615402

    location = "No. 301, Tandi Rd, Gangshan District, Kaohsiung City, Taiwan 820"

    leaksize = "-"

    datatype1 = 0
    datatype2 = 0
    datatype3 = 0
    datatype4 = 1
    datatype5 = 0
    datatype6 = 0
    datatype7 = 1
    datatype8 = 0
    datatype9 = 1
    datatype10 = 0
    datatype11 = 0
    datatype12 = 0
    datatype13 = 0
    datatype14 = 0
    datatype15 = 0
    
    description = soup.find_all("div", class_="page-list-span")
    for x in description:
        text = x.find('p').text

    file = open('Cuba_Victims.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    rows = ([count,company,date,attacker,industry,latitude,longitude,location,leaksize,datatype1,datatype2,datatype3,datatype4,datatype5,datatype6,datatype7,datatype8,datatype9,datatype10,datatype11,datatype12,datatype13,datatype14,datatype15])
    writer.writerow(rows)
    file.close()

with open('TEST.txt','w') as w:
    w.write(text)