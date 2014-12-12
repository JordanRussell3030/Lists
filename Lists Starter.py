shopping_list = [] #blank list
finished = False 
while not finished: #while the list is not complete
    shopping_item = input("Enter next item (-1 to end list): ")
    if shopping_item == "-1":
        finished = True  # program stops requesting inputs when the user enters -1.
    else:
        shopping_list.append(shopping_item) #add new item to the list #each input is appended to the end of the list.

for index, shopping_item in enumerate(shopping_list):
    print("item {0} is {1}".format(index + 1, shopping_item)) #Prints the item in the list along with its index.
