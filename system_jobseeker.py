def system_jobseeker(name):
    user = name
    print(f"--- Welcome to jobseeker system ---")
    print("1) Edit profile\n2) View jobs\n3) View Application")
    enter = input("Enter: ")

    if enter == "1":
        with open("jobseekers.txt", "r") as file:
            data = json.load(file)
            for user in data:
                if user["Name"] == "Uncle Roger":
                    login_user = user
                    break

        for title, detail in login_user.items():
            print(f"{title}: {detail}")
        
        enter = input("Enter 1 to edit, 0 to go back")
        
        if enter == "1":
            print("@@@Editing@@@")
            
            for title, detail in login_user.items():
                detail = input(f"New {title}:")
                login_user[title] = detail
            
            print("\nEdited details below:")
            
            for title, detail in login_user.items():
                print(f"{title}: {detail}")

    elif enter == "2":
        with open("jobs.json", "r") as file:
            data = json.load(file)

        jobs = data

        for i in range(len(jobs)):
            for title, detail in jobs[i].items():
                print(f"{title}: {detail}")
            print()    

    elif enter == "3":
        with open("applications.json", "r") as file:
            data = json.load(file)
        
        app = data
        
        for i in range(len(app)):
            for title, detail in app[i].items():
                print(f"{title}: {detail}")
            print()
    else:
        print("invalid enter")
