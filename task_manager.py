# Importing datetime for user inputs related to dates
from datetime import datetime

# Creating Function to read user.txt as a list
def read_user_file(file_name):
    with open(file_name, "r") as user:
    # Creating dictionary for usernames and passwords
        login_dict = {}
        for user_login in user:
            username, password = user_login.split(", ")
            login_dict[username] = password.strip()
        user.close()
        return login_dict
    
    
# Creating Function to check if user is the admin
def is_admin(username, login_dict):
    if username == "admin" and login_dict[username] == login_dict["admin"]:
        return True
    else:
        return False


# Creating Function to register a new user (admin access only)
def reg_user(login_dict, is_admin):
# Checking if user is admin
    if is_admin:
    # Requesting new username
        new_username = input("► Enter New Username: ").lower().strip()
    # If username is less than 3 characters then displaying error message
        if len(new_username) < 3:
            print("----------------------------------------------------")
            print("✘ Username is too short!")
            print("----------------------------------------------------")
    # Checking if username already exists in user.txt file
        elif new_username in login_dict:
            print("----------------------------------------------------")
            print("✘ Username Already Exists, Please Try Again!")
            print("----------------------------------------------------")
        else:
    # Requesting new password
            new_password = input("► Enter New Password: ")
            if len(new_password) < 3:
                print("----------------------------------------------------")
                print("✘ Password is too short!")
                print("----------------------------------------------------")
                return
            confirm_pass = input("► Confirm New Password: ")
    # Confirming if passwords match and writing it to user.txt file
            if new_password == confirm_pass:
                with open("user.txt", "a") as user_append:
                    user_append.write("\n")
                    user_append.write(f"{new_username},")
                    user_append.write(f" {new_password}")
                print("----------------------------------------------------")
                print(f"✦ New User: >{new_username}< Successfully Added!")
                print("----------------------------------------------------")
            else:
    # Displaying error message if passwords do not match        
                print("----------------------------------------------------")
                print("✘ Passwords do not match, Please Try Again!")
                print("----------------------------------------------------")


# Creating Function that allows user to add tasks to tasks.txt file
def add_task(login_dict):
# Requesting username to assign new task to
    task_username = input("► Enter Username: ").lower().strip()
# Checking if username exists
    if task_username in login_dict:
# Requesting task information
        task_title = input("\n► Enter Task:  ")
        task_description = input("\n► Enter Task Description:  ")
        
# Using while loop to check date format is correct
        while True:
            try:
                task_due_date_input = input("\n► Enter Task Due Date (dd mon yyyy):  ")
        # Using import datetime to get accurate date information
                task_due_date = datetime.strptime(task_due_date_input, '%d %b %Y')
        # Breaking while loop if input is in the correct format
                
        # Using try except to display error message if user enters incorrect format
            except ValueError:
                print("\n----------------------------------------------------")
                print("✘ Invalid date format, please enter date in the format 'dd mon yyyy'.")
                print("----------------------------------------------------")
                continue
            
            while True:
                try:
                    task_current_date_input = input("\n► Enter Current date (dd mon yyyy): ")
                    task_current_date = datetime.strptime(task_current_date_input, '%d %b %Y')
                    break
                except ValueError:
                    print("\n----------------------------------------------------")
                    print("✘ Invalid date format, please enter date in the format 'dd mon yyyy'.")
                    print("----------------------------------------------------")
                    continue
                    
        # Adding new task information to tasks.txt file
            with open ("tasks.txt", "a") as task_append:
                task_append.write("\n")
                task_append.write(f"{task_username},")
                task_append.write(f" {task_title},")
                task_append.write(f" {task_description},")
                task_append.write(f" {task_due_date.strftime('%d %b %Y')},")
                task_append.write(f" {task_current_date.strftime('%d %b %Y')},")
                task_append.write(f" No")
                print("\n----------------------------------------------------")
                print("✦ Task Assigned Successfully!")
                print("----------------------------------------------------")
                break
