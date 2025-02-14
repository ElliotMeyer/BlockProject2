#This file aims to validate the security of a user inputted password. 
#Since I am using an open source license, I will let people contribute by adding to popular passwords that they can think of.
popularPhrases = ["Password1!", "123456789L!", "qwerty123!", "abcde123!", "Password123!"]

#//* 
#User input needed, input your password and run the program to test the
#password's security
#*//*
password = ""

hasDigit = False
hasCapital = False
hasSpecial = False
hasPopularPhrase = False


if popularPhrases.__contains__(password):
   hasPopularPhrase = True


for character in password:
    if not character.isalpha():
        print("Password is not secure")
        password = ""
        break
    elif character.isdigit():
        hasDigit = True
        break
    elif character.isupper():
        hasCapital = True
        break
    else:
        print("Password is secure")
        break


if len(password) < 8 or not hasDigit or not hasCapital or not hasSpecial or not hasPopularPhrase: 
    print("Password is not secure. Try again!")
    password = ""