from system_admin import system_admin
from system_company import system_company
from system_jobseeker import system_jobseeker

def login():
    print("--- Login to your account ---")
    input_name = input("Enter your username: ")
    input_password = input("Enter your password: ")
    print()
    
    file = open("users.txt", "r")
    
    for line in file.readlines():
        line = line.strip()
        name, password, role = line.split(",")
        name = name.strip()
        password = password.strip()
        role = role.strip()
    
        if input_name == name and input_password == password:
            print(f"Welcome {name}! You are logged in as {role}.")

            if role == "admin":
                system_admin()
            elif role == "companyuser":
                system_company()
            elif role == "jobseeker":
                system_jobseeker(name=input_name)
            else:
                print("Invalid role. Please contact support.")
            break
        else:
            print("Invalid username or password. Please try again.")
    
    file.close()

# login()