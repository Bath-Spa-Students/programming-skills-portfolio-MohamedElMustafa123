month = int(input("Enter the number of month (1-12): "))
#if month inputted is greater than or equal to 3 and is less than 6 it outputs "It's spring" 
if month >= 3 and month < 6:
    print("It's spring")
#if month inputted is greater than or equal to 6 and is less than 9 it outputs "It's summer" 
elif month >= 6 and month < 9:
    print("It's summer")
#if none of these conditions are true then it outputs "It's winter" 
else:
    print("It's winter")