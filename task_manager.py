# Opening and reading file
user = open("user.txt", "r")

# Creating empty dictionary to store usernames and passwords
login_dict = {}

# looping through the file and adding usernames and passwords to the dictionary
for line in user:
    username, password = line.split(", ")
    login_dict[username] = password.strip()

# Closing file
user.close()

print(f"       \033[1;32m  ╔═══════════════════════════╗ ")
print(f"═════════   WELCOME TO TASK MANAGER   ═════════")
print(f"         ╚═══════════════════════════╝ \n")
pattern = "----------------------------------------------------"

# Variable created to check if user is admin when using menu
is_admin = False

# Requesting username and password
# Looping to check if username and password are correct
while True:
    user_n = input("► Enter Username: ").lower().strip()
    if user_n in login_dict:
        pass_w = input("► Enter Password: ")
        correct_pass = login_dict.get(user_n)
        if correct_pass == pass_w:
            print(f"\n{pattern}")
            print(f"\n✦ Welcome >{user_n}<, You have logged in successfully!")
            print(f"\n{pattern}")
            break
        else:
# Displaying error message if user inputs invalid password
            print("☒ Invalid Password, Please Try Again")
            print(pattern)
    else:
# Displaying error message if user inputs invalid username
        print("☒ Invalid Username, Please Try Again.")
        print(pattern)


# Checking if user is admin and displaying different menu options
while True:
    if user_n == "admin" and pass_w == login_dict["admin"]:
        is_admin = True
        print(f"         ╔═══════════════════════════╗ ")
        print(f"═════════             MENU            ═════════")
        print(f"         ╚═══════════════════════════╝ \n")
        menu = input('''✦ Select one of the following Options below:
                        
► r - Registering a user
► a - Adding a task
► va - View all tasks
► vm - view my task
► s - Statistics
► e - Exit
: ''').lower()
        
    else:
        print(f"         ╔═══════════════════════════╗ ")
        print(f"═════════             MENU            ═════════")
        print(f"         ╚═══════════════════════════╝ \n")

# Displaying menu for other users who are not admin
        menu = input('''✦ Select one of the following Options below:
                            
► r - Registering a user
► a - Adding a task
► va - View all tasks
► vm - view my task
► e - Exit
: ''').lower()
        

# Allowing Admin only to register users   
    if menu == 'r':
        if is_admin:
            print(f"         ╔═══════════════════════════╗ ")
            print(f"═════════           REGISTER          ═════════")
            print(f"         ╚═══════════════════════════╝ \n")
            new_username = input("► Enter New Username: ").lower().strip()
            new_password = input("► Enter New Password: ")
            confirm_pass = input("► Confirm New Password: ")
            
# Confirming if passwords match and writing it to txt file
            if new_password == confirm_pass:
                user_append = open("user.txt", "a")
                user_append.write("\n")
                user_append.write(f"{new_username},")
                user_append.write(f" {new_password}")
                user_append.close()
                print(pattern)
                print(f"✦ New User: >{new_username}< Successfully Added!")
                print(pattern)
            else:
# Displaying error message if user inputs passwords that do not match
                print("☒ Password does not match!")
                print(pattern)
        else:
            print(f"\n{pattern}")
            print("\n☒ Access Denied: Only an admin can access this option.")
            print(f"\n{pattern}")

# Adding user tasks 
    elif menu == 'a':
        pass
        print(f"         ╔═══════════════════════════╗ ")
        print(f"═════════          ADD TASKS          ═════════")
        print(f"         ╚═══════════════════════════╝ \n")
        
# Requesting username to associate task with
        task_usernname = input("► Enter Username: ").lower().strip()
        
# Checking if user is in dictionary
        while task_usernname not in login_dict:
            print("☒ Invalid Username, Please try again.")
            print(pattern)
            task_usernname = input("► Enter Username: ").lower().strip()
            
# Checking if username is in dictionary
        if task_usernname in login_dict:
            print(f"✦ Assigning Task For: >{task_usernname}<!\n")
            print(pattern)
