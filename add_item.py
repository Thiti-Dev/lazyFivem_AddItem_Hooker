#! /usr/bin/python3

# print("-------- Starting to read the file --------")
# days_file = open("file.lua", 'r')
# x = days_file.read()
# print(x)

# print("-------- Find the line --------")

# numb = input('Input Line: ')
# with open('file.lua') as f:
#     content = f.readlines()

# matching_line = [x for x in range(len(content)) if numb in content[x].lower()]

# target = "AWK.itemData['MAT-metalOre'] = {{nl}{tb}prop_name='ng_proc_binbag_01a',{nl}{tb}translatedName='แร่เหล็ก',{nl}{tb}rotx=120.0,{nl}{tb}roty=300.0,{nl}{tb}rotz=150.0,{nl}{tb}offsetz=-1.00\n"

# target_string = '\ttest\n'


# with open("file.lua", "r") as in_file:
#     buf = in_file.readlines()

# with open("file.lua", "w", newline='', encoding="utf-8") as out_file:
#     for line in buf:
#         if line == "--Add Here\n":
#             line = line + target
#         out_file.write(line)


# Defines
item_type = ''
while True:
    choice = int(
        input('Enter type of item : [1]:Tool , [2]:Material, [3]:Weapon , [4]:Food , [5]:Custom : '))
    if choice == 1:
        item_type = 'TOOL-'
        break
    elif choice == 2:
        item_type = 'MAT-'
        break
    elif choice == 3:
        item_type = 'WEAPON-'
        break
    elif choice == 4:
        item_type = 'FOOD-'
        break
    elif choice == 5:
        item_type = ''
        break


item_name = input('Please enter the item name : ')
translated_name = input('Please enter the thai name : ')
prop_name = input('Please enter the prop name (empty for binbag) : ')
if prop_name == '':
    prop_name = 'ng_proc_binbag_01a'  # Binbag
while True:
    try:
        rotx, roty, rotz = input("Enter [rotx] [roty] [rotz] : ").split()
        break
    except ValueError:
        pass

    print("Enter the value correctly please")

# Finalize
final_name = item_type+item_name
item_rotx = float(rotx)
item_roty = float(roty)
item_rotz = float(rotz)

print("---------- CHECKING ----------")
print("ITEM : " + final_name + " THAI_NAME : " + translated_name)
print("prop_name : ", prop_name)
print("rotx = ", item_rotx)
print("roty = ", item_roty)
print("rotz = ", item_rotz)
print("--------- CONFIRM ----------")
confirm = input("[Y]es or [N]o  : (y,n) => ")
if confirm == 'y':
    # Adding Phase => base_inventory
    inv_path = '../awoken_base/items_config.lua'
    nl = '\n'
    tb = '\t'
    inv_target = f"{nl}AWK.itemData['{final_name}'] = {{{nl}{tb}prop_name='{prop_name}',{nl}{tb}translatedName='{translated_name}', {nl}{tb}rotx = {item_rotx}, {nl}{tb}roty = {item_roty}, {nl}{tb}rotz = {item_rotz}, {nl}{tb}offsetz = -1.00{nl}}}{nl}"
    #inv_target = f"asd = {item_rotx}"
    with open(inv_path, "r", encoding="utf-8") as in_file:
        buf = in_file.readlines()

    with open(inv_path, "w", newline='', encoding="utf-8") as out_file:
        for line in buf:
            if "--38E479865" in line:
                line = line + inv_target
            out_file.write(line)

    # js_conf_path = '../awoken_inventory/html/config.js'
    # js_conf_target = f"{nl}itemsData['{final_name}'] = {{ translatedName: '{translated_name}', pngFileName: '{item_name}.png' }};{nl}"

    # with open(js_conf_path, "r", encoding="utf-8") as in_file:
    #     buf = in_file.readlines()

    # with open(js_conf_path, "w", newline='', encoding="utf-8") as out_file:
    #     for line in buf:
    #         if "//38E479865" in line:
    #             line = line + js_conf_target
    #         out_file.write(line)

    inv_resource_path = '../awoken_inventory/__resource.lua'
    inv_resource_target = f'{nl}{tb}"html/img/{item_name}.png",{nl}'
    with open(inv_resource_path, "r", encoding="utf-8") as in_file:
        buf = in_file.readlines()

    with open(inv_resource_path, "w", newline='', encoding="utf-8") as out_file:
        for line in buf:
            if "--38E479865" in line:
                line = line + inv_resource_target
            out_file.write(line)

    final_exit = input("Added successfully [ Press Enter To Exit ]")
