
print ("\n*****Program to Check Whether The Given Text Is Spam Or Not*****\n")

# Taking Input From User 
text = input("Enter The comment : ")
isSpam = False


if("buy now" in text):
    isSpam = True
elif("make a lot of money" in text):
    isSpam = True
elif("subscribe this" in text):
    isSpam = True
elif("click this" in text):
    isSpam = True

if(isSpam == True):
    print("\n*****This Is An Spam comment !!!*****")
else:
    print("\n*****This Is Not An Spam comment*****")