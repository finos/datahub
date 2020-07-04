
class LEI:
    """
    LEI Datatype, Legal Identifier is made up of a LOU code and
    an ID appended together

    # Attributes:

        {
            lou_code: str
            lou_id: str
        }

    """

    lou_code: str
    lou_id: str

    def __init__(self, lou_code, lou_id):
        self.lou_code = lou_code
        self.lou_id = lou_id

    def get(self):
        """ Get the LEI code """
        return str(self.lou_code) \
            + self.lou_id \
            + self.__rs232_checksum()

    def __rs232_checksum(self):
        """
        Create a rs232 checksum
        Internal DO NOT USE
        """
        return "0A"

