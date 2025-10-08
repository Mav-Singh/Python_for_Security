#goal is to make this program handle any complex password or logic and try to make the front end too
#Program to check the strength of the Password, give examples of strong passwords, and generate superstrong passwords

#Password Strength Checker
def password_checker(password):
    issues = []
    #check for password length
    if len(password) < 10:
        issues.append("Password length below 10 characters")

    #check for digit in the password
    if not any(char.isdigit() for char in password):
        issues.append("Add numbers to your password")

    #Check for upper case
    if not any(char.isupper() for char in password):
        issues.append("Add at-least one upper case character")

    #Check for lower case
    if not any(char.islower() for char in password):
        issues.append("Include lower case characters too")

    #Check special character
    if not any(char in "!@#$%^&*()-_=+" for char in password):
        issues.append("Include a special character such as !@#$%^&*()-_=+")

    #loop through the list "issues" and display the list
    for issue in issues:
        print(issue)

    # display password strength if all the conditions are met
    if len(issues) == 0:
        return "Your Password is: Strong"

#take password from the user
user_pass= input("Enter your password: ")

#logic to call the function & print the result
strength = password_checker(user_pass)
print(strength)


#Example Passwords
strong_passwords = []

#Password Generator
