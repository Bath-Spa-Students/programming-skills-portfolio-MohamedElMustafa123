sandwich_orders = ["Pastrami Sandwich", "Chicken sandwich","Pastrami Sandwich",
                   "Beef burger","Pastrami Sandwich",  "Cheese sandwich"]
finished_sandwiches = []

print("The deli has run out of Pastrami")
#removes pastrami sandwich from the list 
while "Pastrami Sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami Sandwich")
#goes through the list and prints each element,
#using append function we add the finished sandwiches to the list 'finished sandwiches'
for sandwich in sandwich_orders:
    print("I made your " + sandwich)
    finished_sandwiches.append(sandwich)
#printing finished_sandwiches to make sure the finished sandwiches are added to the list
print(finished_sandwiches)