# Displaying error message if username does not exist in user.txt
    else:
        print("----------------------------------------------------")
        print("✘ Invalid Username, Please try again.")
        print("----------------------------------------------------")


# Creating Function that allows user to see all tasks in tasks.txt file
def view_all():
    with open ("tasks.txt", "r") as tasks_read:
        all_tasks = tasks_read.readlines()
# Assigning each task to a number starting from 1    
    for pos, task_line in enumerate(all_tasks, 1):
# Turning data from tasks.txt file into a list
        split_tasks = task_line.strip("\n").split(", ")
# Displaying all task data in a readable format
        all_user_tasks = f"--------------------------[TASK: {pos}]--------------------------\n\n"
        all_user_tasks += f"✦ Assigned To: \t\t{split_tasks[0]}\n\n"
        all_user_tasks += f"✦ Task: \t\t{split_tasks[1]}\n\n"
        all_user_tasks += f"✦ Task Description: \t{split_tasks[2]}\n\n"
        all_user_tasks += f"✦ Date Assigned: \t{split_tasks[3]}\n\n"
        all_user_tasks += f"✦ Date Due: \t\t{split_tasks[4]}\n\n"
        all_user_tasks += f"✦ Task Complete: \t{split_tasks[5]}\n"
        print(all_user_tasks)


# Creating Function that allows user to see and edit their own tasks
def view_mine(current_user, login_dict):
    with open("tasks.txt", "r") as tasks_read:
        all_tasks = tasks_read.readlines()
    # Creating variable to check if task is found 
        task_found = False
    # Assigning each task to a number starting from 1 
        for pos, task_line in enumerate(all_tasks, 1):
    # Turning data from tasks.txt file into a list
            task_data = task_line.strip("\n").split(", ")
    # If task is assigned to user then displaying task data in a readable format
            if task_data[0] == current_user:
                task_found = True
                my_tasks = f"\n------------------------[TASK: {pos}]------------------------\n\n"
                my_tasks += f"✦ Assigned To: \t\t{task_data[0]}\n\n"
                my_tasks += f"✦ Task: \t\t{task_data[1]}\n\n"
                my_tasks += f"✦ Task Description: \t{task_data[2]}\n\n"
                my_tasks += f"✦ Date Assigned: \t{task_data[3]}\n\n"
                my_tasks += f"✦ Due Date: \t\t{task_data[4]}\n\n"
                my_tasks += f"✦ Task Complete: \t{task_data[5]}\n\n"
                my_tasks += f"---------------------------------------------------------"
                print(my_tasks)
    # Displaying error message if user has no tasks   
        else:
            if not task_found:
                print("----------------------------------------------------")
                print("✘ User has no tasks!")
                print("----------------------------------------------------")
                return
        
    while True:
        print(f"\n----------------------[TASK EDITOR]----------------------\n\n")
    # Requsting task number from user or -1 to exit loop
        try:
            task_num = int(input("► Please enter task number to edit or enter -1 to exit: "))-1
        except Exception:
            print("\n----------------------------------------------------")
            print("✘ Invalid input, Please enter a number!!")
            print("----------------------------------------------------")
            continue
            
        if task_num+1 == -1:
            break
        
