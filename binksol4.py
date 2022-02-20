import csv
import pprint
from datetime import datetime as dt

from pandas.conftest import datetime64_dtype


dict = {}

with open('bink_data.csv', 'r') as f:
    for row in csv.DictReader(f):
        date_col1 = datetime.strptime(row[7], '01-06-2009')

        date_col2 = datetime.strptime(row[9], '31-08-2007')
        
        if datetime64_dtype in range date_col1 and date_col2:
            dict.append()
            print{dict}
        #if  dt <= int(line['Lease Start Date']) <= 25:
         #   pprint.pp(line)
