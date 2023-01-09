import csv

columns_to_read = [0,2]

with open('csvfile.csv','r') as f:

    clmn_reader = csv.reader(f)

    for row in clmn_reader:

        print([row[i] for i in columns_to_read])