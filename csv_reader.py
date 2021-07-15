import csv

with open('./data/WGUPSPackageFileSheet.csv') as file:
    table_data = list(csv.reader(file, delimiter=',')) 
    
def print_table():
    print(table_data)


