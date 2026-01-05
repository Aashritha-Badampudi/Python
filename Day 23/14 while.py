crt_pwd="python"
attempts=1
pwd=input("Enter your password: \n")
while pwd!=crt_pwd and attempts<3:
    print("Password incorrect")
    attempts=attempts+1
    pwd=input("Enter your password: \n")
if pwd==crt_pwd:
    print("Login successful!")
else:
     print("Incorrect password and Your attempts are limited")