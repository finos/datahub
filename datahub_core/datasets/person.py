class Person:
    """
    Person data entity, represents an individual

    # Attributes:

        {
            first: str
            last: str
            fullname: str
        }

    """
    first: str
    last: str
    fullname: str

    def __init__(self, first, last, fullname):
        self.first = first
        self.last = last
        self.fullname = fullname

    def to_dict(self):
        return {
            "first": self.first,
            "last": self.last,
            "fullname": self.fullname
        }
