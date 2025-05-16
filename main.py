from system_jobListing import system_jobListing
from login import login

print("@@@@ SCSU Jobs Portal @@@@@")
print("1. View Jobs\n2. Login\n0. Exit")
endProgram = False

while not endProgram:
    option = input("Enter Option: ")
    if option == "1":
        system_jobListing()
    elif option == "2":
        login()
    elif option == "0":
        print("Exiting the program.")
        endProgram = True