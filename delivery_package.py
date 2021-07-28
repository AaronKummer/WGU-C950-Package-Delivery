class DeliveryPackage:
    id = 0
    address = ''
    city = ''
    state = ''
    zip = ''
    delivery_time = ''
    size = ''
    note = ''
    weight = 0
    transits = []
    truck_id = 0

    def __init__(self,id,address,city,state,zip,delivery_time,size,note,transits,truck_id) -> None:
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery_time = delivery_time
        self.size = size
        self.note = note
        self.transits = transits
        self.truck_id = truck_id
        