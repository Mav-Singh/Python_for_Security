#to improve: display what could be improved when the pw is Moderate, weak and doesnt met the pw requirenent
#ask user of password best practise
#also add option to create system generated password


#import modules
import string

question = input("Do you want to know what is strong password looks like? y/n: ").lower()
if question == 'y':
    print("Strong password is atleast 12 characters, with atleast 1 upper, 1 lower, 1 special character and 1 numeric value \n")
else:
    print("\nproceeding further. Loading.....\n")

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
special = any(char in string.punctuation for char in pw) # These chars are included !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""


#check length
pw_len = len(pw)

#logic to find the password strength
if upper and lower and special and digit and pw_len >= 12:
    print("Strong Password")
elif upper and lower and special and digit and 8< pw_len < 12:
    print("Moderate Password")
elif upper and lower and special and digit and 4< pw_len <= 8:
    print("Weak Password")
else:
    print("\nPassword didnt meet the requirments")

#display why passord is weak, moderate or stronger
if len(pw) < 12 and upper and lower and special and digit:
    print("tip: make your password lengthier(at least 12 chars)")
else:
    print("\nYour password must have \n1. One Char in upper \n2. Atleast one char in lower \n3. Atleast one special char \n4. Atleast one digit \n5. Atleast 8 characters")
