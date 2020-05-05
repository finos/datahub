class SicRange:
    """
    SicRange data entity - represents an overall industry sector
    for which there is a range of sub sectors (SicCode's)

    # Attributes:
        {
            start: int
            end: int
            name: str
        }
    """
    start: int
    end: int
    name: str

    def __init__(self, start, end, name):
        self.start = start
        self.end = end
        self.name = name

    def to_dict(self):
        return {
            "start": self.start,
            "end": self.end,
            "name": self.name
        }
