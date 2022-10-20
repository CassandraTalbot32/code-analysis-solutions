import csv
import pprint
import unittest

# 2.a.open file, parse data and extract those rows with a value of 25 lease years
with open('bink_data.csv', 'r') as f:
    for line in csv.DictReader(f):
        if 25 <= int(line['Lease Years']) <= 25:
            pprint.pp(line)

# 2.b. multiply column 1 by column 2 as separate rows try 1 unsuccessful
    if 25 <= int(line['Lease Years'])*float(line['Current Rent']) <= 25:
        pprint.pp(newline)
# Try 2 unsuccessful
def total_rent():
    for line in lines:
        if 25 <= int(line['Lease Years']) and float(line['Current Rent']):
            print(['Lease Years']*['Current Rent'])
          

if __name__ == '__main__':
    unittest.main()
