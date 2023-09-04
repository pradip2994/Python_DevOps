"""
Python packages
A package is a collection of modules.

Python modules
A module is a file containing Python definitions and statements.


"""
import os

# Shows Present Working Directory
print(os.getcwd())

# Disk usage

import shutil

print(shutil.disk_usage("/"))

total, used, free = shutil.disk_usage("/")
print("Total disk space is:", (total // (2**30)),"GB")
print("Used space is:", (used // (2**30)),"GB")
print("Free disk space is:", (free // (2**30)),"GB")

"""
These lines print out the disk usage information in gibibytes (GiB) by dividing the values of total, used, and free by 2^30. 2^30 is used because 1 gibibyte (GiB) is equal to 2^30 bytes. 
The // operator is used for integer division, ensuring that the result is an integer.

"""
