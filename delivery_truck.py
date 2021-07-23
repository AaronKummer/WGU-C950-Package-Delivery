import datetime


class DeliveryTruck:
    distance_traveled = 0
    packages = []
    priority_packages = []
    current_address_index = 0
    truck_id = 0

    def __init__(self,truck_id) -> None:
        self.packages = []
        self.priority_packages = []
        self.distance_traveled
        self.time_traveled_minutes = 0
        self.truck_id = truck_id