path = r"C:\Users\Abder\Desktop\Python assignments\projectpath\dictdump2.txt"

wish_to_keep = "Y"
user_dict = {}
my_rev_dict = {}


while wish_to_keep == "Y":
    user_input = input("What keys and values do you wish to add to the dictionary. Use ';'(Semicolon) to split them respectfully")
    temp_user_input = user_input.split(";")
    user_dict[temp_user_input[0]]=temp_user_input[1]
    wish_to_keep = input("Do you wish to continue? Y/N. Note! You can also save the file by typing 'save' or save as revert with 'saverevert'").capitalize()
    if wish_to_keep == "Revert":
        for k, v in user_dict.items():
            my_rev_dict[v] = k
        print(my_rev_dict)
    elif wish_to_keep == "N":
        print(user_dict)
    elif wish_to_keep == "Saverevert":
        with open(file=path, mode="w") as dictdump2:
            for key, value in user_dict.items():
                dictdump2.write("{};{}\n".format(value, key))
    elif wish_to_keep == "Save":
        with open(file=path, mode="w") as dictdump2:
            for key, value in user_dict.items():
                dictdump2.write("{};{}\n".format(key, value))
else:
    print("We done here :D")
