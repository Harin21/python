import csv
with open("emp.csv","r") as efile:
    data=csv.reader(efile)
    for i in data:
            print (i)
