uname = "python"
pswd = "rules"

i = 0
while i < 5:
    in_name = input("Enter username: ")
    in_pswd = input("Enter password: ")
    if in_name == uname and in_pswd == pswd:
        print("Welcome!")
        break
    print("Access denied")
    i+=1
