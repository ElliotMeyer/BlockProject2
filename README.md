# BlockProject2
This project aims to validate the security of passwords inputted by the user. 

This file aims to check that a password is acceptable given common password criteria. 
The main password criteria are that the password must be longer than 8 characters, the password must have a capital letter, a number, and a special character. 
Additionally, the password cannot contain any popular, easy-to-guess password. Since I am using the Apache, open source license, People will be able to add any popular passwords that are a security risk. 

My reasoning for choosing an Apache license is because I am not the most adept developer and I am not a security expert. By making this program open source, other people will be able to improve on my initial
contributions to this project to make an improve product for everybody. My biggest goal is to make a tool that is the most functional for protecting people in terms of password security. I do not want to make it proprietary because I want to contribute something for "the greater good". 

How to run it: The user only needs to input their "password candidate" as a parameter into the passwordValidator function. After running, the user will get a response of whether their password was secure or not. 

Limitations: I understand that inputting sensitive information, like a password, can be very dangerous for many people. This program does not send any data to a database, it only runs locally. Additionally, it is only used for educational use and may need improvements in order for it to be fully functional in an open source setting. 

As mentioned in the limitations section, there is a risk that a malicious editor could manipulate the program to see what a user's password is. Luckily, we do not take an email or any other personal information, so it would be difficult to connect the password to the person.
Additionally, since the program uses the Apache license, people could use the baseline of this code in order to make a malicious product. Although, the code is not complex and could be created by any novice developer. 
