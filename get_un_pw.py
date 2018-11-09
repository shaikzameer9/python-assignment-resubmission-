'''code to get username and password'''



def main():
    login()
    
def login():
    username="zameer"
    password="sonu"
    print("Enter username : ")
    answer1=input()
    print("Enter password : ")
    answer2=input()
    if answer1==username and answer2==password:
        print("Welcome - Access Granted")
    else:
        print("Access Denied")

main()

