# dictonary in python

dict_of_cloud_services = {

    1 : "aws",
    2 : "google",
    3 : "oracle",
    4 : "azure"
}
print(dict_of_cloud_services)
print(dict_of_cloud_services[4]) #It will display keyerror if not present. 
print(dict_of_cloud_services.get(4, "not found")) # It will not display keyerror insted it will display not found.

# To update dictonary
dict_of_cloud_services.update({5 : "devops"})
print(dict_of_cloud_services)