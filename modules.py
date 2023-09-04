# dictionary, module
# Dictionaries are used to store data values in key:value pairs.

dict_of_cloud = {

    1 : "aws",
    2 : "azure",
    3 : "google",
    4 : "oracle"
}
print(dict_of_cloud, "\n")
print(dict_of_cloud.get(2), "\n")
print(dict_of_cloud.get(1), "stands for Amazon Web Services", "\n")


import json

json_file = json.dumps(dict_of_cloud, indent=20)
print(json_file, "\n")

import yaml

yaml_file = yaml.dump(dict_of_cloud)
print(yaml_file, "\n")

## Read file from present directory.
# If you're dealing with untrusted input or want to ensure a higher level of security, use SafeLoader.

with open("data.yaml") as yamal_file:
    yaml_file1 = yaml.load(yamal_file, Loader=yaml.SafeLoader)
    print(yaml_file1, "\n")


with open("data.json") as json_file:
    json_file1 = json.load(json_file)
    print(json_file1, "\n")


# Read yaml file from present directiry and convert to json.

json_file2 = json.dumps(yaml.load(open("data.yaml"), Loader=yaml.SafeLoader), indent=20)
print(json_file2, "\n")


# Read json file from present directiry and convert to yaml.

yaml_file2 = yaml.dump(json.load(open("data.json")))
print(yaml_file2, "\n")