# Displaying error message if task number does not exist
        if task_num < 0 or task_num >= len(all_tasks):
                print("\n----------------------------------------------------")
                print("✘ Invalid Task number, Please try again!")
                print("----------------------------------------------------")
                continue

        while True:
        # Creating variable for the chosen task
            edit_data = all_tasks[task_num]
        # Requsting option number from user or -1 to exit loop
            try:
                task_choice = int(input('''\n✦ Select one of the following Options below or enter -1 to exit: 
                                
► 1 - Mark Task As Complete
► 2 - Edit Task
► -1 - Exit
: '''))
        # Using try except to display error message if number is not entered        
            except Exception:
                print("\n----------------------------------------------------")
                print("✘ Invalid input, Please enter a number!")
                print("----------------------------------------------------")
                continue
            
            if task_choice == -1:
                break
            
        # Displaying error message if menu number does not exists
            if task_choice <= 0 or task_choice >= 3:
                    print("----------------------------------------------------")
                    print("✘ Invalid Task number, Please try again!")
                    print("----------------------------------------------------")
                    continue
            
        # Allowing user to Mark task as complete
            if task_choice == 1:
                print(f"\n------------[1 - MARK TASK AS COMPLETE]------------\n\n")
            # Creating chosen task into a list
                split_data = edit_data.split(", ")
            # Turning task status to complete
                split_data[-1] = "Yes\n"
            # Returning line of task back to a string
                new_data = ", ".join(split_data)
            # Creating variable for new data created
                all_tasks[task_num] = new_data
        
            # Writing new data to tasks.txt file    
                with open ("tasks.txt", "w") as tasks_write:
                    for line in all_tasks:
                        tasks_write.write(line)
                    print("----------------------------------------------------")
                    print("✦ Task successfully updated!")
                    print("----------------------------------------------------")
                continue
            
            
        # Allowing user to edit the task 
            if task_choice == 2:
                print(f"\n------------------[2 - EDIT TASK]------------------\n\n")
            # Creating task chosen into a list
                user_data = edit_data.split(", ")
            # If task is completed then informing user it can not be edited
                if user_data[-1] == "Yes":
                    print("----------------------------------------------------")
                    print("✘ Task can only be edited if it is not completed!")
                    print("----------------------------------------------------")
                    continue
            # If task is incomplete then user can choose how to edit task           
                else:
            # Requsting option number from user or -1 to exit loop
                    try:
                        option = int(input('''✦ Select one of the following Options below or enter -1 to exit:
            
► 1 - Edit User Assigned
► 2 - Edit Due Date
► -1 - Exit
: '''))
            # Using try except to display error message if number is not entered              
                    except Exception:
                        print("\n----------------------------------------------------")
                        print("✘ Invalid input, Please enter a number!")
                        print("----------------------------------------------------")
                        continue
                        
                    if option == -1:
                        break
                    
                # Allowing user to editing username assigned to task  
                    if option == 1:
                        print(f"\n------------------[1 - EDIT USER]------------------\n\n")
                    # Checking if user entered exists
                        user_data[0] = input("► Enter New User: ")
                    # Displaying error message if username does not exist
                        if user_data[0] not in login_dict:
                            print("----------------------------------------------------")
                            print("✘ User does not exist, Please Try again!")
                            print("----------------------------------------------------")
                            continue
                        else:
                    # If user exists then changing username assigned to the task
                    # Creating chosen task into a list
                            split_user = edit_data.split(", ")
                    # Changing user assigned using user input and using it as confirmation
                            split_user[0] = input("► Confirm New User: ")
                    # Checking if usernames match
                            if user_data == split_user:
                    # Returning line of task back to a string
                                new_user = ", ".join(split_user)
                    # Creating variable for new data created
                                all_tasks[task_num] = new_user
                    # Writing new data to tasks.txt file      
                                with open ("tasks.txt", "w") as tasks_write:
                                    for line in all_tasks:
                                        tasks_write.write(line)
                                    print("----------------------------------------------------")
                                    print(f"✦ User successfully updated to {split_user[0]}!")
                                    print("----------------------------------------------------")
                                    
                            else:
                    # Returning error message if new username assigned does not match
                                print("----------------------------------------------------")
                                print("✘ Username does not match, Please Try again!")
                                print("----------------------------------------------------")
                                    
                                    
                    if option == 2:
                        print(f"\n------------------[2 - EDIT DUE DATE]------------------\n\n")
                    # Using while loop to check date format is correct
                        while True:
                            # Creating chosen task into a list
                            split_date_input = edit_data.split(", ")
                            # Requesting new due date in a specific format
                            split_date_input[-2] = input("Enter New Due Date (dd mon yyyy): ")
                            try:
                        
                        # Checking if date format is correct
                                split_date = datetime.strptime(split_date_input[-2], '%d %b %Y')
                                
                        # Using try except to display error message if user inputs incorrect format
                            except ValueError:
                                print("\n----------------------------------------------------")
                                print("✘ Invalid date format, please enter date in the format 'dd mon yyyy'.")
                                print("----------------------------------------------------")
                            else:
                        # Returning line of task back to a string
                                new_date = ", ".join(split_date_input)
                        # Creating variable for new data created
                                all_tasks[task_num] = new_date
                        
                        # Writing new data to tasks.txt file    
                                with open ("tasks.txt", "w") as tasks_write:
                                    for line in all_tasks:
                                        tasks_write.write(line)
                                    print("----------------------------------------------------")
                                    print(f"✦ Date successfully updated to {split_date_input[-2]}!")
                                    print("----------------------------------------------------")
                                break
                        
                # Returning error if user inputs invalid option       
                    else:
                        if option < 0 or option >= 3:
                            print("----------------------------------------------------")
                            print("✘ Entry Invalid, Please try again!")
                            print("----------------------------------------------------")
                            break
                            
                               
                               
