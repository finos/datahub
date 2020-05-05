class Address:

    """
    Address DataType

    # Attributes:

        {
            address_1: str
            address_2: str
            city: str
            state: str
            postal_code: str
        }

    """

    address_1: str
    address_2: str
    city: str
    state: str
    postal_code: str

    def __init__(self, address_1, address_2, city, state, postal_code):
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.postal_code = postal_code
