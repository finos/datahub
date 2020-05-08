import os
from distutils.dir_util import copy_tree

# Simple build script to make pydocmd compatible with docusaurus

def prepend_header(file_name, line):
    dummy_file = file_name + '.bak'
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        data = read_obj.read().splitlines(True)
        write_obj.write(line + '\n')
        # remove the first line
        for line in data[1:]:
            write_obj.write(line)
    os.remove(file_name)
    os.rename(dummy_file, file_name)



for root, dirs, files in os.walk('datahub_core/docs'):
    for file in files:
        path = os.path.join(root, file)
        name = file.split('.')[0]
        line = f'''---
id: {name}
title: {name}
---
'''
        prepend_header(path, line)

copy_tree("datahub_core/docs/", "docs/")
    