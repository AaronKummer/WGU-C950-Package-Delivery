import csv
from hash_table import HashTable
from delivery_package import DeliveryPackage
from delivery_truck import DeliveryTruck
from datetime import date,datetime,time,timedelta

class PackageDeliveryService: 
    truck_speed = 18 #mph
    truck_3_started = False
    package_data = HashTable()

    # trucks 1 and 2 should be able to start their deliveries at 8 am
    truck_one = DeliveryTruck(1, timedelta(hours=8))
    truck_one.time_traveled_minutes = 480
    truck_two = DeliveryTruck(2, timedelta(hours=8))
    truck_two.time_traveled_minutes = 480
    # truck three's start_delivery time will be determined later after truck 1 or 2 finishes
    truck_three = DeliveryTruck(3, timedelta(hours=11))
    truck_two.time_traveled_minutes = 660

    # truck 3 has late packages, so it will start a bit later
    # truck 3 will have a departure time set when  truck 1 or 2 finishes their routes. 
    # there are only two drivers. Ideally for this scenario that should be after 10:20 due to delays
    
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
        
        print(self.total_packages_delivered, " deliveries were made in ", self.total_miles_for_all_trucks, "miles")
        # print(sorted(self.packages_delivered))

    # reads package data from csv and stores in a simple hash table
    def get_package_data(self) -> None:
        self.packages = list(csv.reader(open('./data/packages.csv'), delimiter=','))
        for package in self.packages:
            self.package_data.insert(int(package[0]), DeliveryPackage(int(package[0]),package[1],package[2],package[3],package[4],package[5],package[6],package[7],[], int(0)))
   
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
    # this is the main 'nearest neighbor' type of algorithm. it is called recursively through deliver_package()
    def find_next_package_and_deliver(self,truck: DeliveryTruck):
        distances_of_packages_on_truck = []
        for package_id in truck.packages: 
            package = self.package_data.get(package_id)
            distance_result = self.get_package_distance(package, truck)
            distance = distance_result[0]
            address_id = distance_result[1]
            distances_of_packages_on_truck.append((package.id,distance,package.delivery_time,address_id))
        if (len(distances_of_packages_on_truck) > 0):
            package = min(distances_of_packages_on_truck,key=lambda x:x[1])
            # print("minimum distance is", package)
            self.deliver_package(truck, package)
        return

    # O(n)
    def set_package_status(self,minutes_traveled,package_id,status, truck_id):
        package:DeliveryPackage = self.package_data.get(package_id)
        package.transits.append((minutes_traveled, status))
        package.truck_id = truck_id
        self.package_data.update(package_id,package)

    # O(n^3)
    def deliver_package(self,truck:DeliveryTruck, package):
        truck.distance_traveled += float(package[1])
        truck.current_address_index = package[3]
        self.total_miles_for_all_trucks += float(package[1])
        hours_decimal_traveled = truck.distance_traveled / self.truck_speed
        truck.time_traveled_minutes += (hours_decimal_traveled*60) % 60 # convert hour decimal to minutes
        self.total_packages_delivered += 1 

        truck.packages.remove(package[0])
        self.packages_delivered.append(package[0])
        self.set_package_status(truck.time_traveled_minutes, package[0], "delivered", truck.truck_id)
        if (len(truck.packages) < 1 and self.truck_3_started == False ):
            self.begin_deliveries_for_truck_3(truck)

        self.find_next_package_and_deliver(truck)

    def begin_deliveries_for_truck_3(self,truck:DeliveryTruck):
        self.truck_3_departure_time = truck.time_traveled_minutes

        # this is reads weird. time_traveled_minutes here is being used as a minutes counter for the day which is
        # passed to truck 3 upon delivery start
        self.truck_three.time_traveled_minutes = truck.time_traveled_minutes
        print('Truck three departs', self.truck_three.time_traveled_minutes, 'minutes into the day')
        self.truck_3_started = True
        self.begin_deliveries(self.truck_three)

    # Entrance to main delivery alrogrithm. Loops through packages for each truck and finds the next closest delivery
    def begin_deliveries(self, truck: DeliveryTruck) :
        self.find_next_package_and_deliver(truck)

    # time calculations O(n^3)
    def get_all_packages_status_at_time(self, time_input):
        packages = []
        # O(n)
        for package_id in range(1,41):
            package: DeliveryPackage = self.package_data.get(package_id)
            packages.append(package)
        # O(n)
        for package in packages:
            self.get_package_status_at_time(package.id, time_input)

    # time calculations O(n)
    def get_package_status_at_time(self,package_id,time) :
        package:DeliveryPackage = self.package_data.get(package_id)
        
        parsed_time_input = self.parse_time_to_minutes(time)
        
        departure_time = 0
        if (package.truck_id == 1):
            departure_time = self.truck_one.departure_time.seconds / 60
        elif (package.truck_id == 2):
            departure_time = self.truck_two.departure_time.seconds / 60
        elif (package.truck_id == 3):
            departure_time = self.truck_three.departure_time.seconds / 60

        if (parsed_time_input < departure_time):
             print("package", package_id, "is still at the hub")
        elif (parsed_time_input > departure_time and parsed_time_input < package.transits[0][0]):
            print("package", package_id, "is in transit at this time")
        else :
            print("package", package_id, "was been delivered at", self.get_formated_delivery_time(package))

    def  get_formated_delivery_time(self,package:DeliveryPackage):
        time_delta = timedelta(minutes=package.transits[0][0])
        return str(time_delta)

    def get_all_package_status_at_time(self,time):
        return self.package_data

    def parse_time_to_minutes(self,time_input):
        time_in_minutes = timedelta()
        parts = time_input.split(':')
        if ('am' in parts[1] and int(parts[0]) != 12):
            time_in_minutes = timedelta(hours=float(parts[0]), minutes=float(parts[1].split(' ')[0]))
        if('pm' in parts[1] and int(parts[0]) != 12):
            time_in_minutes = timedelta(hours=float(parts[0]) + 12, minutes=float(parts[1].split(' ')[0]))
        if('pm' in parts[1] and int(parts[0]) == 12):
            time_in_minutes = timedelta(hours=float(parts[0]), minutes=float(parts[1].split(' ')[0]))
        if('am' in parts[1] and int(parts[0]) == 12):
            time_in_minutes = timedelta(hours=0, minutes=float(parts[1].split(' ')[0]))

        return time_in_minutes.seconds / 60 



    





    
    
        






