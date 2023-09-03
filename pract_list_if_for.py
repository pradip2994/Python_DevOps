### Python lists
# Lists are used to store multiple values in a single variable.

list_of_cloud = [

    "AWS",
    "Google_cloud",
    "azure",
    "oracle"
]
# Add to list
list_of_cloud.append("devops")
print(list_of_cloud, "\n")      # "\n" to create multiline strings or insert line breaks.

# Insert at index
list_of_cloud.insert(0, "cloud_computing")
print(list_of_cloud, "\n")

# Remove from list
list_of_cloud.remove("devops")
print(list_of_cloud, "\n")

# Print particular value from the list.
print(list_of_cloud[2], "\n")

# pop from index
list_of_cloud.pop(0)
print(list_of_cloud, "\n")


## Iteration is the process of repeatedly executing a block of code or 
# processing each item in a sequence (such as a list, tuple, or string) until a specific condition is met. 

# Loop that iterates over a sequence of numbers.

for i in range(5):
    print(i)

# range() function
# range(start, stop, step)
# start: starting number of the sequence
# stop: generate numbers up to, but not including this number
# step: difference between each number in the sequence

for i in range(0,10,2):
    print(i)

## List Iteration

for cloud in list_of_cloud:
    if cloud == "AWS":
        print("AWS is from Amazon web services", "\n")

for cloud in list_of_cloud:
    if cloud == "Google_cloud":
        print("Google cloud is from Google", "\n")

for cloud in list_of_cloud:
    if cloud == "azure":
        print("Azure is from Microsoft", "\n")