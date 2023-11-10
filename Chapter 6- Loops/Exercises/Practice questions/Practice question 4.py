#creating list
nums = [1, 2, 4, 6, 8, 10, 11, 17]
#using variable and inserting a value to find in list
get_num = 10
#using for loop to find the first occurrence  of value stored in get_num
for num in nums:
    if num == get_num:
        print(str(get_num) + " is in the list")
        break #breaks loop when number is found

