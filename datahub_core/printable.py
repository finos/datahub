from pprint import pformat

class Printable:
    def __repr__(self):

        return "<" + type(self).__name__ + "> " + pformat(vars(self), indent=4, width=1)
