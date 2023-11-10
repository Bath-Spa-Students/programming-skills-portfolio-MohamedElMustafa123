dict1 = {'Name': 'Mohamed', 'Age': 19, 'Hobby': 'Skating'}
dict2 = {'Uni': 'BSU', 'fav movie': 'Across the spider-verse'}
#creating a variable to store the new list. 
#using dictionary unpacking we merge the two dictionaries
merged_dict = {**dict1, **dict2}
print(merged_dict)