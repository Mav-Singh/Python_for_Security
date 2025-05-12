 #Password must include the following:
# Use between 8 and 16 characters
# Include at least one lowercase (a-z) and one uppercase letter (A-Z)
# Include at least one special character(e.g. !@#$&)
# Does not contain blank spaces or the following special characters: < > ,
# Include at least one digit (0-9)
# Passwords match


#Import modules
import random

#Ask user if wants to generate a system generated strong password:
password = []
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
low_alph = [chr(i) for i in range(97, 123)]  # a to z
up_alph = [chr(i) for i in range(65, 91)]    # A to Z
ran = random.choice(low_alph)
print(ran)

#Create own Password and check password strength:
#pw = input("Please enter Your Password: ")

#Keep on telling whats keeping the password weak or moderate
