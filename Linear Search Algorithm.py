#9/1/15
#Linear Search Algorithmn

def linear_search(search_list, search_item):
    found = False
    count = 0
    while found == False and count < len(search_list):
        if search_list[count] == search_item:
            print("Found")
            found = True
            return found
        else:
            print("Not found")
        count = count + 1


search_list = ["item_1", "item_2", "item_3", "item_4", "item_5", "item_6"]

search_item = input("Which item are you searching for? ")

linear_search(search_list, search_item)
