class DeliveryPackage:
    id = 0
    address = ''
    city = ''
    state = ''
    zip = ''
    delivery = ''
    size = ''
    note = ''
    weight = 0
    status = ''

    def __init__(self,id,address,city,state,zip,delivery,size,note) -> None:
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.delivery = delivery
        self.size = size
        self.note = note
        