my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Insert an element at the second position
my_list.insert(1,15)

#Extend the list with another list
my_list.extend([50,60,70])

#Remove the last element from the list
my_list.pop()

#Sort the list in ascending order
my_list.sort()

#Find the index of the value 30
index = my_list.index(30)

print(index)