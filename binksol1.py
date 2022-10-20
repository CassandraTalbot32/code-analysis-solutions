# importing the module
import csv
import pprint
import unittest
# open the file in read mode
filename = open('bink_data.csv', 'r')

# creating dictreader object
file = csv.DictReader(filename)

# create empty list
data = []

# iterate over each row and append values to empty list

for col in file:
	data.append(col['Current Rent'])

# 1.a. sort the list of floats in ascending order and print 
data.sort(key=float)

pprint.pp(data)

# 1.b. print the first 5 items from the resultant list
pprint.pp(data[:5])

if __name__ == '__main__':
    unittest.main()



    
