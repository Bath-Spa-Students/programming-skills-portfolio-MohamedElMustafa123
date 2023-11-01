#creating a dictionary
rivers = {'nile': 'Egypt',
          'Amazon River': 'Brazil',
          'Rio Grande River': 'USA'}
#using for loop to iterate through the dictionary. We use two variables since we are accesing the keys
#and values of the keys by using .item()
print("Sentences:")
for x, y in rivers.items():
    print("The " + x + " flows through " + y)
#printing just the keys using the .keys    
print("\nRivers:")
for i in rivers.keys():
    print(i)
#printing the value of the keys using .values
print("\nCountries:")
for z in rivers.values():
    print(z)