# Q. Write a program to enter marks of 6 students and display them in sorted order

marks = []
print("Enter marks of 6 students: ")
for i in range(6):
    marks.append(input("Enter marks: "))

print("Unsorted list = ")
print(marks)

marks.sort()

print("sorted listss = ")
print(marks)


# Output: Enter marks of 6 students: 
#         Enter marks: 26
#         Enter marks: 89
#         Enter marks: 10
#         Enter marks: 54 
#         Enter marks: 35
#         Enter marks: 78
#         Unsorted list = 
#         ['26', '89', '10', '54', '35', '78']
#         sorted marks = 
#         ['10', '26', '35', '54', '78', '89']