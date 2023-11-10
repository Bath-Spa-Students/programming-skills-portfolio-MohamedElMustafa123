#defines a function called facotiral that takes one parameter, num
def factorial(num):
    #checks if num is equal to 0, if it is 0 it returns 1 because factorial of 0 is 1
    if num == 0:
        return 1
    else:
        #if num is not 0, it calculates the factorial by multiplying num with the factorial of num-1
        return num * factorial(num - 1)
    
print(factorial(10))