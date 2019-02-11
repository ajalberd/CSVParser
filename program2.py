import csv
from collections import defaultdict
with open('finalsheet.csv', "r") as sheet:
    data=list(csv.reader(sheet)) #This lets Python interpret the csv data as a 2d array.
print(data)

#This is an example I used for testing. I think it can be deleted.
with open('{0}.txt'.format(data[0][0]),"w") as file: #The filename is row0 col0, aka the first cell.
    file.write(data[0][1])  #The data is the cell next to it (row 0, column 1)

for i in range(len(data)): #This iterates across the range of all the data. See the example for how I did it.
    with open('{0}.txt'.format(data[i][0]), "w") as file:
        file.write(data[i][1])