#Store the locations in a list. Make sure the list is not in alphabetical order.
places = ["Tokyo", "Bahamas", "Australlia", "Canada", "Paris"]

#Print your list in its original order. Don’t worry about printing the list neatly,
#just print it as a raw Python list.
print("Original order: ", places)

#Use sorted() to print your list in alphabetical order without modifying the actual list.
sorted_places = sorted(places)
print("List in Alphabetical order using sorted(): ", sorted_places)

# Show that your list is still in its original order by printing it.
print("Original order: ", places)

#Use sorted() to print your list in reverse alphabetical order without changing the order of 
#the original list.
reverse_list = sorted(places, reverse = True)
print("Reverse alphabetical order using sorted(): ", reverse_list)

#Show that your list is still in its original order by printing it again.
print("Original order: ", places)

#Use reverse() to change the order of your list. Print the list to show that its order has changed.
places.reverse()
print("Reversed order using reverse(): " , places)

#Use reverse() to change the order of your list again. Print the list to show it’s back to its 
#original order.
places.reverse()
print("Original order using reverse(): ", places)

#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that
#its order has been changed.
places.sort()
print("Alphabetical order using sort(): ", places)

#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to 
#show that its order has changed.
places.sort(reverse=True)
print("Reverse alphabetical order using sort(): ", places)

