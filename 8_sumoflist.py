# Q. Write a program to sum a list with 4 numbers.

number = []
print("Enter 4 numbers: ")
x=1
for i in range(4):
    number.append(int(input("Number " + str(x) + " =")))
    x=x+1

print("Sum of 4 numbers = ",sum(number))

# Output: Enter 4 numbers: 
#         Number 1 =550
#         Number 2 =240
#         Number 3 =210
#         Number 4 =300
#         Sum of 4 numbers =  1200