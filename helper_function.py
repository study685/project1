# global file paths
import os
BASE_DIR = os.path.join(os.getcwd(), "data")
CREDENTIAL_FILE = os.path.join(BASE_DIR, "users.txt")
JOBS_FILE = os.path.join(BASE_DIR, "jobs.txt")
COMPANY_FILE = os.path.join(BASE_DIR, "companyinfo.txt")
JOBSEEKERS_FILE = os.path.join(BASE_DIR, "jobseekers.txt")
APPLICATIONS_FILE = os.path.join(BASE_DIR, "applications.txt")
MANAGERIAL_FILE = os.path.join(BASE_DIR, "managerial.txt")
TECHNICAL_FILE = os.path.join(BASE_DIR, "technical.txt")

def update_users_file(old_name, new_name, role):
    """Update username in credentials file based on old name, new name, and role."""
    try:
        with open(CREDENTIAL_FILE, "r") as f:
            lines = f.readlines()

        updated_lines = []
        for line in lines:
            parts = line.strip().split(",")
            if parts[0].strip() == old_name and parts[2].strip() == role:
                parts[0] = new_name
            updated_lines.append(",".join(parts) + "\n")

        with open(CREDENTIAL_FILE, "w") as f:
            f.writelines(updated_lines)
        print(f"Username '{old_name}' updated to '{new_name}' in {role} file.")
    except FileNotFoundError:
        print(f"Error: The file '{CREDENTIAL_FILE}' was not found.")

def update_jobseeker_applications_file(old_name, new_name):
    """Update jobseeker name in applications file based on old name and new name."""
    try:
        with open(APPLICATIONS_FILE, "r") as f:
            lines = f.readlines()

        updated_lines = []
        for line in lines:
            parts = line.strip().split(",")
            if parts[2].strip() == old_name:
                parts[2] = new_name
            updated_lines.append(",".join(parts) + "\n")

        with open(APPLICATIONS_FILE, "w") as f:
            f.writelines(updated_lines)
        print(f"Jobseeker '{old_name}' updated to '{new_name}' in applications file.")
    except FileNotFoundError:
        print(f"Error: The file '{APPLICATIONS_FILE}' was not found.")

