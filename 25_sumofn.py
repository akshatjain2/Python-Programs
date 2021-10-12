print ("\n*****Program to print the sum of first n natural numbers using while loop*****\n")

num = int(input("Enter The Number : "))
sumn = 0
i = 0
while range(i, num+1):
    sumn = sumn + i
    i = i + 1
print(f"\nThe Sum of First {num} Number Is : ",sumn)