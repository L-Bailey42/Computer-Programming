#Task 1
name = input("Enter your name: ")
if name:
    print("Hello,",name)
else:
    print("Hello, Stranger!")


#Task 2
password = input("\nEnter a new password: ")
password_check = input("Confirm password: ")
if password == password_check:
    print("Password Set")
else:
    print("Passwords Don't Match")


#Task 3
password = input("\nEnter a new password: ")
password_check = input("Confirm password: ")
if password == password_check and 8 <= len(password) <= 12:
    print("Password Set")
else:
    print("Passwords Don't Match")


#Task 4
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
password = input("\nEnter a new password: ")
password_check = input("Confirm password: ")
if password == password_check and 8 <= len(password) <= 12 and (password in BAD_PASSWORDS == False):
    print("Password Set")
else:
    print("Invalid Password")


#Task 5
pass_ = False
BAD_PASSWORDS = ['password','letmein','sesame','hello','justinbieber']
while pass_ == False:
    password = input("\nEnter a new password: ")
    password_check = input("Confirm password: ")
    if password == password_check and 8 <= len(password) <= 12 and (password in BAD_PASSWORDS) == False:
        print("Password Set")
        pass_ = True
    else:
        print("Invalid Password")
        pass_ = False


#Task 6
for count in range (0,13)
    print(count,"x 7 =",(count*7))


#Task 7
num = int(input("Enter a number (1-12): "))
if 1 <= num <= 12:
    for count in range (0,13)
        print(count,"x",num,"=",(count*7))
else:
    print("Number not in range")


#Task 8
num = int(input("Enter a number (1-12): "))
if 1 <= num <= 12:
    for count in range (0,13):
        print(count,"x",num,"=",(count*num))
elif -12 <= num <= -1:
    for count in reversed(range (0,13)):
        print(count,"x",-num,"=",(count*-num))
else:
    print("Number not in range")
