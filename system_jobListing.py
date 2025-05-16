def read_jobs_from_file(filename):
    jobs = []
    with open(filename, "r") as file:
        content = file.read().split("=====")
        for job in content:
            if job.strip():
                job_data = {}
                jobcontent = job.split("\n")
                for line in jobcontent:
                    if line.strip():
                        keyvalue = line.split(":")
                        if len(keyvalue) == 2:
                            key = keyvalue[0].strip()
                            value = keyvalue[1].strip()
                            job_data[key] = value
                jobs.append(job_data)
    return jobs


def display_job_list(jobs):
    print(f"{'Job No.':<5} {'Job Title':<20} {'Category':<20} {'Company':<20} {'Job Type':<20} {'Min Education':<20} {'Exp req':<20}")
    for idx, job in enumerate(jobs, start=1):
        print(f"{idx:<5} {job.get('Job Title', 'N/A'):<20} {job.get('Category', 'N/A'):<20} {job.get('Company', 'N/A'):<20} "
              f"{job.get('Job Type', 'N/A'):<20} {job.get('Min Education', 'N/A'):<20} {job.get('Years of Experience required', 'N/A'):<20}")


def show_job_details(job):
    print("\nJob Details:")
    for key, value in job.items():
        print(f"{key}: {value}")
    print()


def system_job_listing():
    jobs = read_jobs_from_file("jobs.txt")
    display_job_list(jobs)
    user_input = input("Enter the job number to view details, or 0 to go back: ")

    job_number = int(user_input)
    if 1 <= job_number <= len(jobs):
        show_job_details(jobs[job_number - 1])
    else:
        print("Invalid job number.")