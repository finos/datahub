""" MName """
from .mdict import MDict

class MName:
    """ A name from a Markov chain """
    def __init__(self, names, random_state, chain_len=3):

        # Building the dictionary
        if chain_len > 10 or chain_len < 1:
            print("Chain length must be between 1 and 10, inclusive")

        self.mcd = MDict(random_state)
        self.chain_len = chain_len

        for name in names:
            name = name.strip()

            s = " " * chain_len + name

            for index in range(0, len(name)):
                prefix = s[index:index+chain_len]
                suffix = s[index+chain_len]
                self.mcd.add_key(prefix, suffix)

            self.mcd.add_key(s[len(name):len(name)+chain_len], "\n")

    def make(self):
        """ New name from the Markov chain """
        prefix = " " * self.chain_len
        name = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > 90:
                break

            name = name + suffix
            prefix = prefix[1:] + suffix
        return name.capitalize()
