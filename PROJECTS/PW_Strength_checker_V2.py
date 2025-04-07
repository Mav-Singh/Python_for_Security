#to improve: display what could be improved when the pw is Moderate, weak and doesnt met the pw requirenent
#also add option to create system generated password


#import modules
import string

#get the password input from the user
pw = input("Enter your password: ")

#logic to check the password for various parameters
#check upper case
upper = any(char.isupper() for char in pw) 

#check for lowercase
lower = any(char.islower() for char in pw)

#check for digit
digit = any(char.isdigit() for char in pw)

#check special character
special = any(char in string.punctuation for char in pw)

#check length
pw_len = len(pw)

#logic to find the password strength
if upper and lower and special and digit and pw_len >= 12:
    print("Strong Password")
elif upper and lower and special and digit and 8< pw_len < 12:
    print("Moderate Password")
elif upper and lower and special and digit and 4< pw_len < 8:
    print("Weak Password")
else:
    print("Password didnt meet the requirments")

#display why passord is weak, moderate or stronger
