class DeliveryTruck:
    distance = 0
    packages = []
    priority_packages = []
    current_address_index = 0

    def __init__(self) -> None:
        self.packages = []
        self.priority_packages = []
        self.at_home = True