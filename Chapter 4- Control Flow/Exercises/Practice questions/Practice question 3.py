amount1 = 500
amount2 = 99
#checks if amount1 is greater than 10 and if amount 2 is less than 100
if amount1 > 10 and amount2 < 100:
    #checks if amount1 is greater than amount2
    if amount1 > amount2:
        #displays amount1 if it is greater than amount2
        print("amount 1:", amount1)
    else:
        #displays amount2 if amount2 is greater than amount1
        print("amount 2:" , amount2)
else:
    print("Condtions not met")