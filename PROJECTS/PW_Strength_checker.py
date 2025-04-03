#what needs to be fixed further 1. try to display the final message if the pw is stronger and vice versa

#Variables for later
numeric = False
length = False


#get the password from the user
pw = input("Enter your password: ")

#logic to check the password for various parameters
#check the total characters of the password
if len(pw) >= 12:
    print("Password length is good")
    length = True
else:
    print("Password length under 12 chars")
    
#Check for upper case
if pw != pw.lower():
    print("Password has atleast one char in upper case")
else:
    print("No upper case character")
    
#Check for lower case
if pw != pw.upper():
    print("Password has atleast one char in lower case")
    
#Check for numeric
for i in pw:
    if i in [0-9]:
        numeric = True

if numeric:
    print("Password has atleast one numeric character")
else:
    print("Password has no numeric character")
    
#Check for special character
for i in pw:
    if i in ["~","@"]:
        special = True

if special:
    print("Password has atleast one special character")
else:
    print("Password has no special character")
    
if length:
    print("You got a stronger password")
