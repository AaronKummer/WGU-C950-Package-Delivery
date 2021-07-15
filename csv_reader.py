from hash_table import HashTable
import csv

with open('./data/WGUPSPackageFileSheet.csv') as file:
    hash_map = HashTable()
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery = row[5]
        size = row[6]
        note = row[7]
        print(row)


