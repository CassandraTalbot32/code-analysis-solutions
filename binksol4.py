import csv
import pprint
from datetime import datetime


dates = {}
#open file and parse 
with open('bink_data.csv', 'r') as f:
    for row in csv.DictReader(f):
        #specify date range needed
        if datetime.date('01-06-2009') < datetime.date('31-08-2007'):
            #redo the dictionary and print
            dates.append()
            pprint.pp(dates)

        #if col1 is > 
        #date_col1 = datetime.strptime(row[7], '01-06-2009')

        #date_col2 = datetime.strptime(row[9], '31-08-2007')
        
        #if datetime.date in range date_col1 and date_col2:
         #   dict.append()
          #  print{dict}
        #if  dt <= int(line['Lease Start Date']) <= 25:
         #   pprint.pp(line)
