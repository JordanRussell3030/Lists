unsorted_list = ["c", "t", "u", "a", "z", "h"]

def bubble_sort(unsorted_list):
    no_swaps = False
    while no_swaps == False:
        no_swaps = True
        for item in range(len(unsorted_list)- 1):
            if unsorted_list[item] > unsorted_list[item + 1]:
                no_swaps = False
                temp = unsorted_list[item]
                unsorted_list[item] = unsorted_list[item + 1]
                unsorted_list[item + 1] = temp
    print(unsorted_list)
    return unsorted_list

bubble_sort(unsorted_list)

                
