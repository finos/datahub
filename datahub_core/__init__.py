import os
import pkg_resources
from .printable import Printable


# Create temp folder for any processes created logs etc
if not os.path.exists('./.temp/'):
    os.makedirs('./.temp/')


def resource(name):
    return pkg_resources.resource_filename('datahub_core', 'data/' + name)


os.environ["NLTK_DATA"] = resource("nltk")
