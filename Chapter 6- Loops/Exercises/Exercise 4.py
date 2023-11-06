sandwich_orders = ["Chicken sandwich", "Beef burger", "Cheese sandwich"]
finished_sandwiches = []
#goes through the list and prints each element,
#using append function we add the finished sandwiches to the list 'finished sandwiches'
for sandwich in sandwich_orders:
    print("I made your " + sandwich)
    finished_sandwiches.append(sandwich)
#printing finished_sandwiches to make sure the finished sandwiches are added to the list
print(finished_sandwiches)