def update_applications_file(old_name, new_name, filename=APPLICATIONS_FILE):
    """Update company name in applications file based on old name and new name."""
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        updated_lines = []
        for line in lines:
            parts = line.strip().split(",")
            if parts[1].strip() == old_name:
                parts[1] = new_name
            updated_lines.append(",".join(parts) + "\n")

        with open(filename, "w") as f:
            f.writelines(updated_lines)
        print(f"Company '{old_name}' updated to '{new_name}' in applications file.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

def update_job_file(old_name, new_name, role, filename=JOBS_FILE):
    """
    Update job file entries based on the role:
    - If role is 'companyuser', update company name in jobs.txt.
    - If role is 'jobseeker', update jobseeker name in jobs.txt (if applicable).
    """
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        updated_lines = []
        for line in lines:
            parts = line.strip().split(",")
            if role == "companyuser" and parts[1].strip() == old_name:
                parts[1] = new_name
            elif role == "jobseeker" and parts[9].strip() == old_name:
                parts[9] = new_name
            updated_lines.append(",".join(parts) + "\n")

        with open(filename, "w") as f:
            f.writelines(updated_lines)

        print(f"{role.capitalize()} name updated from '{old_name}' to '{new_name}' in job listings.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

def get_jobs_from_file(filename=JOBS_FILE):
    """Read job listings from a specified file and return as a list."""
    try:
        jobs = []
        with open(filename, "r") as f:
            for line in f:
                line = line.strip().split(",")
                if line:
                    parts = []
                    for p in line:
                        parts.append(p.strip())
                    jobs.append(parts)
            return jobs

        if not jobs:
            return None
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None

def get_applicants_from_file(applications_file=APPLICATIONS_FILE):
    """Load applicants for a specific job from the applications file."""
    applicants = []
    try:
        with open(applications_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(",")
                applicants.append(parts)
        return applicants
    except FileNotFoundError:
        print(f"Error: The file '{applications_file}' was not found.")
        return []
    
# print(get_applicants_from_file(APPLICATIONS_FILE))

def get_filtered_jobs(jobs, *filters):
    i = 0
    while i < len(filters):
        key, value = filters[i]
        temp = []
        j = 0
        while j < len(jobs):
            job = jobs[j]
            if job[key].isdigit(): # filter by number value: year of experience, pay
                if int(job[key]) >= int(value):
                    temp.append(job)
            else:
                if str(job[key]).strip() == value.strip(): # filtered by string:category, job types, edu
                    temp.append(job)
            j += 1
        jobs = temp
        i += 1
    return jobs

def print_jobs(jobs):
    print(f"\n{'Job ID':<10}{'Job Title':<20}{'Category':<20}{'Company':<20}{'Job Type':<25}{'Min Education':<15}{'Exp req':<7}")
    i = 0
    while i < len(jobs):
        job = jobs[i]
        print(f"{job[0]:<10}{job[2]:<20}{job[3]:<20}{job[1]:<20}{job[6]:<25}{job[7]:<15}{job[8]:<7}")
        i += 1

def filter_jobs(file, *filters):
    jobs = get_jobs_from_file(file)
    filtered = get_filtered_jobs(jobs, *filters)
    print_jobs(filtered)

def display_jobs(filename=JOBS_FILE, filter=True):
    """Display job listings from a specified file and allow filtering."""
    jobs = get_jobs_from_file(filename)
    if not jobs:
        return "No jobs"
    print_jobs(jobs)
    if filter:
        choice = input("Enter -1 to filter jobs, 0 to go back: ")
        if choice != "-1":
            return
        filters = []
        while True:
            print("\nFilter by:\n1. Category\n2. Job Type\n3. Experience Required\n4. Min pay\n5. Education\n0. Done")
            option = input("Enter your choice (0 to finish): ")
            if option == "1":
                print("Job categories:\n1. Cybersecurity\n2. Software Engineering\n3. AI & Data Science")
                cat = input("Enter category to filter: ")
                if cat == "1":
                    filters.append((3, "Cybersecurity"))
                elif cat == "2":
                    filters.append((3, "Software Engineering"))
                elif cat == "3":
                    filters.append((3, "AI & Data Science"))
            elif option == "2":
                print("Job types:\n1. Full time (Junior)\n2. Full time (Senior)\n3. Part time")
                jt = input("Enter job type to filter: ")
                if jt == "1":
                    filters.append((6, "Full time (Junior)"))
                elif jt == "2":
                    filters.append((6, "Full time (Senior)"))
                elif jt == "3":
                    filters.append((6, "Part time"))
            elif option == "3":
                exp = input("Enter minimum experience required: ")
                filters.append((8, exp))
            elif option == "4":
                min_pay = input("Enter minimum pay:")
                filters.append((4, min_pay))
            elif option == "5":
                print("Education levels:\n1. Diploma\n2. Bachelor's\n3. Master's\n4. PhD")
                edu = input("Enter education to filter: ")
                if edu == "1":
                    filters.append((7, "Diploma"))
                elif edu == "2":
                    filters.append((7, "Bachelor's"))
                elif edu == "3":
                    filters.append((7, "Master's"))
                elif edu == "4":
                    filters.append((7, "PhD"))
            elif option == "0":
                break
            else:
                print("Invalid option.")
        if filters:
            filter_jobs(filename, *filters)

def get_jobseekers_from_file(filename=JOBSEEKERS_FILE):
    """Read jobseeker profiles from a specified file and return as a list."""
    try:
        jobseekers = []
        with open(filename, "r") as f:
            for line in f:
                line = line.strip().split(",")
                if line:
                    parts = []
                    for p in line:
                        parts.append(p.strip())
                    jobseekers.append(parts)
            return jobseekers
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    
def get_specific_jobseeker_detail_from_file(filename=JOBSEEKERS_FILE, name=None, company=None):
    """Read jobseeker profiles from a specified file and return as a list."""
    try:
        jobseekers = []
        with open(filename, "r") as f:
            for line in f:
                line = line.strip().split(",")
                if line:
                    parts = []
                    for p in line:
                        parts.append(p.strip())
                    jobseekers.append(parts)
            if name:
                for seeker in jobseekers:
                    if seeker[0] == name:
                        return seeker
            else:
                return jobseekers
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None

# print(get_specific_jobseeker_from_file(name="moe")) 

def get_companies_from_file(filename=COMPANY_FILE):
    """Read company profiles from a specified file and return as a list."""
    try:
        companies = []
        with open(filename, "r") as f:
            for line in f:
                line = line.strip().split(",")
                if line:
                    parts = []
                    for p in line:
                        parts.append(p.strip())
                    companies.append(parts)
            return companies
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None

def get_specific_company_detail_from_file(filename=COMPANY_FILE, name=None):
    """Read company profiles from a specified file and return as a list."""
    try:
        companies = []
        with open(filename, "r") as f:
            for line in f:
                line = line.strip().split(",")
                if line:
                    parts = []
                    for p in line:
                        parts.append(p.strip())
                    companies.append(parts)
            if name:
                for company in companies:
                    if company[0] == name:
                        return company
            else:
                return companies
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None

# print(get_specific_company_from_file(name="New Company"))

def validate_input(mode, *args):
    if mode == "nocomma":
        sentence = args[0]
        if "," in sentence:
            print("Sentence cannot contain commas.")
            return 'None'
        return sentence

    if mode == "option":
        input_val, options, label = args
        if input_val in options:
            return options[input_val]
        print(f"Invalid {label}. Choose from: {', '.join(options.keys())}.")
        return 'None'

    if mode == "pay":
        min_pay, max_pay = args
        if not min_pay.isdigit() or not max_pay.isdigit():
            print("Pay must be numeric.")
            return 'None', 'None'
        min_pay = int(min_pay)
        max_pay = int(max_pay)
        if min_pay > max_pay:
            print("Min pay must not exceed Max pay.")
            return 'None', 'None'
        return str(min_pay), str(max_pay)

    if mode == "isdigit":
        digit = args[0]
        if not digit.isdigit():
            print("Input must be numeric.")
            return
        return digit

    if mode == "islist":
        raw = args[0]

        if not raw:
            return 'None'

        parts = raw.split(",")

        items = []
        for item in parts:
            stripped = item.strip()
            if stripped:
                items.append(stripped)

        return str(items).replace("'", "").replace(",", ";")

    if mode == "age":
        age = args[0]
        if not age.isdigit():
            print("Age must be numeric.")
            return 'None'
        age = int(age)
        if not (1 <= age <= 199):
            print("Age must be between 1 and 199.")
            return 'None'
        return str(age)

    if mode == "email":
        email = args[0]
        if "@" not in email or "." not in email:
            print("Invalid email format.")
            return 'None'
        return email

    if mode == "url":
        url = args[0]
        if url.count(".") <= 1:
            print("URL must contain more than one '.'")
            return 'None'
        return url


def edit_profile(name, role):
    """
    Allow jobseekers or companies to edit their profile information in data files.
    Reads the respective file, displays current profile info, allows edits, and writes updates.
    """
    try:
        if role == "jobseeker":
            try:
                with open(JOBSEEKERS_FILE, "r+") as f:
                    lines = f.readlines()
                    index = 0
                    for line in lines:
                        parts = line.strip().split(",")
                        if parts[0] == name:
                            try:
                                # Display current profile information
                                print("\nProfile Info:")
                                print("Name:", parts[0])
                                print("Age:", parts[1])
                                print("Email:", parts[2])
                                print("Education:", parts[3])
                                print("Category:", parts[4])
                                print("Experience:", parts[5])
                                tech_l = parts[6].replace("[", "").replace("]", "").replace(";", ", ")
                                print("Technical Skills:", tech_l)
                                man_l = parts[7].replace("[", "").replace("]", "").replace(";", ", ")
                                print("Managerial Skills:", man_l)
                                print("Additional user description:", parts[8])

                                if input("Enter 1 to edit, 0 to go back: ") == "1":
                                    updated = []
                                    updated.append(input("Name: "))
                                    updated.append(input("Age: "))
                                    updated.append(input("Email: "))
                                    updated.append(input("Education: "))
                                    updated.append(input("Category: "))
                                    updated.append(input("Years of Experience: "))

                                    t_list = input("Technical Skills: ")
                                    t_list = t_list.replace(",",";")
                                    updated.append(f"[{t_list}]")
                                    
                                    m_list = input("Managerial Skills: ")
                                    m_list = m_list.replace(",",";")
                                    updated.append(f"[{m_list}]")
                                    
                                    updated.append(input("Min pay range: "))
                                    updated.append(input("Max pay range: "))
                                    updated.append(input("Additional user description: "))

                                    lines[index] = ",".join(updated) + "\n"
                                    f.seek(0)
                                    f.writelines(lines)
                                    
                                    try:
                                        update_users_file(name, updated[0], role)
                                        update_jobseeker_applications_file(name, updated[0])
                                        update_job_file(name, updated[0], role)
                                        print("\nProfile updated, please login again!")
                                        break
                                    except Exception as e:
                                        print("Error while updating related files:", str(e))
                            except Exception as e:
                                print("Error while editing jobseeker profile:", str(e))
                        index += 1
            except FileNotFoundError:
                print(f"Error: The file '{JOBSEEKERS_FILE}' was not found.")

        elif role == "companyuser":
            try:
                with open(COMPANY_FILE, "r+") as f:
                    company_info = f.readlines()
                    index = 0
                    for i in range(len(company_info)):
                        parts = company_info[i].strip().split(",")
                        if parts[0] == name:
                            try:
                                # Display current company info
                                print("\nCurrent Company Info:")
                                print("Company Name:", parts[0])
                                print("URL:", parts[1])
                                print("Description:", parts[2])

                                if input("Enter 1 to edit, 0 to return: ") == "1":
                                    updated = []
                                    updated.append(input("New Company Name: "))
                                    updated.append(input("New URL: "))
                                    updated.append(input("New Description: "))

                                    company_info[i] = ",".join(updated) + "\n"
                                    f.seek(0)
                                    f.writelines(company_info)
                                    
                                    try:
                                        update_users_file(name, updated[0], role)
                                        update_applications_file(name, updated[0])
                                        update_job_file(name, updated[0], role)
                                        print("\nProfile updated successfully!")
                                    except Exception as e:
                                        print("Error while updating related files:", str(e))
                            except Exception as e:
                                print("Error while editing company profile:", str(e))
                            break
                        index += 1
            except FileNotFoundError:
                print(f"Error: The file '{COMPANY_FILE}' was not found.")
    except Exception as e:
        print("Unexpected error:", str(e))


def add_profile(name, role):
    """
    Allow jobseekers or companies to add their profile information to the data files.
    The function collects the necessary information from the user and appends it to the respective file.
    The function handles both jobseeker and company profiles based on the role provided.
    It also handles the case where the file does not exist by creating it if necessary.
    The function prints a success message after adding the profile.
    """
    try:
        if role == "jobseeker":
            # Collect jobseeker information
            print("\nEnter Jobseeker Information:")
            updated = []
            updated.append(name)
            updated.append(input("Age: "))
            updated.append(input("Email: "))
            updated.append(input("Education: "))
            updated.append(input("Category: "))
            updated.append(input("Years of Experience: "))
            updated.append(input("Technical Skills (separated by comma): "))
            updated.append(input("Managerial Skills (separated by comma): "))
            updated.append(input("Additional description (no comma): "))

            # Append the new jobseeker information to the jobseekers file
            with open(JOBSEEKERS_FILE, "a") as f:
                f.write(",".join(updated) + "\n")
            print("\nJobseeker profile added successfully!")

        elif role == "companyuser":
            # Collect company information
            curl = input("URL: ")
            cdesc = input("Description: ")

            # Append the new company information to the companies file
            with open(COMPANY_FILE, "a") as f:
                f.write(f"{name},{curl},{cdesc}\n")
            print("\nCompany profile added successfully!")

    except FileNotFoundError:
        if role == "companyuser":
            file_name = COMPANY_FILE
        else:
            file_name = JOBSEEKERS_FILE

        print(f"Error: The file '{file_name}' was not found.")
