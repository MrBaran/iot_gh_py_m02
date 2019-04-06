''' IoT Greenhouse - Module 2: Activity 01
    Parsing a text message using list methods and features
    Keith E. Kelly
    K2 Creatives, LLC
'''
command_list = ["#stop","#help","#temp","#open","#close","#fan-on","#fan-off","#lamp-on","#lamp-off","#beep"]

#user enters gh bot id and a list of commands
#example: @gh01 #beep #open #fan-on

user_message = None
user_commands = []
command_to_process = None
while command_to_process != "#stop":
    #input
    print()
    user_message = input("Enter a bot message. ")
    user_message = user_message.strip()
    user_message = user_message.lower()

    if len(user_message) == 0:
        pass    #no message to process
    else:
        user_values = user_message.split(" ")
        BOT_NAME = "@gh01"
        if len(user_values) > 0:
            bot_name = user_values[0]       #bot name must be first
            if bot_name[0] != "@":
                print("Invalid message. Bot name must be provided first.")
            elif bot_name != BOT_NAME:
                print("This is not my message.")
            else:    
                #use slices to extract command values
                new_commands = user_values[1:]
                #print(new_commands)
                for cmd in new_commands:
                    if cmd in command_list:
                        print("New command entered:",cmd)
                        user_commands.insert(0, cmd)
                    else:
                        print("Sorry. Love to chat, but I only accept commands.")

    #process
    print("Should I process a user command?")
    user_message = input("Enter Y or N: ")
    user_message = user_message.strip()
    user_message = user_message.upper()
    user_message = user_message[0]
    if user_message == "Y" and len(user_commands) > 0:
        command_to_process = user_commands.pop()
        print(command_to_process)
    print("Command processed. Count is:", len(user_commands))