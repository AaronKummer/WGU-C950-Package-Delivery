import csv
from hash_table import HashTable
from delivery_package import DeliveryPackage

class PackageDeliveryService: 
    table = HashTable()
    def __init__(self) -> None:
        with open('./data/WGUPSPackageFileSheet.csv') as file:
            reader = csv.reader(file, delimiter=',') 
            for row in reader:
                self.table.set(int(row[0]),(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

X = PackageDeliveryService()
print(X.table.get(1))
p = DeliveryPackage(*X.table.get(1))
print(p.address)


    
    
        





