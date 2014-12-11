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

def output_change(list_of_names,student, change):
    count = 0
    list_of_names = ["James", "Alice", "Sarah", "Ahmed", "Richard", "Hoi", "Fraser", "Claire"]
    change = change
    list_of_names.pop(student)
    list_of_names.insert(student, change)
    for each in list_of_names:
        count = count + 1
        print("{0}. {1}".format(count, each))
    
list_of_names = output_names()
student, change = select_student(list_of_names)
output_change(list_of_names, student, change)
        
