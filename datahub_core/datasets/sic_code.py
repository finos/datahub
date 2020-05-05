class SicCode:
    """

    SicCode data class. Represents a specific industry within an
    Industry Sector.. For example, Commercial Bank within the Finance
    Sector

    # Attributes:
        {
            code: int
            name: str
        }
    """
    code: int
    name: str

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name
        }
