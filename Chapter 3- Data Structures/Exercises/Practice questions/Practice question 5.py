list1 = [5, 10, 15, 20, 25, 50, 20]
#checks if 20 is in list1
if 20 in list1:
    #finds the index of 20 in the list
    index = list1.index(20)
    #replaces it with the value 200
    list1[index] = 200
#displaying list
print(list1)
