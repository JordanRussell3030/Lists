#Lists R+R Task 1

def output_names():
    count = 0
    list_of_names = ["James", "Alice", "Sarah", "Ahmed", "Richard", "Hoi", "Fraser", "Claire"]
    for each in list_of_names:
        count = count + 1
        print("{0}. {1}".format(count, each))
    print("0. Exit program")

def select_student(list_of_names):
    list_of_names = ["James", "Alice", "Sarah", "Ahmed", "Richard", "Hoi", "Fraser", "Claire"]
    student = input("Which students name would you like to change? ")
    if student in list_of_names:
        change = input("Please type your change here: ")
        return student, change
    elif student == "0":
        exit()
    else:
        print("Student not found.")

def output_change(list_of_names, student, change):
    if student == "James":
        count = 0
        list_of_names = ["James", "Alice", "Sarah", "Ahmed", "Richard", "Hoi", "Fraser", "Claire"]
        change = change
        list_of_names.pop(0)
        list_of_names.insert(0, change)
        for each in list_of_names:
            count = count + 1
            print("{0}. {1}".format(count, each))
    elif student == "Alice":
        count = 0
        list_of_names = ["James", "Alice", "Sarah", "Ahmed", "Richard", "Hoi", "Fraser", "Claire"]
        change = change
        list_of_names.pop(1)
        list_of_names.insert(1, change)
        for each in list_of_names:
            count = count + 1
            print("{0}. {1}".format(count, each))
    elif student == "Sarah":
        count = 0
        list_of_names = ["James", "Alice", "Sarah", "Ahmed", "Richard", "Hoi", "Fraser", "Claire"]
        change = change
        list_of_names.pop(2)
        list_of_names.insert(2, change)
        for each in list_of_names:
            count = count + 1
            print("{0}. {1}".format(count, each))
    elif student == "Ahmed":
        count = 0
        list_of_names = ["James", "Alice", "Sarah", "Ahmed", "Richard", "Hoi", "Fraser", "Claire"]
        change = change
        list_of_names.pop(3)
        list_of_names.insert(3, change)
        for each in list_of_names:
            count = count + 1
            print("{0}. {1}".format(count, each))
    elif student == "Richard":
        count = 0
        list_of_names = ["James", "Alice", "Sarah", "Ahmed", "Richard", "Hoi", "Fraser", "Claire"]
        change = change
        list_of_names.pop(4)
        list_of_names.insert(4, change)
        for each in list_of_names:
            count = count + 1
            print("{0}. {1}".format(count, each))
    elif student == "Hoi":
        count = 0
        list_of_names = ["James", "Alice", "Sarah", "Ahmed", "Richard", "Hoi", "Fraser", "Claire"]
        change = change
        list_of_names.pop(5)
        list_of_names.insert(5, change)
        for each in list_of_names:
            count = count + 1
            print("{0}. {1}".format(count, each))
    elif student == "Fraser":
        count = 0
        list_of_names = ["James", "Alice", "Sarah", "Ahmed", "Richard", "Hoi", "Fraser", "Claire"]
        change = change
        list_of_names.pop(6)
        list_of_names.insert(6, change)
        for each in list_of_names:
            count = count + 1
            print("{0}. {1}".format(count, each))
    elif student == "Claire":
        count = 0
        list_of_names = ["James", "Alice", "Sarah", "Ahmed", "Richard", "Hoi", "Fraser", "Claire"]
        change = change
        list_of_names.pop(7)
        list_of_names.insert(7, change)
        for each in list_of_names:
            count = count + 1
            print("{0}. {1}".format(count, each))
    
list_of_names = output_names()
student, change = select_student(list_of_names)
output_change(list_of_names, student, change)
        
