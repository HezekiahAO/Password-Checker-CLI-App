print("Please Before you enter your Password, Ensure to include a symbol, a digit and at least an Upper Case. Thank you")

password = input("Enter your Password:  ")
    # print(type(x))
    # print(len(x))

import string   # This is what allowes me to test for symbols in this code 

special_symbol = string.punctuation   


#def password_checker(password):

has_upper = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(char in special_symbol for char in password) 


if len(password) < 8:
    print("Please enter an 8 digit passeword or more:    ")

elif any(char.isupper() for char in password) == False :
    print("Please include at least an upper Case in your password")                   # This line of the code test if any of the conidtions are met at all


elif any(char.isdigit() for char in password) == False :
    print("Please include at least a digit in your password  ")


elif any(char in special_symbol for char in password) == False :
    print("Please include a Special Character in your password.   Na for security :) ")

else:
    print("Your Password has been Created!  ")
        


# This aspect of code is specifically testing the strength of the password


strengt = sum([has_upper, has_digit, has_symbol])  # coverted the variables to a list and gets there arithmetic sum which i now use to test fro the strength

if strengt >= 3 and len(password) >=8:
    print("Password Strength is Strong   ")

elif strengt == 2 and len(password) >=8:
    print("Password has medium Strength   ")
    
else:
    print("Your Password is Weak   ")   
        
# This aspect of code is specifically testing the strength of the password