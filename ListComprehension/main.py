# main.py

#slide 9 and 10 week06 ppt
names = ["George Washington", "Thomas Jefferson", "John Adams", "John Kennedy", "Herbert Hoover", "Ronald Reagan"]
print(len(names))
print(names[0:2]) # slicing syntax will print 0th and 1st elements
# slide 11 week06 ppt
nameSplit = [(name.upper()).split(" ") for name in names] # uses the space to separate the elements of the list to create sublists/nested lists
# added upper to capitalize, order of operations is important, if added after split it does not work
print(nameSplit)
# slide 12 week06 ppt
# the one line of code on line 8 takes 4ish lines with brute force
finalList = [] # creates an empty list
for name in names:
    # split on the space into a new 2 element list
    newList = name.split(" ")
    # print(name, newList) prints the original element and what it ended with
    # print(newList)
    finalList.append(newList)
print(finalList) # if this is in the loop it will show you each iteration


# create a new list of lists such that last name precedes first name
lastFirst = [name.split(" ") [::-1] for name in names] # the ::-1 means start from end and give that element first
print(lastFirst)

