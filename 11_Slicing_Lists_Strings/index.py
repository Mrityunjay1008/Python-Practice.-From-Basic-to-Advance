my_list = [0,1,2,3,4,5,6,7,8,9]
#          0  1  2  3  4  5  6  7  8  9
#          -10 -9 -8 -7 -6 -5 -4 -3 -2 -1


# Slicing
# my_list[start:end:step]

print(my_list[0:5]) # print the list till 4 index
print(my_list[:5]) # print the list till 4 index
print(my_list[5:]) # print the list from 5 index till the end
print(my_list[:]) # print the whole list
print(my_list[-8:9]) # print the list from -8(2) index till 8 index

# step
print(my_list[0:10:4]) # print the list from 0 index to 9 index with step 4
print(my_list[-1:1:-2]) # print the list from 9 index to 0 index with step -1
print(my_list[::-1]) # reverse the list

#Strings

sample_url = "https://sharmadev.com" # Not a real url

print(sample_url[8:]) #This will print domain
print(sample_url[::-1]) #This will reverse the url
print(sample_url.split("//")[1]) #This will print domain