# view_mine(read_user_file("user.txt"))
print(f"       \033[1;32m  ╔═══════════════════════════╗ ")
print(f"═════════   WELCOME TO TASK MANAGER   ═════════")
print(f"         ╚═══════════════════════════╝ \n")
pattern = "----------------------------------------------------"


# Looping to check if username and password are correct
while True:
# Requesting username 
    user_n = input("► Enter Username: ").lower().strip()
# Checking if username is is user.txt file
    if user_n in read_user_file("user.txt"):
# Requesting password     
        pass_w = input("► Enter Password: ")
# Getting password that matches username in user.txt file
        correct_pass = read_user_file("user.txt").get(user_n)
# Checking if passwords match
        if correct_pass == pass_w:
            print(pattern)
            print(f"✦ Welcome >{user_n}<, You have logged in successfully!")
            print(pattern)
            break
        else:
    # Displaying error message if user inputs invalid password
            print(pattern)
            print("☒ Invalid Password, Please Try Again")
            print(pattern)
    else:
    # Displaying error message if user inputs invalid username
        print(pattern)
        print("☒ Invalid Username, Please Try Again.")
        print(pattern)

# Checking if user is admin and displaying different menu options
while True:
    if is_admin(user_n, read_user_file("user.txt")):
        print("\n")
        print(f"\033[1;32m         ╔═══════════════════════════╗ ")
        print(f"═════════             MENU            ═════════")
        print(f"         ╚═══════════════════════════╝ \n")
        menu = input('''✦ Select one of the following Options below:

► r - Registering a user
► a - Adding a task
► va - View all tasks
► vm - View my task
► gr - Generate reports
► ds - Statistics
► e - Exit
: ''').lower()

    else:
        print(f"         ╔═══════════════════════════╗ ")
        print(f"═════════             MENU            ═════════")
        print(f"         ╚═══════════════════════════╝ \n")

# Displaying menu for other users who are not admin
        menu = input('''✦ Select one of the following Options below:

► a - Adding a task
► va - View all tasks
► vm - View my task
► e - Exit
: ''').lower()

# Creating menu option for admin to register users
    if menu == 'r':
        pass
        print(f"         ╔═══════════════════════════╗ ")
        print(f"═════════           REGISTER          ═════════")
        print(f"         ╚═══════════════════════════╝ \n")
        reg_user(read_user_file("user.txt"), is_admin)

# Creating menu option for adding tasks
    elif menu == 'a':
        pass
        print(f"         ╔═══════════════════════════╗ ")
        print(f"═════════          ADD TASKS          ═════════")
        print(f"         ╚═══════════════════════════╝ \n")
        add_task(read_user_file("user.txt"))
        continue

