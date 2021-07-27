import csv
from hash_table import HashTable
from delivery_package import DeliveryPackage
from delivery_truck import DeliveryTruck
from datetime import date,datetime,time,timedelta

class PackageDeliveryService: 
    truck_speed = 18 #mph
    package_data = HashTable()

    # trucks 1 and 2 should be able to start their deliveries at 8 am
    # truck 3 has late packages, so it will start a bit later
    truck_one = DeliveryTruck(1,8)
    truck_two = DeliveryTruck(2,8)
    truck_three = DeliveryTruck(3,10)
    total_miles_for_all_trucks = 0
    total_packages_delivered = 0
    packages_delivered = []

    def __init__(self) -> None:
        self.addresses = list(csv.reader(open('data/addresses.csv'), delimiter=','))
        self.distances = list(csv.reader(open('data/distances.csv'), delimiter=','))

        self.get_package_data()
        self.load_trucks()
        self.begin_deliveries(self.truck_one)
        self.begin_deliveries(self.truck_two)
        self.begin_deliveries(self.truck_three)
        print(self.total_packages_delivered, " deliveries were made in ", self.total_miles_for_all_trucks, "miles")
        # print(sorted(self.packages_delivered))

    # reads package data from csv and stores in a simple hash table
    def get_package_data(self) -> None:
        self.packages = list(csv.reader(open('./data/packages.csv'), delimiter=','))
        for package in self.packages:
            self.package_data.insert(int(package[0]),(package[1],package[2],package[3],package[4],package[5],package[6],package[7],[]))
   
    # arranges data based on the notes and grouped packages from the csv and places package ids into trucks
    def load_trucks(self) -> None:
        # manually loading the trucks makes this program not very scalable.. 
        self.truck_one.packages = [14,16,1,2,4,7,13,15,19,27,29,31,33,34,35,39]
        self.truck_two.packages = [3,18,38,36,10,11,12,17,20,21,22,23,26]

        # truck three has all the problematic deliveries, packages that are not at the hub in the morning etc
        self.truck_three.packages = [6,25,28,32,9,8,5,24,30,37,40]

    # O(n)
    def get_column(self,matrix, i):
        return [row[i] for row in matrix]

    def get_package_distance(self,package:DeliveryPackage, truck: DeliveryTruck) -> float:
        address_id = 0
        distance = 0
        for address in self.addresses:
            if (address[2] == package.address):
                address_id = int(address[0])
                break
        distance_column = self.get_column(self.distances, truck.current_address_index)
        distance = distance_column[int(address_id)]
        return (distance,address_id)

    # O(n^3)
    def find_next_package_and_deliver(self,truck: DeliveryTruck):
        distances_of_packages_on_truck = []
        for package_id in truck.packages: 
            package = DeliveryPackage(package_id, *self.package_data.get(package_id))
            distance_result = self.get_package_distance(package, truck)
            distance = distance_result[0]
            address_id = distance_result[1]
            distances_of_packages_on_truck.append((package.id,distance,package.delivery_time,address_id))
        if (len(distances_of_packages_on_truck) > 0):
            package = min(distances_of_packages_on_truck,key=lambda x:x[1])
            print("minimum distance is", package)
            self.deliver_package(truck, package)
        return

    # O(n)
    def set_package_status(self,minutes_traveled,package_id,status):
        package = self.package_data.get(package_id)
        package[7].append((minutes_traveled, status))
        self.package_data.update(package_id,package)

    def deliver_package(self,truck:DeliveryTruck, package):
        self.set_package_status(truck.time_traveled_minutes, package[0], "in transit")
        truck.distance_traveled += float(package[1])
        truck.current_address_index = package[3]
        self.total_miles_for_all_trucks += float(package[1])
        hours_decimal_traveled = truck.distance_traveled / self.truck_speed
        truck.time_traveled_minutes += (hours_decimal_traveled*60) % 60 # convert hour decimal to minutes
        truck.time.__add__(timedelta(minutes=truck.time_traveled_minutes))
        self.total_packages_delivered += 1 
        # print("delivering package ID", package[0], "took ",(hours_decimal_traveled*60) % 60, " minutes")
        # print("truck", truck.truck_id, " has traveled: ", truck.distance_traveled, "miles so far")
        truck.packages.remove(package[0])
        self.packages_delivered.append(package[0])
        self.set_package_status(truck.time_traveled_minutes, package[0], "delivered")
        self.find_next_package_and_deliver(truck)

    # Entrance to main delivery alrogrithm. Loops through packages for each truck and finds the next closest delivery
    def begin_deliveries(self, truck: DeliveryTruck) :
        self.find_next_package_and_deliver(truck)

    def get_package_status_at_time(self,package_id,time) -> DeliveryPackage :
        print("Getting transit information for package: ", package_id)
        package = DeliveryPackage(package_id, *self.package_data.get(package_id))
        print(package.transits)
        return package

    def get_all_package_status_at_time(self,time):
        return self.package_data




    
    
        





