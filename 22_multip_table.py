print ("\n*****Program to print multiplication table for a given number*****\n")

# Taking Input From User 
Number = int(input("Enter A Number : "))
print("The Multiplication Table For Given Number Is :-\n")
for i in range(1, 11):
    print(f"{Number} X {i} = {Number*i}")