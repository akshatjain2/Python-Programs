print ("\n*****Program to find out whether a given post is talking about \"Simarjeet\" or not*****\n")

# Taking Input From User 
post = input("Enter Your Post Here : ")
post = post.lower()

if("Simarjeet".lower() in post):
    print("\n***This Post Is Talking About Simarjeet***")
else:
    print("\n***This Post Is Not Talking About Simarjeet***")