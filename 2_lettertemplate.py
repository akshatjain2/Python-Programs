# Write a program to fill in a letter template given below with name and date: 
# letter = ''' Dear <|Name|>  You are selected  <|Date|> '''

Name = input("Enter your Name: ")
Date = input("Enter Date: ")
print("''' Dear " + Name + "\n You are selected" + "\n" + Date + "'''") 


# Output: Enter your Name: Akshat Jain
#         Enter Date: 11-10-2021
#         ''' Dear Akshat Jain
#             You are selected
#             11-10-2021'''