from bs4 import BeautifulSoup
import csv
import re
import urllib.parse
from datetime import datetime

industries = {'GovernmentAgency': ['national','instituto','government', 'defense', 'homeland security','federal','state', 'social', 'county', 'confederation','ministry'], 
              'Agriculture': ['agriculture', 'crop', 'farms'], 
              'Supermarket': ['supermarket', 'grocery'], 
              'Technology': ['technology-based','technology','wireless', 'communication', 'digital'],
              'Security': ['security', 'secure','intelligence', 'surveillance', 'reconnaissance'],
              'Motor/Vehicular': ['vehicles','driving','car','drive', 'motorcycles', 'snowmobiles'],
              'Medical': ['medical', 'health', 'hospital', 'clinic', 'pharmaceutical', 'pathology'],
              'RealEstate': ['estate'],
              'School': ['school', 'college'],
              'Airline': ['airline','flights'],
              'ConsultingServices': ['consulting'],
              'Cosmetics': ['cosmetics', 'suplements', 'beauty', 'skin care'],
              'NonProfitOrganisation': ['community', 'in need', 'communities', 'voluntary'],
              'Water': ['water'],
              'Legal': ['legal', 'law'],
              'HeavyMachineryManufacturer': ['forklifts'],
              'Accountancy': ['accountants'],
              'Pipes': ['tubular'],
              'Fuel/Oil': ['fuel', 'petrol','propance'],
              'Construction/Renovation': ['barrier', 'roofing', 'waterproofing', 'construction', 'building'],
              'Aerospace': ['turbine engine'],
              'Unions': ['union'],
              'DrinkManufacturer': ['drink'],
              'ConventionCentre': ['meeting', 'exhibition'],
              'Accessories': ['accessories'],
              'Glass': ['glass'],
              'Food': ['food'],
              'Welding': ['metal', 'material'],
              'Finance': ['commerce'],
              'Retailer': ['consumer'],
              'Diamond': ['diamond'],
              'Cinema/Movie': ['PVR Ltd.'], 
              'Multimedia': ['multimedia', 'television', 'productions', 'films', 'advertising'],
              'Drilling': ['drilling', 'rigs']}

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


file = open('Lorenz.csv', 'w+', newline='', encoding='utf-8')
writer = csv.writer(file)
headers = (['Count','Company Targeted', 'Publish Date', 'Attacker', 'Industry', 'Latitude', 'Longitude', 'Location of Attack', 'Leak Size (In MB)'])
for key in dataType:
    headers.append(key)
writer.writerow(headers)
file.close()

count = 1

with open("lorenzmlwpzgxq736jzseuterytjueszsvznuibanxomlpkyxk6ksoyd.txt") as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    names = soup.find_all("h3")
    companies = []
    for x in names:
        if (x.text)!= "Lorenz":
            companies.append(x.text)
    companies.pop()

    dates = []
    date = soup.find_all("h5")
    for i in date:
        if "Posted" in i.text:
            dates.append(i.text)
    for i in range (42):
        if "2021" in dates[i] or "2020" in dates[i]:
            dates[i] = ""
            companies[i] = ""
        if "Keicorp(ICPM)" in companies[i]:
            dates[i] = ""
            companies[i] = ""            
    companies= [value for value in companies if value != '']
    dates = [value for value in dates if value != '']

    for i in range(len(dates)):
        dates[i] = dates[i].lstrip("Posted ")
        dates[i] = dates[i].rstrip(".")
        dates[i] = dates[i].replace(",","")
        dates[i] = datetime.strptime(dates[i], '%b %d %Y')
        dates[i] = dates[i].strftime("%Y-%m-%d")

    industry = ['Manufacturer','Manufacturer','Motor/Vehicular','Manufacturer','Utility','Manufacturer','Utility','DrinkManufacturer','Finance',
    'Technology','Manufacturer','Manufacturer','NonProfitOrganisation','Manufacturer','Manufacturer','Manufacturer','ConsultingServices',
    'Motor/Vehicular','Finance','Legal','Technology','Technology']
    latitude = [42.54161918889784, 44.880724575935645, 43.07448158655449, 19.520091662457197, 32.987921278484485, 41.4182676703754, 
    46.53912371891505, 43.19024254585053, 41.15376728681359, 44.89705747909835, 42.21310377184401, 33.757363220558865, 
    31.220936681601646, 42.60380001255043, 35.65240082352616, 41.294252012976756, 47.53952136703897, 41.66456950016151, 
    41.23152997571209, 53.79544490567843, 36.04113335539345, 48.04744357921632]
    longitude = [ -71.61386704423393, -93.15876034762489, -88.47594948816479, -99.20768860247206, -83.848949188697, -82.00286843077973, 
    -87.4188581017728, -88.74828597304938, -111.93642903264526, -93.44162320182917, -87.9502949154079, -118.09049317333026,
    121.47803999776778, -88.43114991713333, 139.7474205514249, -92.64742044633074, -122.02226752924953, -93.59506322459227, 
    -96.19024468867458, -1.554440086159583, -115.02870167326768, 11.657465398280277]
    locations = ['155 Jackson Rd, Devens, MA 01434, USA', '1355 Mendota Heights Rd STE 100, Mendota Heights, MN 55120, United States', '1830 Executive Dr, Oconomowoc, WI 53066, USA',
    'Av Presidente Juárez 225, San Jerónimo Tepetlacalco, 54090 Tlalnepantla de Baz, Méx., Mexico', '1135 Rumble Rd, Forsyth, GA 31029, USA',
    '34655 Mills Rd, North Ridgeville, OH 44039, United States', '1002 Harbor Hills Dr, Marquette, MI 49855, United States', '860 West St, Watertown, WI 53094, United States',
    '6026 Fashion Point Dr, Ogden, UT 84403, United States', '12701 Whitewater Dr, Minnetonka, MN 55343, USA', '171 Corporate Woods Pkwy, Vernon Hills, IL 60061, United States',
    '1710 Apollo Ct, Seal Beach, CA 90740, USA', 'China, Shang Hai Shi, Huangpu, 168, Hubin Rd, 168号26-27层无极限大厦 邮政编码: 200021',
    '1225 Sage St, Lake Geneva, WI 53147, United States', 'MP2W+XX Minato City, Tokyo, Japan', '100 1st Ave W, Oskaloosa, IA 52577, USA',
    '904 7th Ave NE, Issaquah, WA 98029, USA', '1572 NE 58th Ave, Des Moines, IA 50313, United States', '17605 Wright St, Omaha, NE 68130, USA',
    '5 Wellington Pl, Leeds LS1 4AP, UK', '198 N Gibson Rd, Henderson, NV 89014, USA','Willy-Messerschmitt-Straße 3, 82024 Taufkirchen, Germany']

    leaksize = ['-','-','-',600000,'-','-','-',250000,'-','-','-',150000,'-',300000,250000,220000,'-',150000,'-',180000,220000,200000]

    for i in range(len(companies)):
        file = open('Lorenz.csv', 'a', newline='', encoding='utf-8')
        writer = csv.writer(file)
        rows = ([i+1,companies[i],dates[i],"Lorenz",industry[i],latitude[i],longitude[i],locations[i],leaksize[i],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        writer.writerow(rows)
        file.close()
