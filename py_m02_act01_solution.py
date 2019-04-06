''' IoT Greenhouse - Module 2: Activity 01
    Investigate lists
    Keith E. Kelly
    K2 Creatives, LLC
'''
command_list = ["#stop","#help","#temp","#open","#close","#fan-on","#fan-off","#lamp-on","#lamp-off","#beep"]

# print(command_list)
# #add item to list
# print("List length 1 =", len(command_list))
# command_list.append("#about")
# print("List length 2 =", len(command_list))
# #remove item
# command_list.remove("#about")
# print("List length 3 =", len(command_list))

# # iterate list
# for i in range(0, len(command_list)):
#     print(command_list[i])
#     #print("item %d: %s" % (i,command_list[i]))
#     #print("item {0}: {1}".format(i,command_list[i]))

# for command in command_list:
#     print(command)

command = None
while command != "#stop":
    print()
    user_input = input("Please enter an command: ")
    user_input = user_input.strip()
    user_input = user_input.lower()
   
    # found = False
    # for command in command_list:
    #    if user_input == command:
    #        found = True
    #        break
    # if found:
    #    print("Your command is ", command)
    # else:
    #    print("Invalid command.")
    if user_input in command_list:
       command = user_input
       print(command)
    else:
       print("Invalid command.")
       
       