pword = input("what is the master password?  ")

def view():
    pass
def add():
    name = input("Account name:  ")
    pwd = input("password:  ")

    with open('passwords.txt', 'a') as f:
                f.write(name + "|" + pwd)
                

while True:
    
    pass
    mode = input("would you like to add a new password or view existing ones?(view,add) or press q to quit  ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
        
    elif mode == "add":
        add()
    else:
        print("invalid input")
        
