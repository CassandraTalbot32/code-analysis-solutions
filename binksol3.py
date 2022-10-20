import csv
import pprint
import unittest


# 3.create dictionary containing tenant name and count of masts for each tenant, output to console in readable form
# tenant name : count of masts
# how many times does tenant name appear in record
# create empty dict
name_count = {}
# open file parse data
with open('bink_data.csv', 'r') as count:
    csvReader = csv.reader(count, delimiter=",", quotechar='"')

    next(csvReader)
# point to column 6 and request number of instances for each name
    for row in csvReader:
        if row [6] not in name_count:
            name_count[row[6]] = 1 
        else:
            name_count[row[6]] += 1
pprint.pp(name_count)

if __name__ == '__main__':
    unittest.main()

