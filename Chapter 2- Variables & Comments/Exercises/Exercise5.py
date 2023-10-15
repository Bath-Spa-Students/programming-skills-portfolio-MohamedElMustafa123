usb = 6
budget = 50
able_to_buy = round(budget / usb)
#calculates how many USB sticks she can buy and rounds it down
print("She can buy " + str(able_to_buy) + " USB sticks with £50")
change = budget - (able_to_buy * usb)
print("Her change would be £" +str(change))