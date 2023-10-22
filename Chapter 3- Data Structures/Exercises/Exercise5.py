inv = ["Brownlee", "Stanlee", "Felix K"]
#print messages stating that the guest wont be able to make it
print(inv[2] + " Will not be able to make it to dinner")

#replacing the guest "Felix K" with "Postmalone"
inv[2] = "Postmalone"
index = 0
count = 0
#If you add more names, increase the conditional statement by however many names you added
#prints the invitations 
while count <3:
    print("Hello " + inv[index] + "! I would like to invite you for dinner")
    index = index + 1
    count = count + 1
