import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os
import sqlalchemy



pageurl='https://events.bli.gov.tw/report//reportM.aspx?m=10704&f=a7010&fbclid=IwAR2yubnAHDUd3pjcVchuUUKYWpVrhLGibqrbvG1VTSqFyDiGUUc8aewO-JQ'


soup = BeautifulSoup(page, 'html.parser')

href_box=soup.find('A',attrs={'href':'attachment_file/Report/month/10704/a7010.csv'})
href=href_box.text.strip()
print (href)

with open('index.csv','a') as csv_file:
    writer=csv.writer(csv_file)
    writer.writerow([href,datetime.now])

