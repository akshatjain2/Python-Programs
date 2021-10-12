# Q. Write a program to find out whether a given name is present in a list or not.


Names = ["Akshat","Rohit","Aditya","Kunal","Manu","Jay"]
X = input("Enter Name to search: ")

if(X in Names):
    print("Name is Present...")
    exit
else:
    print("Name is not Present...")

# Output :    Enter Name to search: Gaurav
#             Name is not Present...

#             Enter Name to search: Manu
#             Name is Present...