#This file aims to validate the security of a user inputted password. 
#Since I am using an open source license, I will let people contribute by adding to popular passwords that they can think of.

#//* 
#User input needed, input your password and run the program to test the
#password's security.
#*//*
def checkPassword(password):
    
    hasDigit = False
    hasCapital = False
    hasSpecial = False
    hasPopularPhrase = False
    popularPhrases = ["Password1!", "123456789L!", "qwerty123!", "abcde123!", "Password123!"]


    if password in popularPhrases:
        hasPopularPhrase = True

    
    for character in password:
        if character.isdigit():
            hasDigit = True
        elif character.isupper():
            hasCapital = True
        elif not character.isalnum():
            hasSpecial = True



    if len(password) < 8 or not hasDigit or not hasCapital or not hasSpecial or hasPopularPhrase: 
        print("Password is not secure. Try again!")
    else:
        print("Password is secure")

# Simple tests to confirm the program works correctly.

# Test 1 #Expect not secure, common password.
password1 = "Password1!"
checkPassword(password1)

# Test 2 #Expect secure
password2 = "SecurePass123!"
checkPassword(password2)

# Test 3 #Expect not secure, too short
password3 = "Pass1!"
checkPassword(password3)

# Test 4 #Expect not secure, missing digit
password4 = "Password!"
checkPassword(password4)

# Test 5 #Expect not secure, missing special character
password5 = "Password1232313"
checkPassword(password5)