# from system_company import system_company

def system_admin():
    print("--- Welcome to the Admin Panel ---")
    print("1)View all users\n2)Add new users")
    z = input("Enter option: ")
    if z == "1":
        display_pass = open("users.txt","r")
        lines = display_pass.readlines()
        for num, line in enumerate(lines):
            print(lines[num].strip())

    elif z == "2":
        new_name = input("Enter new user name: ")
        new_pass = input("Enter new user password: " )
        new_role = input("Enter new user role (admin, companyuser, jobseeker): " )
        with open("users.txt", "a") as file:
                file.write(f"{new_name},{new_pass},{new_role}\n")

# system_admin()