# Creating menu option for viewing all tasks
    elif menu == 'va':
        pass
        print(f"         ╔═══════════════════════════╗ ")
        print(f"═════════          ALL TASKS          ═════════")
        print(f"         ╚═══════════════════════════╝ \n")
        view_all()

# Creating menu option for viewing users tasks
    elif menu == 'vm':
        pass
        print(f"         ╔═══════════════════════════╗ ")
        print(f"═════════          USER TASKS         ═════════")
        print(f"         ╚═══════════════════════════╝ \n")
        view_mine(user_n, read_user_file("user.txt"))

# Creating menu option for admin to generate reports
    elif menu == 'gr':
        pass
        if is_admin:
            print(f"         ╔═══════════════════════════╗ ")
            print(f"═════════     REPORTS (Admin Only)    ═════════")
            print(f"         ╚═══════════════════════════╝ \n")
            
    # Generating reports for task_overview.txt
        # The total number of tasks
        # Creating counter
            task_count = 0
            with open ("tasks.txt", "r") as tasks_read:
        # Incrementing counter for every line in task.txt file    
                for line in tasks_read:
                    task_count += 1
                
                
        # The total number of completed tasks
        # Creating counter
            num_completed_tasks = 0
            with open ("tasks.txt", "r") as tasks_read:
                read_tasks = tasks_read.readlines()
        # Loop through each task and turn into list
                for line in read_tasks:
                    task_detail = line.strip().split(", ")
        # If the task completion status is "Yes", increment the counter
                    if task_detail[-1] == "Yes":
                        num_completed_tasks += 1
            
            
        # The total number of uncompleted tasks
        # Creating counter
            num_uncompleted_tasks = 0
            with open ("tasks.txt", "r") as tasks_read:
                read_tasks = tasks_read.readlines()
            for line in read_tasks:
                task_detail = line.strip().split(", ")
        # If the task completion status is "No", increment the counter
                if task_detail[-1] == "No":
                    num_uncompleted_tasks += 1
            
            
        # The total number of tasks that are overdue
        # Creating variable for the current date 
            current_date = datetime.now().date()
        # Creating counter
            num_overdue_tasks = 0
            with open("tasks.txt", "r") as tasks_read:
                read_tasks = tasks_read.readlines()
                for line in read_tasks:
                    task_detail = line.strip().split(", ")
        # Check if the task is incomplete and if its due date has passed
                    if task_detail[-1] == "No" and datetime.strptime(task_detail[4], '%d %b %Y').date() < current_date:
                        num_overdue_tasks += 1
            
            
        # The percentage of tasks that are incomplete
            task_count_2 = 0
            per_uncompleted_tasks = 0
            with open("tasks.txt", "r") as tasks_read:
                read_tasks = tasks_read.readlines()
        # Incrementing counter for every line in task.txt file
                for line in read_tasks:
                    task_count_2 += 1
                    task_detail = line.strip().split(", ")
        # Check if the task is incomplete and incrementing counter if true
                    if task_detail[-1] == "No":
                        per_uncompleted_tasks += 1
        # Calculating the percentage of incomplete tasks
                percentage_incomplete = (per_uncompleted_tasks / task_count_2) * 100
                
                
        # The percentage of tasks that are overdue
        # Creating counters
            task_count_3 = 0
            per_overdue_tasks = 0
        # today = datetime.today().date()
            with open("tasks.txt", "r") as tasks_read:
                read_tasks = tasks_read.readlines()
        # Incrementing counter for every line in task.txt file
                for line in read_tasks:
                    task_count_3 += 1
                    task_detail = line.strip().split(", ")
        # Checking due date and correct format
                    due_date = datetime.strptime(task_detail[4], "%d %b %Y").date()
        # If task is incomplete and overdue, incrementing the counter
                    if task_detail[-1] == "No" and current_date > due_date:
                        per_overdue_tasks += 1
        # Calculating the percentage of overdue tasks
                percentage_overdue = (per_overdue_tasks / task_count_3) * 100
            
            
        # Writing reports to new file
            with open("task_overview.txt", "w+") as task_over:
                task_over.write(f"Total Number Of Tasks: {task_count}\n")
                task_over.write(f"Total number of completed tasks: {num_completed_tasks}\n")
                task_over.write(f"Total number of uncompleted tasks: {num_uncompleted_tasks}\n")
                task_over.write(f"Number of overdue tasks: {num_overdue_tasks}\n")
                task_over.write(f"Percentage of tasks that are incomplete: {percentage_incomplete:.2f}%\n")
                task_over.write(f"Percentage of tasks that are overdue: {percentage_overdue:.2f}%")
            
            print("✦ Text file 'task_overview.txt' has been generated ✅\n")
            
    # Generating reports for user_overview.txt        
        # The total number of users
        # Creating counter
            user_count = 0
            with open ("user.txt", "r") as user_read:
        # Incrementing counter for every line in user.txt file
                for line in user_read:
                    user_count += 1
            
            
        # The total number of tasks
        # Creating counter
            task_count_4 = 0
            with open ("tasks.txt", "r") as tasks_read:
        # Incrementing counter for every line in tasks.txt file   
                for line in tasks_read:
                    task_count_4 += 1
                
                
        # The total number of tasks assigned to a user
        # Looping through all usernames in dictionary
            for username in read_user_file("user.txt").keys():
        # Creating counter
                user_task_count = 0
                with open("tasks.txt", "r") as tasks_file:
                    read_tasks = tasks_file.readlines()
        # Incrementing counter for every line in tasks.txt file if username is in task
                    for line in read_tasks:
                        task_detail = line.strip().split(", ")
                        if task_detail[0] == username:
                            user_task_count += 1
            
            
        # The percentage of tasks that have been assigned to a user
        # Looping through all usernames in dictionary
            for username in read_user_file("user.txt").keys():
            # Creating counters
                task_count_5 = 0
                user_task_count_2 = 0
                with open("tasks.txt", "r") as tasks_read:
                    read_tasks = tasks_read.readlines()
            # Incrementing counter for every line in tasks.txt file
                    for line in read_tasks:
                        task_detail = line.strip().split(", ")
                        task_count_5 += 1
            # Incrementing counter if the task is assigned to the user
                        if task_detail[0] == username:
                            user_task_count_2 += 1
            # Checking if user has tasks
                    if user_task_count_2 == 0:
                        percentage_assigned = 0
                    else:
            # Calculating percentage of tasks assigned to users
                        percentage_assigned = (user_task_count_2 / task_count_5) * 100
       
       
        # The percentage of completed tasks assigned to a user
        # Looping through all usernames in dictionary
            for username in read_user_file("user.txt").keys():
            # Creating counters
                task_count_6 = 0
                user_task_count_3 = 0
                with open("tasks.txt", "r") as tasks_read:
                    read_tasks = tasks_read.readlines()
            # Loop through each task
                    for line in read_tasks:
                        task_detail = line.strip().split(", ")
            # Incrementing counter if the task is assigned to the user
                        if task_detail[0] == username:
                            task_count_6 += 1
            # Checking if the task is completed
                            if task_detail[-1] == "Yes":
                                user_task_count_3 += 1
            # Checking if user has tasks
                    if task_count_6 == 0:
                        percentage_assigned_to_user = 0
                    else:
            # Calculating the percentage of tasks assigned to the user
                        percentage_assigned_to_user = (user_task_count_3 / task_count_6) * 100
      
      
        # The percentage of tasks assigned to a user that are incomplete
        # Looping through all usernames in dictionary
            for username in read_user_file("user.txt").keys():
            # Creating counters
                user_task_count_4 = 0
                task_count_7 = 0
                
                with open("tasks.txt", "r") as tasks_read:
                    read_tasks = tasks_read.readlines()
                    for line in read_tasks:
                        task_detail = line.strip().split(", ")
            # Check if the task is assigned to the user and is incomplete
                        if task_detail[0] == username: 
                            task_count_7 += 1
                            if task_detail[-1] == "No":
                                user_task_count_4 += 1
            # Checking if user has tasks   
                    if user_task_count_4 == 0: 
                        percentage_assigned_to_user = 0
                    else:
            # Calculating the percentage of tasks assigned to the user that are incomplete
                        percentage_assigned_to_user = (user_task_count_4 / task_count_7) * 100
                    
                    
        # The percentage of tasks assigned to a user that are incomplete and overdue
            for username in read_user_file("user.txt").keys():
            # Creating counters
                user_task_count_5 = 0
                user_incomplete_count = 0
                with open("tasks.txt", "r") as tasks_read:
                    read_tasks = tasks_read.readlines()
                    for line in read_tasks:
                        task_detail = line.strip().split(", ")
            # Checking if the task is assigned to the user and incrementing counter
                        if task_detail[0] == username:
                            user_task_count_5 += 1
            # Checkikng if the task is incomplete and incrementing counter
                            if task_detail[-1] == "No":
                                user_incomplete_count += 1
            # Checking if task is overdue 
                                due_date = datetime.strptime(task_detail[-2], '%d %b %Y')
                                if due_date < datetime.now():
                                    user_incomplete_count -= 1
            # Checking if user has tasks    
                    if user_task_count_5 == 0:
                        percentage_assigned_to_user = 0
                    else:
            # Calculating the percentage of tasks assigned to the user that are both incomplete and overdue
                        percentage_assigned_to_user = (user_incomplete_count / user_task_count_5) * 100


        # Writing data to file
            with open("user_overview.txt", "a") as user_over:
                user_over.write(f"Total Number Of Users: {user_count}\n")
                user_over.write(f"Total Number Of Tasks: {task_count_4}\n")
                user_over.write(f"Total number of tasks for {username}: {user_task_count}\n")
                user_over.write(f"Percentage of tasks assigned to {username}: {percentage_assigned:.2f}%\n")      
                user_over.write(f"Percentage of tasks completed by {username}: {percentage_assigned_to_user:.2f}%\n")
                user_over.write(f"Percentage of tasks assigned to {username} that are incomplete: {percentage_assigned_to_user:.2f}%\n")
                user_over.write(f"Percentage of tasks assigned to {username} that are incomplete and overdue : {percentage_assigned_to_user:.2f}%\n")
            
            print("✦ Text file 'user_overview.txt' has been generated ✅")    
                
# Creating menu option for admin to display statistics
    elif menu == 'ds':
        pass
        if is_admin:
            print(f"         ╔═══════════════════════════╗ ")
            print(f"═════════   STATISTICS (Admin Only)   ═════════")
            print(f"         ╚═══════════════════════════╝ \n")
            print(f"\n\033[0;33m------------------[Task_Overview.txt]------------------\n\n")
        # Displaying statistics from task_overview.txt    
            with open("task_overview.txt", "r") as task_file:
                tasks_view = task_file.readlines()
                print(f"+ {'+ '.join(tasks_view)}")
        # Displaying statistics from user_overview.txt         
            print(f"\n------------------[User_Overview.txt]------------------\n\n")
            with open("user_overview.txt", "r") as user_file:
                user_view = user_file.readlines()
                print(f"+ {'+ '.join(user_view)}")
        continue
    
    
# Creating menu option "exit"
    elif menu == 'e':
        print(f"         ╔═══════════════════════════╗ ")
        print(f"═════════        GOODBYE >{user_n}<      ═════════")
        print(f"         ╚═══════════════════════════╝ \n")
        exit()


# Displaying error message if user inputs invalid option
    else:
        print(pattern)
        print("✘ Invalid Option, Please Try Again")
        print(pattern)