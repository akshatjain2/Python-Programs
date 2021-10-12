print ("\n*****Program to print the sum of first n natural numbers using while loop*****\n")

num = int(input("Enter The Number : "))

for i in  range(num):
    print(" " * (num - i - 1), end = "")
    print("* " * (i+1), end = "")
    print(" " * (num - i - 1))