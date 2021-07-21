import csv
from hash_table import HashTable
from delivery_package import DeliveryPackage
from delivery_truck import DeliveryTruck

class PackageDeliveryService: 
    truck_speed = 18/60
    package_data = HashTable()
    priority_packages = []  #these packages have to be delievered at a special time
    grouped_packages = []   #these packages have to be delivered with another package
    truck_one = DeliveryTruck()
    truck_two = DeliveryTruck()
    truck_three = DeliveryTruck()

    def __init__(self) -> None:
        self.addresses = list(csv.reader(open('data/addresses.csv'), delimiter=','))
        self.distances = list(csv.reader(open('data/distances.csv'), delimiter=','))
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

    # O(n)
    def get_column(self,matrix, i):
        return [row[i] for row in matrix]

    def get_package_distance(self,package:DeliveryPackage, truck: DeliveryTruck) -> float:
        # print("getting distance for ", package.address)
        address_id = 0
        for address in self.addresses:
            if (address[2] == package.address):
                address_id = address[0]

        # This column will have distance information for the current address the truck is at
        distance_column = self.get_column(self.distances, truck.current_address_index) 
        return distance_column[int(address_id)]
        # [0] will be the current location's distance from itself which is 0
        # next_closest_distance = sorted(distance_column)[1]
        # next_closest_address_index = distance_column.index(next_closest_distance)

    def find_next_package_to_deliver(self,truck: DeliveryTruck):
        print("finding next package")
        distances_of_packages_on_truck = []
        for package_index in truck.packages: 
            distance = self.get_package_distance(DeliveryPackage(package_index, *self.package_data.get(package_index)), truck)
            distances_of_packages_on_truck.append(distance)
        print(distances_of_packages_on_truck)
        

    def deliver_package(self,truck,package):
        print("delivering package")

    # Entrance to main delivery alrogrithm. Loops through packages for each truck and finds the next closest delivery
    def begin_deliveries(self, truck: DeliveryTruck) :
        next_package = self.find_next_package_to_deliver(truck)
            





    

# X = PackageDeliveryService()

# print(X.package_data.map)
# p = X.package_data.get(15)
# print(p)
# p = DeliveryPackage(i,*X.package_data.get(i))





    
    
        





