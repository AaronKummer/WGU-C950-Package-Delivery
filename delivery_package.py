class DeliveryPackage:
    address = ''
    city = ''
    state = ''
    zip = ''
    delivery = ''
    size = ''
    note = ''

    def __init__(self,address,city,state,zip,delivery,size,note) -> None:
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery = delivery
        self.size = size
        self.note = note
        