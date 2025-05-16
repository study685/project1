import csv
from system_jobListing import system_jobListing

def system_company():
    def applicants(file):
        with open(file, "r") as file1:
            lines = file1.readlines()
            if lines:
                headers = ["Name", "Age", "Education", "Years Experience"]
                data = []
                print(f"\n{headers[0]:<20}{headers[1]:<10}{headers[2]:<30}{headers[3]:<20}")
                for i in lines:
                    parts = i.strip().split(",")
                    data.append(parts)
                for idx, row in enumerate(data, start=1):
                    number = f"{idx})"
                    print(f"{row[0]:<20}{row[1]:<10}{row[2]:<30}{row[3]:<20}")
                print()
            else:
                print("Jobs listing is empty")

    def applicantsInfo(file, name):
        try:
            with open(file, "r") as file1:
                lines = csv.reader(file1)
                if lines:
                    headers = ["Application status", "Name", "Education", "Email", "Age", "Years Experience", "Technical skills", "Managerial Skills", "Additional description"]
                    for i in lines:
                        if i[1] == name:
                            print(f"{headers[0]}: {i[0]}")
                            print(f"{headers[1]}: {i[1]}")
                            print(f"{headers[2]}: {i[2]}")
                            print(f"{headers[3]}: {i[3]}")
                            print(f"{headers[4]}: {i[4]}")
                            print(f"{headers[5]}: {i[5]}")
                            print(f"{headers[6]}: {i[6]}")
                            print(f"{headers[7]}: {i[7]}")
                            print(f"{headers[8]}: {i[8]}")
                    print()
                else:
                    print("Jobs listing is empty")
        except FileNotFoundError:
            print("Error. File not found")

    def load_skills(category):
        skills ={
            "Cybersecurity": [
                "Network Security", "Cryptography", "Firewall Management", "Penetration Testing", "Malware Analysis"
            ],
            "Software Engineering": [
                "Python", "Java", "C++", "Javascript", "React", "Android", "iOS", "PHP", "HTML", "MySQL", "LAMP", "LEMP", "Mongo DB", "MSSQL", "Go"
            ],
            "AI & Data Science": [
                "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Natural Language Processing", "R", "Python", "SQL", "Big Data"
            ]
        }
        return skills.get(category, [])

    def load_managerialSkills():
        return  [
            "Team Leadership", "Project Management", "Budgeting", "Conflict Resolution", "Strategic Planning"
        ]

    def newJobs():
        title = input("\nEnter the Job Title: ")
        category = input("Choose the category (Cybersecurity, Software Engineering, AI & Data Science): ")
        skills = load_skills(category)
        print("\nTechnical Skills:")
        for idx, skill in enumerate(skills, start=1):
            print(f"{idx}) {skill}")
        skillChoices = input("Enter the number of skills, separate by commas: ")
        selectedSkills = [skills[int(choice)-1] for choice in skillChoices.split(",")]
        minPay = input("Enter minimum pay: ")
        maxPay = input("Enter maximum pay: ")
        jobType = input("Choose Job Type (Part time, Full time (Junior), Full time (Senior)): ")
        
        managerialSkills = []
        if jobType == "Full time (Senior)":
            managerialSkills = load_managerialSkills()
            print("\nManagerial Skills: ")
            for idx, skill in enumerate(managerialSkills, start=1):
                print(f"{idx}) {skill}")
            
            selected_managerialSkills = input("Enter the number of managerial skills, separated by commas: ")
            selected_managerialSkills = [managerialSkills[int(choice) - 1] for choice in selected_managerialSkills.split(",")]
        minEducation = input("Enter minimum education: ")
        exp = input("Years of experience: ")
        company = input("Company name: ")
        add_desc = input("Enter additional job description: ")

        with open("jobs.txt", "a") as file:
            file.write(f"{title},{category},{minPay},{maxPay},{jobType},{minEducation},{exp},{selectedSkills},{selected_managerialSkills},{add_desc}\n")


    print("\n1) Edit company profile\n2) View jobs posted\n3) Add new job\n ")
    option1 = input("Enter option: ")
    if option1 == "1":
        try:
            with open("companyinfo.txt", "r") as file:
                lines = file.readlines()
                data = []
                if lines:
                    for i in lines:
                        parts = i.strip().split(",")
                        data.append(parts)
                    name1 = input("\nEnter company name: ")
                    for i in data:
                        if i[0] == name1:
                            print()
                            print(f"Company Name: {i[0]}")
                            print(f"Company URL: {i[1]}")
                            print(f"Description: {i[2]}")
                            print()
                else:
                    print("Company profile is empty")
        except FileNotFoundError:
            print("Error. File not Found")
        
        option2 = input("Enter 1 to edit, or 0 to return back to main menu: ")
        if option2 == "1":
            with open ("companyinfo.txt","a") as file:
                name = input("\nName: ")
                url = input("url: ")
                desc = input("description: ")
                file.write(f"{name},{url},{desc}\n")

    elif option1 == "2":
        name2 = input("\nEnter company name: ")
        # jobs("jobs.txt", name2)
        print("There are 3 applicants")
        option3 = input("Enter 1 to view applications, or 0 to go back: ")
        if option3 == "1":
            applicants("applicants.txt")
            option4 = input("Select user to view details, or 0 to go back. ")
            print()
            applicantsInfo("applicantsInfo.txt", option4)
            option5 = input("Enter 1 to approve this applicant for interview, -1 to reject, 0 to go back ")

    elif option1 == "3":
        newJobs()



                