# Requesting task information in detail
            task_title = input("\n► Enter Task:  ")
            task_description = input("\n► Enter Task Description:  ")
            task_due_date = input("\n► Enter Task Due Date:  ")
            task_current_date = input("\n► Enter Current date: " )
            print(f"\n{pattern}")
            print("\n✦ Task Assigned Successfully!\n")
            print(pattern)
            
# Writing task information provided to the txt file
            task_append = open("tasks.txt", "a")
            task_append.write("\n")
            task_append.write(f"{task_usernname},")
            task_append.write(f" {task_title},")
            task_append.write(f" {task_description},")
            task_append.write(f" {task_due_date},")
            task_append.write(f" {task_current_date},")
            task_append.write(f" No")
            task_append.close()
        else:
# Displaying error message if user inputs invalid username
            if task_usernname not in login_dict:
                print("☒ Invalid Username, Please try again.")
                print(pattern)
                
            continue
        
# Allowing user to view all tasks
    elif menu == 'va':
        pass
        print(f"         ╔═══════════════════════════╗ ")
        print(f"═════════          ALL TASKS          ═════════")
        print(f"         ╚═══════════════════════════╝ \n")
        all_tasks = open("tasks.txt", "r")
        tasks = all_tasks.readlines()
        
# Counting tasks using for loop and enumerate
# Starting task count from 1 instead of 0
        for pos, data in enumerate(tasks, 1):
            split_tasks = data.strip("\n").split(", ")
            output = f"------------------------[{pos}]------------------------\n\n"
            output += f"✦ Assigned To: \t\t{split_tasks[0]}\n\n"
            output += f"✦ Task: \t\t{split_tasks[1]}\n\n"
            output += f"✦ Task Description: \t{split_tasks[2]}\n\n"
            output += f"✦ Date Assigned: \t{split_tasks[3]}\n\n"
            output += f"✦ Date Due: \t\t{split_tasks[4]}\n\n"
            output += f"✦ Task Complete: \t{split_tasks[5]}\n"
            print(output)
            
# Closing file
        all_tasks.close()
        
# Allowing user to view their own tasks only
    elif menu == 'vm':
        pass
        print(f"         ╔═══════════════════════════╗ ")
        print(f"═════════          USER TASKS         ═════════")
        print(f"         ╚═══════════════════════════╝ \n")
# Checking and displaying tasks associated with the user who is logged in
        if user_n in login_dict:
            with open("tasks.txt", "r") as task_file:
                for line in task_file:
                    task_data = line.strip().split(", ")
                    if task_data[0] == user_n:
                        print(f"✦ Task: \t\t{task_data[1]}\n")
                        print(f"✦ Task Description: \t{task_data[2]}\n")
                        print(f"✦ Date Assigned: \t{task_data[3]}\n")
                        print(f"✦ Due Date: \t\t{task_data[4]}\n")
                        print(f"✦ Task Complete: \t{task_data[5]}\n")
                        print(f"{pattern} \n")
                        
# Displaying statistics for number of tasks and users (admin access only)               
    elif menu == 's':
        if is_admin:
            print(f"         ╔═══════════════════════════╗ ")
            print(f"═════════   STATISTICS (Admin Only)   ═════════")
            print(f"         ╚═══════════════════════════╝ \n")
        # Creating count variable for total number of tasks
            task_count = 0
            with open("tasks.txt", "r") as task_file:
                for line in task_file:
                    task_count += 1
            
            print(f"Total Number Of Tasks: {task_count}\n")
        # Creating count variable for total number of users    
            user_count = 0
            with open("user.txt", "r") as user_file:
                for line in user_file:
                    user_count += 1

            print(f"Total Number Of Users: {user_count}\n")
            
        continue

# Creating option to exit program
    elif menu == 'e':
        print(f"         ╔═══════════════════════════╗ ")
        print(f"═════════        GOODBYE >{user_n}<      ═════════")
        print(f"         ╚═══════════════════════════╝ \n")
        exit()

# Displaying error message if user inputs invalid option
    else:
        print(pattern)
        print("\n☒ Invalid Option, Please Try Again\n")
        print(pattern)