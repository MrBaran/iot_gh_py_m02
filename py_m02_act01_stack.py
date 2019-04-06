''' IoT Greenhouse - Module 2: Activity 01
    Example stack and queue
    Keith E. Kelly
    K2 Creatives, LLC
'''

command_list = ["#stop","#help","#temp","#open","#close","#fan-on","#fan-off","#lamp-on","#lamp-off","#beep"]

command = None
user_commands = []
while command != "#stop":
    #input
    print()
    user_input = input("Please enter an command: ")
    user_input = user_input.strip()
    user_input = user_input.lower()
    if user_input in command_list:
       command = user_input
       print("New command entered:",command)
       user_commands.append(command)
       print("Command added to user command list. Count is:", len(user_commands))
    else:
       print("Invalid command.")
    #process
    print()
    print("Should I process a user command?")
    user_input = input("Enter Y or N: ")
    user_input = user_input.strip()
    user_input = user_input.upper()
    user_input = user_input[0]
    if user_input == "Y" and len(user_commands) > 0:
       command_to_process = user_commands.pop()
       print(command_to_process)
    print("Command processed. Count is:", len(user_commands))
    