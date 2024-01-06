'''A password generator is a useful tool that generates strong and random passwords 
for users. This project aims to create a password generator application using Python, 
allowing users to specify the length and complexity of the password. 
User Input: Prompt the user to specify the desired length of the password. 
Generate Password: Use a combination of random characters to generate a 
password of the specified length. 
Display the Password: Print the generated password on the screen.'''

length = lower = upper = digit = False

password = input("Enter password ")

if len(password) >= 8:
    length = True

    for i in password:
        if i.islower():
            lower = True
        elif i.isupper():
            upper = True
        elif i.isdigit():
            digit = True

    if length and lower and upper and digit:
        print("Password is valid")
    else:
        print("Password is incorrect")
else:
    print("Password is less than 8 characters")
