inv = ["Brownlee", "Stanlee", "Felix K"]
#print messages stating that the guest wont be able to make it
print(inv[2] + " Will not be able to make it to dinner")

#replacing the guest "Felix K" with "Postmalone"
inv[2] = "Postmalone"

#essage saying that you can invite only two people for dinner.
print("unfortunately I can only invite 2 people because our new dinner table didn't arrive")
#using pop to remove "Brownlee"
print("Sorry " + inv[0] + " I will not be able to accomidate you")
inv.pop(0)
print("List after pop: ", inv)
index = 0
count = 0
#If you add more names, increase the conditional statement by however many names you added
#prints the invitations
while count <2:
    print("Hello " + inv[index] + " dinner is still on!")
    index = index + 1
    count = count + 1
del inv[:]
print(inv)