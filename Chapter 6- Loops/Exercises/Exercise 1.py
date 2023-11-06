#prompts user to enter toppings
#if user inputs quit the loop will break
while True:
    toppings = input("Enter the toppings you would like to add to your pizza: ")
    if toppings == "quit":
        break
    print("I will add " + toppings + " to your pizza")


