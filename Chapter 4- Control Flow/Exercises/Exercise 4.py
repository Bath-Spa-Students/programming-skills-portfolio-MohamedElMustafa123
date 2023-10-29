age = 19
if age >= 1 and age <= 120:
    if age < 2:
        print("Person is a baby")
    elif age >= 2 and age < 4:
        print("Person is a toddler")
    elif age >= 4 and age < 13:
        print("Person is a kid")
    elif age >= 13 and age < 20:
        print("Person is a teenager")
    elif age >= 20 and age < 65:
        print("Person is an adult")
    else:
        print("Person is an elder")
else:
    print("Enter a valid age (Range from 1 to 120)")