import csv
from hash_table import HashTable
from delivery_package import DeliveryPackage
from delivery_truck import DeliveryTruck

class PackageDeliveryService: 
    truck_speed = 18/60
    package_data = HashTable()
    packages = []
    truck_one = DeliveryTruck()
    truck_two = DeliveryTruck()
    truck_three = DeliveryTruck()

    def __init__(self) -> None:
        self.get_package_data()
        self.load_trucks()
        self.begin_deliveries(self.truck_one)
        # self.begin_deliveries(self.truck_two)
        # self.begin_deliveries(self.truck_three)

    # reads package data from csv and stores in a simple hash table
    def get_package_data(self) -> None:
        self.packages = list(csv.reader(open('./data/packages.csv'), delimiter=','))
        for package in self.packages:
            self.package_data.insert(int(package[0]),(package[1],package[2],package[3],package[4],package[5],package[6],package[7]))
   
    # arranges data based on the notes and grouped packages from the csv and places package ids into trucks
    def load_trucks(self) -> None:
        self.truck_one.packages = [13,14,15,16,29,30,31,34,37,40,1,4,7,39,8,32]
        self.truck_two.packages = [3,18,36,38,6,10,11,12,17,20,21,22,23,24,25,26]
        self.truck_three.packages = [9,19,27,28,33,35,2,5]
        
        self.truck_one.priority_packages = [13,14,15,16,29,30,31,34,37,40]
        self.truck_two.priority_packages = [6,20,25]
        self.truck_three.priority_packages = []


    # Entrance to main delivery alrogrithm. Loops through packages for each truck and finds the next closest delivery
    def begin_deliveries(self, truck: DeliveryTruck) :
        for package in truck.packages:
            print(package)





    

# X = PackageDeliveryService()

# print(X.package_data.map)
# p = X.package_data.get(15)
# print(p)
# p = DeliveryPackage(i,*X.package_data.get(i))





    
    
        





