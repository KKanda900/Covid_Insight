import csv
import operator

sample = open('us-states.csv', 'r')

csv1 = csv.reader(sample, delimiter=',')

sort = sorted(csv1, key=operator.itemgetter(1))

with open('NJ_Data.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    for eachline in sort:
        if(eachline[1] == 'New Jersey'):
            csvwriter.writerow(eachline)
