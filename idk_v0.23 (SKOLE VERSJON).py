import msvcrt, time, random

def c_input(c): # clear_input
    while msvcrt.kbhit():
        msvcrt.getwch()
    
    return input(c)

########################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################

# FIX LIST AND OTHER
# Let the player chose when to leave the basement after getting the offer.
# After rps with nello, describe the room a little better.
# Remember def <name>_talk when you talk to someone in a room, and that it checks <name>_current_room for what room you are in.
# Should the roof really be its own room? maybe there will be a item to use up there, or a way to escape?
# Make a few tips somewhere, to make it easier to understand how the game works?
# <name>_rizz_points?
# forandre på så snakke med folk i rom alltid har samme options, (drepe feks) med noen options som passer rommet kanskje? Eller skal det bare gå hvis de er en follower?
# Climb ut the window to get to the roof?
# Mouse in the attic (and maybe other places, for example dining room.)
# Killing will have a random dialoge of what happends. (3 different ways can happen?)
# Remove dining_room_floor1?
# 1% Chance when phone the galactic alphabet.

# current_room = 'parlor_floor1'
# if linnia_current_room != 'parlor_floor1' and linnia_alive == True:
#     linnia_random_current_room()

# (EERIE CAN MOVE ROOM EVEN IF YOU WANT INTO THE ROOM THEY ARE IN, and maybe with a higher chance to move room? Maybe they cant roll the room they currently are on?)



# CHARACTERS AND THEIR STATS
nello_name = '\033[30m???'
linnia_name = '\033[35m???'
silf_name = '\033[36m???'
valtura_name = '\033[32m???'
program_name = '\033[34m???'
man_name = '\033[31m???'

nello_alive = True
linnia_alive = True
silf_alive = True
valtura_alive = True
leaf_alive = True
eerie_alive = True
program_alive = True
man_alive = True

linnia_current_room = 'Nowhere'
silf_current_room = 'Nowhere'
valtura_current_room = 'Nowhere'
leaf_current_room = 'Nowhere'
eerie_current_room = 'Nowhere'

talk_attack_linnia_scared = False


# PLAYER
current_room = None # Players current room
follower = None # if follower == '<name>':


# INVENTORY
inventory_flower = 0
inventory_knife = 0
inventory_revolver = 0
inventory_basement_key = 0
inventory_spellbook = 0


# Other
talk_attacked = None # the current person getting attacked by the player.
basement_key_holder = 'linnia'


# ROOMS   (ft = first time. Describes the room, which automaticly happends on the first time entering a room. This also reveales the room name.)
ft_storage_room_floor0 = True
name_storage_room_floor0 = '???'

ft_parlor_floor1 = True
name_parlor_floor1 = '???'
ft_garden_floor1 = True
name_garden_floor1 = '???'
ft_kitchen_floor1 = True
name_kitchen_floor1 = '???'
ft_dining_room_floor1 = True
name_dining_room_floor1 = '???'
ft_valtura_room_floor1 = 's1'
name_valtura_room_floor1 = '???'
ft_bathroom_floor1 = True
name_bathroom_floor1 = '???'
ft_door_floor1 = True
name_door_floor1 = '???'

ft_balcony_floor2 = True
name_balcony_floor2 = '???'
ft_linnia_room_floor2 = True
name_linnia_room_floor2 = '???'
ft_silf_room_floor2 = True
name_silf_room_floor2 = '???'
ft_bathroom_floor2 = True
name_bathroom_floor2 = '???'
ft_office_floor2 = True
name_office_floor2 = '???'

ft_attic_floor3 = True
name_attic_floor3 = '???'


# STAGES (s1 = stage 1)
# Intro basement
basement_nello_whoareyou = 's1'
basement_nello_wherearewe = 's1'
basement_window = 's1'
basement_door = 's1'
basement_flower = 's1'
basement_girl = 's1'
basement_girl_whereami = 's1'
basement_girl_tellmemoreaboutyou = 's1'
basement_girl_whydidyouletmeout = 's1'
basement_girl_canyouletoutnello = 's1'
basement_girl_leave = 's1'

# Floor0
nello_floor0_trytoopendoor = 's1'

# Floor1
parlor_floor1_sitdownbyfireplace_choice_examinethefireplace = 's1'
parlor_floor1_sitdownbyfireplace_choice_throwaflowerintothefire = 's1'
parlor_floor1_examinebookshelfs = 's1'
parlor_floor1_gotopiano_follower_none = 's1'
parlor_floor1_gotopiano_follower_linnia = 's1'
parlor_floor1_gotopiano_follower_silf = 's1'

garden_floor1_examinethetree = 's1'
garden_floor1_gotopond  = 's1'
garden_floor1_pickupflower = 's1'
garden_floor1_pickupflower_choice = None # Theres a check for what value this variable has somewhere.
garden_floor1_pickupflower_flowers_amount = 75

door_floor1_openthedoor = 's1'

# Floor2
office_floor2_examinephotosonthewall = 's1'
office_floor2_makeacallonthetelephone_7 = 's1'
office_floor2_makeacallonthetelephone_17 = 's1'

# Floor3


# You aren't planning to change anything in the credits, are you?
def credits():
    time.sleep(2)
    print()
    print("\033[33mCREDITS\033[0m")
    time.sleep(2)
    print()
    print("\033[33mA Game Made By:\033[0m")
    time.sleep(2)
    print("Åsmund Nordal Sørum")
    time.sleep(2)
    print()
    print("\033[33mStory:\033[0m")
    time.sleep(2)
    print("Åsmund Nordal Sørum")
    time.sleep(2)
    print()
    print("\033[33mProgramming:\033[0m")
    time.sleep(2)
    print("Åsmund Nordal Sørum")
    time.sleep(2)
    print()
    print("\033[33mBugs: (If there are any)\033[0m")
    time.sleep(2)
    print("Åsmund Nordal Sørum")
    time.sleep(2)
    print()
    print("\033[33mVisuals:\033[0m")
    time.sleep(2)
    print("Åsmund Nordal Sørum")
    time.sleep(2)
    print("Your Brain")
    time.sleep(2)
    print()
    print("\033[33mCharacter Designs:\033[0m")
    time.sleep(2)
    print("Åsmund Nordal Sørum")
    time.sleep(2)
    print("Your Brain")
    time.sleep(2)
    print()
    print("\033[33mMusic:\033[0m")
    time.sleep(2)
    print("[Not in this version.]")
    time.sleep(2)
    print()
    print("\033[33mPlaytesters:\033[0m")
    time.sleep(2)
    print("Åsmund Nordal Sørum")
    time.sleep(2)
    print()
    print("\033[33mSpecial Thanks:\033[0m")
    time.sleep(2)
    print("Åsmund Nordal Sørum")
    time.sleep(2)
    print("" + program_name + "\033[0m")
    time.sleep(2)
    print("" + name + "\033[0m")



def random_chance_100():
    global random_chance_100_result
    random_chance_100_result = random.randint(1, 100)
    print(f"ADMIN MESSAGE: {random_chance_100_result}")
    return

    

########################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################

# FLOOR STAIRS
def stairs():
    global current_room
    current_room = 'stairs'
    c_input("\033[33m(You are on the stairs.) \033[0m")
    print("\033[33m(What floor do you want to go to?)\033[0m")
    time.sleep(1)
    print("\033[33m[0 = Basement]\033[0m")
    print("\033[33m[1 = First floor]\033[0m")
    print("\033[33m[2 = Second floor]\033[0m")
    stairs_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if stairs_choice == '0':
        basement_floor0()
    elif stairs_choice == '1':
        hall_floor1()
    elif stairs_choice == '2':
        hall_floor2()
    else:
        stairs()



########################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################

# FLOOR 0
def basement_floor0():
    global current_room
    current_room = 'basement_floor0'
    c_input("\033[33m(You are in the basement. [Basement]) \033[0m")
    print("\033[33m(Where do you wanna go?)\033[0m")
    time.sleep(1)
    print("\033[33m[1 = " + name_storage_room_floor0 + "]\033[0m")
    print("\033[33m[2 = " + nello_name + "\033[33m]\033[0m")
    print("\033[33m[0 = Stairs]\033[0m")
    basement_floor0_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)

    if basement_floor0_choice == '1':
        if linnia_current_room != 'storage_room_floor0' and linnia_alive == True and follower != 'linnia':
            linnia_random_current_room()
        if silf_current_room != 'storage_room_floor0' and silf_alive == True and follower != 'silf':
            silf_random_current_room()
        if valtura_current_room != 'storage_room_floor0' and valtura_alive == True:
            valtura_random_current_room()
        if leaf_current_room != 'storage_room_floor0' and leaf_alive == True:
            leaf_random_current_room()
        if eerie_current_room != 'storage_room_floor0' and eerie_alive == True:
            eerie_random_current_room()
        storage_room_floor0()

    elif basement_floor0_choice == '2':
        if linnia_current_room != 'nello_floor0' and linnia_alive == True and follower != 'linnia':
            linnia_random_current_room()
        if silf_current_room != 'nello_floor0' and silf_alive == True and follower != 'silf':
            silf_random_current_room()
        if valtura_current_room != 'nello_floor0' and valtura_alive == True:
            valtura_random_current_room()
        if leaf_current_room != 'nello_floor0' and leaf_alive == True:
            leaf_random_current_room()
        if eerie_current_room != 'nello_floor0' and eerie_alive == True:
            eerie_random_current_room()
        nello_floor0()

    elif basement_floor0_choice == '0':
        stairs()
    else:
        basement_floor0()



def storage_room_floor0():
    global linnia_current_room, silf_current_room, valtura_current_room, leaf_current_room, eerie_current_room # (JUST FOR TESTING(ADMIN)
    global ft_storage_room_floor0
    global name_storage_room_floor0
    global current_room
    current_room = 'storage_room_floor0'
    if ft_storage_room_floor0 == True:
        c_input("\033[33m(You walk into a small room in the basement.) \033[0m")
        c_input("\033[33m(The room is filled with a lot of random stuff, like old christmas decoration and other stuff.) \033[0m")
        c_input("\033[33m(It smells pretty strange in here.) \033[0m")
        c_input("\033[33m(The one light bulb in the ceiling flickers from time to time.) \033[0m")
        if follower == 'linnia':
            print()
            c_input("\033[33m(" + linnia_name + "\033[33m uhh... why are we down here?) \033[0m")
        elif follower == 'silf':
            print()
            c_input("" + silf_name + ": Wow, it's even messier than I remembered. \033[0m")
        name_storage_room_floor0 = 'Storage room'
        print()
        ft_storage_room_floor0 = False
    c_input("\033[33m(You are in the storage room. [Basement]) \033[0m")
    print("\033[33m(What do you wanna do?)\033[0m")
    time.sleep(1)
    print("\033[33m[1 = Check inventory.]\033[0m")
    print("\033[33m[0 = Go back]\033[0m")
    storage_room_floor0_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if storage_room_floor0_choice == '1':
        if inventory_flower == 1:
            c_input(f"\033[33m(You have {inventory_flower} flower.)\033[0m")
        elif inventory_flower > 1:
            c_input(f"\033[33m(You have {inventory_flower} flowers.)\033[0m")
        if inventory_knife == 1:
            c_input(f"\033[33m(You have {inventory_knife} knife.)\033[0m")
        elif inventory_knife > 1:
            c_input(f"\033[33m(You have {inventory_knife} knifes.)\033[0m")
        if inventory_revolver == 1:
            c_input(f"\033[33m(You have {inventory_revolver} revolver.)\033[0m")
        elif inventory_revolver > 1:
            c_input(f"\033[33m(You have {inventory_revolver} revolvers.)\033[0m")
        if inventory_basement_key == 1:
            c_input(f"\033[33m(You have {inventory_basement_key} basement key.)\033[0m")
        elif inventory_basement_key > 1:
            c_input(f"\033[33m(You have {inventory_basement_key} basement keys.)\033[0m")
        if inventory_spellbook == 1:
            c_input(f"\033[33m(You have {inventory_spellbook} spellbook.)\033[0m")
        elif inventory_spellbook > 1:
            c_input(f"\033[33m(You have {inventory_spellbook} spellbooks.)\033[0m")
        if inventory_flower == 0 and inventory_knife == 0 and inventory_revolver == 0:
            c_input("\033[33m(You don't have anything in your inventory.)\033[0m")
        print()
        storage_room_floor0()
    elif storage_room_floor0_choice == '9':
        if linnia_alive == True:
            linnia_random_current_room()
        if silf_alive == True:
            silf_random_current_room()
        if valtura_alive == True:
            valtura_random_current_room()
        if leaf_alive == True:
            leaf_random_current_room()
        if eerie_alive == True:
            eerie_random_current_room()
        print()
        print("Linnia = " + linnia_current_room + "")
        print("Silf = " + silf_current_room + "")
        print("Valtura = " + valtura_current_room + "")
        print("Leaf = " + leaf_current_room + "")
        print("Eerie = " + eerie_current_room + "")
        print()
        storage_room_floor0()

    elif storage_room_floor0_choice == '0':
        basement_floor0()
    else:
        storage_room_floor0()



def nello_floor0():
    global ft_nello_floor0
    global current_room
    current_room = 'nello_floor0'
    if ft_bathroom_floor1 == True:
        c_input("\033[33m(You walk back to " + nello_name + "\033[33m's room.) \033[0m")
        c_input("\033[33m(It's as dusty as last time.) \033[0m")
        if follower == 'linnia':
            print()
            c_input("\033[33m(" + linnia_name + "\033[33m coughs.) \033[0m")
        elif follower == 'silf':
            print()
            c_input("" + silf_name + ": Why are we here? Do you miss your roommate or something? \033[0m")
        print()
        ft_nello_floor0 = False
    c_input("\033[33m(You are outside " + nello_name + "\033[33m's room. [Basement]) \033[0m")
    print("\033[33m(What do you wanna do?)\033[0m")
    time.sleep(1)
    print("\033[33m[1 = Talk with Nello.]\033[0m")
    if inventory_basement_key == 0:
        print("\033[33m[2 = Try to open door.]\033[0m")
    elif inventory_basement_key > 0:
        print("\033[33m[2 = Unlock door using basment key.]\033[0m")
    print("\033[33m[0 = Go back]\033[0m")
    nello_floor0_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if nello_floor0_choice == '1':
        nello_talk()
    if nello_floor0_choice == '2':
        if inventory_basement_key == 0:
            if nello_floor0_trytoopendoor == 's1':
                c_input("\033[33m(You try to open the door.) \033[0m")
                if basement_door == 's2':
                    print()
                    c_input("" + nello_name + ": It's still locked, dumbass. \033[0m")
                else:
                    c_input("\033[33m(The door is locked.) \033[0m")
                    print()
                c_input("" + nello_name + ": You will need the Basement key to open that door. \033[0m")
                nello_floor0_trytoopendoor = 's2'
            elif nello_floor0_trytoopendoor == 's2':
                c_input("\033[33m(You try to open the door again.) \033[0m")
                c_input("\033[33m(Surprisingly, the door is still locked.) \033[0m")
                print()
                c_input("" + nello_name + ": (This kid is actually so stupid.) \033[0m")
                c_input("" + nello_name + ": Like I said, you will need the Basement key to open that door. \033[0m")
                if follower == 'silf':
                    print()
                    c_input("" + silf_name + ": As if we are ever letting him out, right? \033[0m")
            print()
            nello_floor0()
        elif inventory_basement_key > 0:
            c_input("\033[33m(placeholder) \033[0m")
    elif nello_floor0_choice == '0':
        basement_floor0()
    else:
        nello_floor0()

########################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################

# FLOOR 1
def hall_floor1():
    global current_room
    current_room = 'hall_floor1'
    c_input("\033[33m(You are in the hall. [First floor]) \033[0m")
    print("\033[33m(Where do you wanna go?)\033[0m")
    time.sleep(1)
    print("\033[33m[1 = " + name_parlor_floor1 + "]\033[0m")
    print("\033[33m[2 = " + name_garden_floor1 + "]\033[0m")
    print("\033[33m[3 = " + name_kitchen_floor1 + "]\033[0m")
    print("\033[33m[4 = " + name_dining_room_floor1 + "]\033[0m")
    print("\033[33m[5 = " + name_valtura_room_floor1 + "]\033[0m")
    print("\033[33m[6 = " + name_bathroom_floor1 + "]\033[0m")
    print("\033[33m[7 = " + name_door_floor1 + "]\033[0m")
    print("\033[33m[0 = Stairs]\033[0m")
    hall_floor1_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if hall_floor1_choice == '1':
        if linnia_current_room != 'parlor_floor1' and linnia_alive == True and follower != 'linnia':
            linnia_random_current_room()
        if silf_current_room != 'parlor_floor1' and silf_alive == True and follower != 'silf':
            silf_random_current_room()
        if valtura_current_room != 'parlor_floor1' and valtura_alive == True:
            valtura_random_current_room()
        if leaf_current_room != 'parlor_floor1' and leaf_alive == True:
            leaf_random_current_room()
        if eerie_current_room != 'parlor_floor1' and eerie_alive == True:
            eerie_random_current_room()
        parlor_floor1()

    elif hall_floor1_choice == '2':
        if linnia_current_room != 'garden_floor1' and linnia_alive == True and follower != 'linnia':
            linnia_random_current_room()
        if silf_current_room != 'garden_floor1' and silf_alive == True and follower != 'silf':
            silf_random_current_room()
        if valtura_current_room != 'garden_floor1' and valtura_alive == True:
            valtura_random_current_room()
        if leaf_current_room != 'garden_floor1' and leaf_alive == True:
            leaf_random_current_room()
        if eerie_current_room != 'garden_floor1' and eerie_alive == True:
            eerie_random_current_room()
        garden_floor1()

    elif hall_floor1_choice == '3':
        if linnia_current_room != 'kitchen_floor1' and linnia_alive == True and follower != 'linnia':
            linnia_random_current_room()
        if silf_current_room != 'kitchen_floor1' and silf_alive == True and follower != 'silf':
            silf_random_current_room()
        if valtura_current_room != 'kitchen_floor1' and valtura_alive == True:
            valtura_random_current_room()
        if leaf_current_room != 'kitchen_floor1' and leaf_alive == True:
            leaf_random_current_room()
        if eerie_current_room != 'kitchen_floor1' and eerie_alive == True:
            eerie_random_current_room()
        kitchen_floor1()

    elif hall_floor1_choice == '4':
        if linnia_current_room != 'dining_room_floor1' and linnia_alive == True and follower != 'linnia':
            linnia_random_current_room()
        if silf_current_room != 'dining_room_floor1' and silf_alive == True and follower != 'silf':
            silf_random_current_room()
        if valtura_current_room != 'dining_room_floor1' and valtura_alive == True:
            valtura_random_current_room()
        if leaf_current_room != 'dining_room_floor1' and leaf_alive == True:
            leaf_random_current_room()
        if eerie_current_room != 'dining_room_floor1' and eerie_alive == True:
            eerie_random_current_room()
        dining_room_floor1()

    elif hall_floor1_choice == '5':
        if linnia_current_room != 'valtura_room_floor1' and linnia_alive == True and follower != 'linnia':
            linnia_random_current_room()
        if silf_current_room != 'valtura_room_floor1' and silf_alive == True and follower != 'silf':
            silf_random_current_room()
        if valtura_current_room != 'valtura_room_floor1' and valtura_alive == True:
            valtura_random_current_room()
        if leaf_current_room != 'valtura_room_floor1' and leaf_alive == True:
            leaf_random_current_room()
        if eerie_current_room != 'valtura_room_floor1' and eerie_alive == True:
            eerie_random_current_room()
        valtura_room_floor1()

    elif hall_floor1_choice == '6':
        if linnia_current_room != 'bathroom_floor1' and linnia_alive == True and follower != 'linnia':
            linnia_random_current_room()
        if silf_current_room != 'bathroom_floor1' and silf_alive == True and follower != 'silf':
            silf_random_current_room()
        if valtura_current_room != 'bathroom_floor1' and valtura_alive == True:
            valtura_random_current_room()
        if leaf_current_room != 'bathroom_floor1' and leaf_alive == True:
            leaf_random_current_room()
        if eerie_current_room != 'bathroom_floor1' and eerie_alive == True:
            eerie_random_current_room()
        bathroom_floor1()

    elif hall_floor1_choice == '7':
        if linnia_current_room != 'door_floor1' and linnia_alive == True and follower != 'linnia':
            linnia_random_current_room()
        if silf_current_room != 'door_floor1' and silf_alive == True and follower != 'silf':
            silf_random_current_room()
        if valtura_current_room != 'door_floor1' and valtura_alive == True:
            valtura_random_current_room()
        if leaf_current_room != 'door_floor1' and leaf_alive == True:
            leaf_random_current_room()
        if eerie_current_room != 'door_floor1' and eerie_alive == True:
            eerie_random_current_room()
        door_floor1()

    elif hall_floor1_choice == '0':
        stairs()
    else:
        hall_floor1()



def parlor_floor1():
    global ft_parlor_floor1
    global name_parlor_floor1
    global parlor_floor1_sitdownbyfireplace_choice_examinethefireplace
    global parlor_floor1_sitdownbyfireplace_choice_throwaflowerintothefire
    global parlor_floor1_examinebookshelfs
    global inventory_flower
    global garden_floor1_pickupflower_choice
    global parlor_floor1_gotopiano_follower_none, parlor_floor1_gotopiano_follower_linnia, parlor_floor1_gotopiano_follower_silf
    global current_room
    current_room = 'parlor_floor1'

    if ft_parlor_floor1 == True:
        c_input("\033[33m(You walk into a cozy room.) \033[0m")
        c_input("\033[33m(There is a small table in the middle of the room with comfy looking chairs around it.) \033[0m")
        c_input("\033[33m(The carpet has a cool and unique design.) \033[0m")
        c_input("\033[33m(A few bookshelfs are on the sides of the room.) \033[0m")
        c_input("\033[33m(There is a piano in the corner.) \033[0m")
        c_input("\033[33m(There's also a fireplace.) \033[0m")
        c_input("\033[33m(It looks like a living room.) \033[0m")
        print()
        if follower == 'linnia':
            print()
            c_input("" + linnia_name + ": My mom has has her friends over sometimes. \033[0m")
            c_input("" + linnia_name + ": They always sit here talking while drinking tea. \033[0m")
            c_input("" + linnia_name + ": It always disturbs my reading... \033[0m")
        elif follower == 'silf':
            print()
            c_input("" + silf_name + ": I often trown flowers into the fireplace when I'm bored. \033[0m")
        name_parlor_floor1 = 'Parlor'
        print()
        ft_parlor_floor1 = False
    c_input("\033[33m(You are in the parlor. [First floor]) \033[0m")
    print("\033[33m(What do you wanna do?)\033[0m")
    time.sleep(1)
    print("\033[33m[1 = Sit down by fireplace.]\033[0m")
    print("\033[33m[2 = Examine bookshelfs.]\033[0m")
    print("\033[33m[3 = Go to piano.]\033[0m")
    print("\033[33m[0 = Go back]\033[0m")
    parlor_floor1_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)

    if parlor_floor1_choice == '1':
        c_input("\033[33m(You sit down by the fireplace.) \033[0m")
        c_input("\033[33m(You feel its heat.) \033[0m")
        c_input("\033[33m(You feel comfortable.) \033[0m")
        c_input("\033[33m(" + linnia_name + "\033[33m sits down beside you.) \033[0m")
        print()
        c_input("" + linnia_name + ": This is my second favorite reading place. \033[0m")
        c_input("" + linnia_name + ": After under the tree in the garden of course! \033[0m")
        time.sleep(1)
        while True:
            parlor_floor1_sitdownbyfireplace_option_flower = None
            parlor_floor1_sitdownbyfireplace_options = 1
            print("\033[33m[1 = Examine the fireplace.]\033[0m")
            if inventory_flower > 0:
                parlor_floor1_sitdownbyfireplace_options += 1
                print(f"\033[33m[{parlor_floor1_sitdownbyfireplace_options} = Throw a flower into the fire.]\033[0m")
                parlor_floor1_sitdownbyfireplace_option_flower = parlor_floor1_sitdownbyfireplace_options
            print("\033[33m[0 = Go back]\033[0m")
            parlor_floor1_sitdownbyfireplace_choice = c_input("\033[33mAnswer: \033[0m")
            print()
            time.sleep(1)
            if parlor_floor1_sitdownbyfireplace_choice == '1':
                if parlor_floor1_sitdownbyfireplace_choice_examinethefireplace == 's1':
                    c_input("\033[33m(It's a fireplace.) \033[0m")
                    c_input("\033[33m(A warm feeling fills you.) \033[0m")
                    c_input("\033[33m(The fire glows bright.) \033[0m")
                    parlor_floor1_sitdownbyfireplace_choice_examinethefireplace = 's2'
                elif parlor_floor1_sitdownbyfireplace_choice_examinethefireplace == 's2':
                    c_input("\033[33m(It's still a fireplace.) \033[0m")
                    c_input("\033[33m(A warm feeling fills you.) \033[0m")
                    c_input("\033[33m(The fire glows bright.) \033[0m")
                print()
                continue
            elif parlor_floor1_sitdownbyfireplace_choice == str(parlor_floor1_sitdownbyfireplace_option_flower) and parlor_floor1_sitdownbyfireplace_option_flower is not None:
                inventory_flower -= 1
                if parlor_floor1_sitdownbyfireplace_choice_throwaflowerintothefire == 's1':
                    c_input("\033[33m(You throw a flower into the fire.) \033[0m")
                    c_input("\033[33m(It catches fire immediately.) \033[0m")
                    c_input("\033[33m(You see it turning into ash and embers.) \033[0m")
                    print()
                    c_input("" + linnia_name + ": (Why did they do that?) \033[0m")
                    parlor_floor1_sitdownbyfireplace_choice_throwaflowerintothefire = 's2'
                elif parlor_floor1_sitdownbyfireplace_choice_throwaflowerintothefire == 's2':
                    c_input("\033[33m(You throw another flower into the fire.) \033[0m")
                    c_input("\033[33m(Something about the flower burning is really enjoyable.) \033[0m")
                    print()
                    c_input("" + linnia_name + ": (...) \033[0m")
                    if garden_floor1_pickupflower_choice == '1':
                        c_input("" + linnia_name + ": (I would gladly take another flower...) \033[0m")
                    else:
                        c_input("" + linnia_name + ": (I would gladly take a flower...) \033[0m")
                    parlor_floor1_sitdownbyfireplace_choice_throwaflowerintothefire = 's3'
                elif parlor_floor1_sitdownbyfireplace_choice_throwaflowerintothefire == 's3':
                    c_input("\033[33m(You throw another flower into the fire.) \033[0m")
                    c_input("\033[33m(Something about the flower burning is really enjoyable.) \033[0m")
                    print()
                    c_input("" + linnia_name + ": (...) \033[0m")
                print()
                continue
            elif parlor_floor1_sitdownbyfireplace_choice == '0':
                break
            else:
                continue
        print()
        parlor_floor1()

    elif parlor_floor1_choice == '2':
        if parlor_floor1_examinebookshelfs == 's1':
            c_input("\033[33m(You walk to one of the bookshelfs.) \033[0m")
            c_input("\033[33m(There's a lot of different books.) \033[0m")
            print()
            c_input("" + linnia_name + ": My favorite books are up in my room. \033[0m")
            c_input("" + linnia_name + ": (If they're even interested in books.) \033[0m")
            while True:
                c_input("" + linnia_name + ": Are you interested in books? \033[0m")
                time.sleep(1)
                print("\033[33m[1 = Yes!]\033[0m")
                print("\033[33m[2 = A little.]\033[0m")
                print("\033[33m[3 = Not really...]\033[0m")
                print("\033[33m[4 = I hate books.]\033[0m")
                parlor_floor1_examinebookshelfs_choice = c_input("\033[33mAnswer: \033[0m")
                print()
                time.sleep(1)
                if parlor_floor1_examinebookshelfs_choice == '1':
                    c_input("" + linnia_name + ": That's so cool! \033[0m")
                    c_input("" + linnia_name + ": I should definitively show you my favorite books sometime! \033[0m")
                    c_input("" + linnia_name + ": Maybe you might recognize some of them? \033[0m")
                elif parlor_floor1_examinebookshelfs_choice == '2':
                    c_input("" + linnia_name + ": Well, it's something at least! \033[0m")
                    c_input("" + linnia_name + ": I could show my favorite ones up in my room later, if you would like to. \033[0m")
                elif parlor_floor1_examinebookshelfs_choice == '3':
                    c_input("" + linnia_name + ": That's fine. \033[0m")
                    c_input("" + linnia_name + ": It's not for everyone. \033[0m")
                elif parlor_floor1_examinebookshelfs_choice == '4':
                    c_input("" + linnia_name + ": Oh... \033[0m")
                    c_input("" + linnia_name + ": Well, reading is not for everyone, I guess. \033[0m")
                else:
                    continue
                parlor_floor1_examinebookshelfs = 's2'
                break
        elif parlor_floor1_examinebookshelfs == 's2':
            c_input("\033[33m(You walk to the bookshelfs again.) \033[0m")
            c_input('\033[33m(A book named "Dusk After Dawn" catches your eye.) \033[0m')
            c_input("\033[33m(You take the book out of the bookshelf.) \033[0m")
            c_input("\033[33m(You open to a random page.) \033[0m")
            c_input("\033[33m(The language is not written in english, so you don't understand what is says.) \033[0m")
            print()
            c_input("" + linnia_name + ": Did that book catch your eye? \033[0m")
            c_input("" + linnia_name + ": The story is pretty interesting. \033[0m")
            c_input("" + linnia_name + ": But to be honest, It wasn't really for me. \033[0m")
            print()
            c_input("\033[33m(You put the book back into the bookshelf.) \033[0m")
            parlor_floor1_examinebookshelfs = 's3'
        elif parlor_floor1_examinebookshelfs == 's3':
            c_input("\033[33m(There aren't any books that catches your interest.) \033[0m")
        print()
        parlor_floor1()

    elif parlor_floor1_choice == '3':
        if follower == None:
            if parlor_floor1_gotopiano_follower_none == 's1':
                c_input("\033[33m(You walk over to the piano in the corner.) \033[0m")
                c_input("\033[33m(It's pretty dusty.) \033[0m")
                c_input("\033[33m(You press down a note on the piano.) \033[0m")
                c_input("\033[33m(It makes a sound.) \033[0m")
                c_input("\033[33m(You are absolutely flabbergasted over this discovery.) \033[0m")
                parlor_floor1_gotopiano_follower_none = 's2'
            elif parlor_floor1_gotopiano_follower_none == 's2':
                c_input("\033[33m(You walk over to the piano in the corner.) \033[0m")
                c_input("\033[33m(You press down another note on the piano.) \033[0m")
                c_input("\033[33m(It made a sound again, but a different one!) \033[0m")
                c_input("\033[33m(You are even more flabbergasted.) \033[0m")
                parlor_floor1_gotopiano_follower_none = 's3'
            elif parlor_floor1_gotopiano_follower_none == 's3':
                c_input("\033[33m(You walk over to the piano in the corner.) \033[0m")
                c_input("\033[33m(You try to press down another note,) \033[0m")
                c_input("\033[33m(but there's too many options.) \033[0m")
                c_input("\033[33m(You end up not pressing any of the notes, because you don't know which one to press.) \033[0m")
                parlor_floor1_gotopiano_follower_none = 's4'
            elif parlor_floor1_gotopiano_follower_none == 's4':
                c_input("\033[33m(You walk over to the piano in the corner.) \033[0m")
                c_input("\033[33m(The amount of notes overwhelm you.) \033[0m")
            print()
            parlor_floor1()

        elif follower == 'linnia':
            if parlor_floor1_gotopiano_follower_linnia == 's1':
                c_input("\033[33m(You walk over to the piano in the corner.) \033[0m")
                print()
                c_input("" + linnia_name + ": I wish I could play the piano... \033[0m")
                c_input("" + linnia_name + ": I have tried multiple times to learn it before, \033[0m")
                c_input("" + linnia_name + ": but I fail every time. \033[0m")
                if silf_name == '\033[36m???':
                    c_input("" + linnia_name + ": My brother used to play it a lot, \033[0m")
                elif silf_name == '\033[36mSilf':
                    c_input("" + linnia_name + ": " + silf_name + "\033[35m used to play it a lot. \033[0m")
                c_input("" + linnia_name + ": He was actually pretty good at it. \033[0m")
                while True:
                    c_input("" + linnia_name + ": Wait... can you play the piano? \033[0m")
                    time.sleep(1)
                    print("\033[33m[1 = Yes.]\033[0m")
                    print("\033[33m[2 = No.]\033[0m")
                    parlor_floor1_gotopiano_follower_linnia_choice = c_input("\033[33mAnswer: \033[0m")
                    print()
                    time.sleep(1)
                    if parlor_floor1_gotopiano_follower_linnia_choice == '1':
                        c_input("" + linnia_name + ": Actually?? \033[0m")
                        c_input("" + linnia_name + ": That's so cool! \033[0m")
                        c_input("" + linnia_name + ": You should teach me how to play it sometime! \033[0m")
                        c_input("" + linnia_name + ": Or... try to teach me atleast... \033[0m")
                        c_input("" + linnia_name + ": (Who am I kidding, after all these tries, It's not like I suddenly gonna figure out how to play it...) \033[0m")
                    elif parlor_floor1_gotopiano_follower_linnia_choice == '2':
                        c_input("" + linnia_name + ": Well... \033[0m")
                        c_input("" + linnia_name + ": You seem like someone who would be good at it... \033[0m")
                    parlor_floor1_gotopiano_follower_linnia = 's2'
                    break
            elif parlor_floor1_gotopiano_follower_linnia == 's2':
                c_input("\033[33m(You walk over to the piano in the corner.) \033[0m")
                print()
                c_input("" + linnia_name + ": You know what, \033[0m")
                c_input("" + linnia_name + ": If I really want to learn the piano, \033[0m")
                c_input("" + linnia_name + ": then I shouldn't give up on learning it. \033[0m")
                c_input("" + linnia_name + ": But not right now, I wouldn't want to torture you. \033[0m")
                print()
                c_input("\033[33m(" + linnia_name + "\033[33m laughs a little for herself.) \033[0m")
                parlor_floor1_gotopiano_follower_linnia = 's3'
            elif parlor_floor1_gotopiano_follower_linnia == 's3':
                c_input("\033[33m(You walk over to the piano in the corner.) \033[0m")
                c_input("\033[33m(It's a piano, that's for sure.) \033[0m")
            print()
            parlor_floor1()

        elif follower == 'silf':
            if parlor_floor1_gotopiano_follower_silf == 's1':
                c_input("\033[33m(You walk over to the piano in the corner.) \033[0m")
                print()
                c_input("" + silf_name + ": Oh, the piano. \033[0m")
                c_input("" + silf_name + ": I actually used to play the piano. \033[0m")
                c_input("" + silf_name + ": You can tell that nobody has played on in a while because of how dusty it is. \033[0m")
                c_input("" + silf_name + ": " + linnia_name + "\033[36m also tried to learn to play it at some point, \033[0m")
                c_input("" + silf_name + ": and she was absolutely terrible at it. \033[0m")
                parlor_floor1_gotopiano_follower_silf = 's2'
            elif parlor_floor1_gotopiano_follower_silf == 's2':
                c_input("\033[33m(You walk over to the piano in the corner.) \033[0m")
                print()
                c_input("" + silf_name + ": Why are we back at the piano? \033[0m")
                c_input("" + silf_name + ": ... \033[0m")
                while True:
                    c_input("" + silf_name + ": You don't want me to play on it, right? \033[0m")
                    time.sleep(1)
                    print("\033[33m[1 = Yes.]\033[0m")
                    print("\033[33m[2 = No.]\033[0m")
                    parlor_floor1_gotopiano_follower_silf_choice = c_input("\033[33mAnswer: \033[0m")
                    print()
                    time.sleep(1)
                    if parlor_floor1_gotopiano_follower_silf_choice == '1':
                        c_input("" + silf_name + ": Uhh, yeah no thanks. \033[0m")
                        c_input("" + silf_name + ": As you know, I haven't played in a while. \033[0m")
                    elif parlor_floor1_gotopiano_follower_silf_choice == '2':
                        c_input("" + silf_name + ": That's probably the best. \033[0m")
                        c_input("" + silf_name + ": As you know, I haven't played in a while. \033[0m")
                    parlor_floor1_gotopiano_follower_silf = 's3'
                    break
            elif parlor_floor1_gotopiano_follower_silf == 's3':
                c_input("\033[33m(You walk over to the piano in the corner.) \033[0m")
                print()
                c_input("" + silf_name + ": (Why are we at the piano again??) \033[0m")
            print()
            parlor_floor1()

    elif parlor_floor1_choice == '0':
        hall_floor1()
    else:
        parlor_floor1()



def garden_floor1():
    global ft_garden_floor1
    global name_garden_floor1
    global garden_floor1_examinethetree
    global garden_floor1_gotopond
    global garden_floor1_pickupflower
    global garden_floor1_pickupflower_choice
    global garden_floor1_pickupflower_flowers_amount
    global inventory_flower
    global current_room
    current_room = 'garden_floor1'
    if ft_garden_floor1 == True:
        c_input("\033[33m(You walk outside behind the building.) \033[0m")
        c_input("\033[33m(The vibrant red nature waving in the wind.) \033[0m")
        c_input("\033[33m(There's multiple different plants and flowers around.) \033[0m")
        c_input("\033[33m(There is also a small pond here, with a few lilypads here and there.) \033[0m")
        c_input("\033[33m(A tree is standing in the middle, with its red leaves shining in the moonlight.) \033[0m")
        if follower == 'linnia':
            c_input("\033[33m(" + linnia_name + "\033[33m is staring up at the moon.) \033[0m")
            print()
            c_input("" + linnia_name + ": Nighttime is probably my favorite time of day. \033[0m")
        elif follower == 'silf':
            print()
            c_input("" + silf_name + ": I feel like nature would maybe look better if it had a different color then red. \033[0m")
            c_input("" + silf_name + ": Like, maybe green or something? \033[0m")
            c_input("" + silf_name + ": Yeah nevermind. \033[0m")
        name_garden_floor1 = 'Garden'
        print()
        ft_garden_floor1 = False
    c_input("\033[33m(You are in the garden. [First floor]) \033[0m")
    print("\033[33m(What do you wanna do?)\033[0m")
    time.sleep(1)
    print("\033[33m[1 = Examine the tree.]\033[0m")
    print("\033[33m[2 = Go to pond.]\033[0m")
    print("\033[33m[3 = Pick up flower.]\033[0m")
    print("\033[33m[0 = Go back]\033[0m")
    garden_floor1_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)

    if garden_floor1_choice == '1':
        if garden_floor1_examinethetree == 's1':
            c_input("\033[33m(You examine the tree.) \033[0m")
            c_input("\033[33m(It's a tree.) \033[0m")
            print()
            c_input("" + linnia_name + ": That tree fills this garden with so much more life. \033[0m")
            c_input("" + linnia_name + ": I used to play with my brother and dad in the garden. \033[0m")
            c_input("" + linnia_name + ": But my dad recently vanished... \033[0m")
            c_input("" + linnia_name + ": He said he was just gonna go for a walk in the forest nearby, \033[0m")
            c_input("" + linnia_name + ": But he hasn't come back... \033[0m")
            garden_floor1_examinethetree = 's2'
        elif garden_floor1_examinethetree == 's2':
            c_input("\033[33m(You examine the tree again.) \033[0m")
            c_input("\033[33m(It's still a tree.) \033[0m")
            print()
            c_input("" + linnia_name + ": I often sit under it while reading a book. \033[0m")
            c_input("" + linnia_name + ": It's kinda my comfort place... \033[0m")
            garden_floor1_examinethetree = 's3'
        elif garden_floor1_examinethetree == 's3':
            c_input("\033[33m(Well, it's still just a tree.) \033[0m")
        print()
        garden_floor1()
    
    elif garden_floor1_choice == '2':
        if garden_floor1_gotopond == 's1':
            c_input("\033[33m(You sit down by the pond and look into it.) \033[0m")
            print()
            c_input("" + linnia_name + ": If you look closely, you can see a few fish swimming around. \033[0m")
            c_input("" + linnia_name + ": We used to have more fish, but my cat ate them. \033[0m")
            c_input("" + linnia_name + ": I have trained him to not eat them anymore, so the rest should be safe. \033[0m")
            garden_floor1_gotopond = 's2'
        elif garden_floor1_gotopond == 's2':
            c_input("\033[33m(You sit down by the pond with " + linnia_name + "\033[33m again.) \033[0m")
            print()
            c_input("" + linnia_name + ": I really like the garden. It's so peaceful, especially at this time of day. \033[0m")
            garden_floor1_gotopond = 's3'
        elif garden_floor1_gotopond == 's3':
            c_input("\033[33m(The moonlight is glowing of the pond.) \033[0m")
        print()
        garden_floor1()

    elif garden_floor1_choice == '3':
        if garden_floor1_pickupflower == 's1':
            c_input("\033[33m(You pick up a flower from the garden.) \033[0m")
            garden_floor1_pickupflower_flowers_amount -= 1
            c_input("\033[33m(You turn around with the flower in your hand and meet eyes with " + linnia_name + "\033[33m.) \033[0m")
            print()
            c_input("" + linnia_name + ": Uhm... \033[0m")
            print()
            c_input("\033[33m(" + linnia_name + "\033[33m looks down at the flower and blushes.) \033[0m")
            time.sleep(1)
            while True:
                print("\033[33m[1 = Give flower to " + linnia_name + "\033[33m.]\033[0m")
                print("\033[33m[2 = Keep the flower.]\033[0m")
                garden_floor1_pickupflower_choice = c_input("\033[33mAnswer: \033[0m")
                print()
                time.sleep(1)
        
                if garden_floor1_pickupflower_choice == '1':
                    c_input("\033[33m(You offer the flower to " + linnia_name + "\033[33m.) \033[0m")
                    print()
                    c_input("" + linnia_name + ": (WHAT.) \033[0m")
                    c_input("" + linnia_name + ": (WHAT.) \033[0m")
                    c_input("" + linnia_name + ": (WHAT.) \033[0m")
                    print()
                    c_input("\033[33m(" + linnia_name + "\033[33m blushes even more.) \033[0m")
                    c_input("\033[33m(" + linnia_name + "\033[33m looks down at the flower and tries to not make eye contact.) \033[0m")
                    c_input("\033[33m(" + linnia_name + "\033[33m takes the flower carefully out of your hand and holds it in both hands.) \033[0m")
        
                elif garden_floor1_pickupflower_choice == '2':
                    c_input("\033[33m(You put the flower in your pocket.) \033[0m")
                    inventory_flower += 1
                    c_input("\033[33m(The flower was added to your inventory.) \033[0m")
                    print()
                    c_input("" + linnia_name + ": (...) \033[0m")
                    print()
                    c_input("\033[33m(" + linnia_name + "\033[33m slowly walks away and tries to think about something else.) \033[0m")
                else:
                    continue
                garden_floor1_pickupflower = 's2'
                break
            print()
            garden_floor1()
        elif garden_floor1_pickupflower == 's2':
            if garden_floor1_pickupflower_flowers_amount == 0:
                c_input("\033[33m(There aren't any flowers left to pick up.) \033[0m")
            else:
                c_input("\033[33m(You picked up another flower.) \033[0m")
                garden_floor1_pickupflower_flowers_amount -= 1
                inventory_flower += 1
                c_input("\033[33m(The flower was added to your inventory.) \033[0m")
            print()
            garden_floor1()

    elif garden_floor1_choice == '0':
        hall_floor1()
    else:
        garden_floor1()



def kitchen_floor1():
    global ft_kitchen_floor1
    global name_kitchen_floor1
    global current_room
    current_room = 'kitchen_floor1'
    if ft_kitchen_floor1 == True:
        c_input("\033[33m(You walk into a pretty white room.) \033[0m")
        c_input("\033[33m(The floor has a black and white checker pattern.) \033[0m")
        c_input("\033[33m(There is a bench in the middle of the room.) \033[0m")
        c_input("\033[33m(There are cabinets along the walls.) \033[0m")
        c_input("\033[33m(It smells pretty good in here.) \033[0m")
        if follower == 'linnia':
            print()
            c_input("" + linnia_name + ": placeholder \033[0m")
        elif follower == 'silf':
            print()
            c_input("" + silf_name + ": This isn't a room I'm often in. \033[0m")
            c_input("" + silf_name + ": I suck at making food... \033[0m")
        name_kitchen_floor1 = 'Kitchen'
        print()
        ft_kitchen_floor1 = False
    c_input("\033[33m(You are in the kitchen. [First floor]) \033[0m")
    print("\033[33m(What do you wanna do?)\033[0m")
    time.sleep(1)
    print("\033[33m[0 = Go back]\033[0m")
    kitchen_floor1_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if kitchen_floor1_choice == '0':
        hall_floor1()
    else:
        kitchen_floor1()



def dining_room_floor1(): # Vurderer å fjerne rommet, fordi jeg ikke kommer på så mye å gjøre her. Kan heller bare flytte bordet til kjøkkenet.
    global ft_dining_room_floor1
    global name_dining_room_floor1
    global current_room
    current_room = 'dining_room_floor1'
    if ft_dining_room_floor1 == True:
        c_input("\033[33m(You walk into what looks like a pretty royal room.) \033[0m")
        c_input("\033[33m(There are paintings on the walls.) \033[0m")
        c_input("\033[33m(A few candlesticks light up the room.) \033[0m")
        c_input("\033[33m(There's a rectangular table in the middle of the room, with chairs gathered around it.) \033[0m")
        name_dining_room_floor1 = 'Dining room'
        print()
        ft_dining_room_floor1 = False
    c_input("\033[33m(You are in the dining room. [First floor]) \033[0m")
    print("\033[33m(What do you wanna do?)\033[0m")
    time.sleep(1)
    print("\033[33m[0 = Go back]\033[0m")
    dining_room_floor1_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if dining_room_floor1_choice == '0':
        hall_floor1()
    else:
        dining_room_floor1()



def valtura_room_floor1():
    global ft_valtura_room_floor1
    global name_valtura_room_floor1
    global current_room
    current_room = 'valtura_room_floor1'
    if ft_valtura_room_floor1 == 's1':
        c_input("" + linnia_name + ": I don't think we should go in there... \033[0m")
        c_input("" + linnia_name + ": That's my mom's room. \033[0m")
        c_input("" + linnia_name + ": Well... It also used to be my dad's room... \033[0m")
        name_valtura_room_floor1 = "" + valtura_name + "\033[33m's room"
        ft_valtura_room_floor1 = 's2'
        print()
        hall_floor1()
    elif ft_valtura_room_floor1 == 's2':
        c_input("" + linnia_name + ": I said we can't go in there. \033[0m")
        print()
        hall_floor1()
    elif ft_valtura_room_floor1 == 's3':
        c_input("\033[33m(You walk into a luxurious looking room.) \033[0m")
        c_input("\033[33m(There are carpet and curtains are dark green coloured.) \033[0m")
        c_input("\033[33m(There is a comfy looking four-poster bed here.) \033[0m")
        c_input("\033[33m(The room gives of a pretty dark feeling.) \033[0m")
        c_input("\033[33m(You feel like you are not allowed to be here.) \033[0m")
        print()
        ft_valtura_room_floor1 = 's4'
    c_input("\033[33m(You are in " + valtura_name + "\033[33m's room. [First floor]) \033[0m")
    print("\033[33m(What do you wanna do?)\033[0m")
    time.sleep(1)
    print("\033[33m[0 = Go back]\033[0m")
    valtura_room_floor1_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if valtura_room_floor1_choice == '0':
        hall_floor1()
    else:
        valtura_room_floor1()



def bathroom_floor1(): # Might be removed.
    global ft_bathroom_floor1
    global name_bathroom_floor1
    global current_room
    current_room = 'bathroom_floor1'
    if ft_bathroom_floor1 == True:
        c_input("\033[33m(placeholder) \033[0m")
        name_bathroom_floor1 = 'Bathroom'
        print()
        ft_bathroom_floor1 = False
    c_input("\033[33m(You are in the bathroom. [First floor]) \033[0m")
    print("\033[33m(What do you wanna do?)\033[0m")
    time.sleep(1)
    print("\033[33m[0 = Go back]\033[0m")
    bathroom_floor1_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if bathroom_floor1_choice == '0':
        hall_floor1()
    else:
        bathroom_floor1()



def door_floor1():
    global ft_door_floor1
    global name_door_floor1
    global door_floor1_openthedoor
    global current_room
    current_room = 'door_floor1'
    if ft_door_floor1 == True:
        c_input("\033[33m(You walk into a small room.) \033[0m")
        c_input("\033[33m(A few small paintings are on the wall.) \033[0m")
        c_input("\033[33m(There's a flower pot in the corner.) \033[0m")
        c_input("\033[33m(It doesn't look like there is much to do here.) \033[0m")
        if follower == 'linnia':
            print()
            c_input("" + linnia_name + ": Uhh... why are we here? \033[0m")
        elif follower == 'silf':
            print()
            c_input("" + silf_name + ": Do you want to leave? \033[0m")
            c_input("" + silf_name + ": Pretty understandable when my sister also lives here, heh. \033[0m")
        name_door_floor1 = 'Door'
        print()
        ft_door_floor1 = False
    c_input("\033[33m(You are at the door. [First floor])  \033[0m")
    print("\033[33m(What do you wanna do?)\033[0m")
    time.sleep(1)
    print("\033[33m[1 = Open the door.]\033[0m")
    print("\033[33m[0 = Go back]\033[0m")
    door_floor1_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if door_floor1_choice == '1':
        if door_floor1_openthedoor == 's1':
            c_input("\033[33m(Surprisingly enough, the door actually opened.) \033[0m")
            print()
            c_input("" + linnia_name + ": Do you wanna leave? \033[0m")
            c_input("" + linnia_name + ": Well then you will have to convince my mom first. \033[0m")
            c_input("" + linnia_name + ": She has put a spell around the house, \033[0m")
            c_input("" + linnia_name + ": So if someone without permisson tries to go from or to the house, they cant. \033[0m")
            c_input("" + linnia_name + ": (...That sounded kinda creepy, didn't it?) \033[0m")
            door_floor1_openthedoor = 's2'
        elif door_floor1_openthedoor == 's2':
            c_input("" + linnia_name + ": Do you really want to leave that much? \033[0m")
            c_input("" + linnia_name + ": Well, go for it. \033[0m")
            c_input("" + linnia_name + ": But you won't get far while my mom's spell is still active. \033[0m")
            door_floor1_openthedoor = 's3'
        elif door_floor1_openthedoor == 's3':
            c_input("\033[33m(You walk out the door.) \033[0m")
            c_input("\033[33m(You follow the gravel path from the house into the woods.) \033[0m")
            c_input("\033[33m(But before you manage to get past the metal fence,) \033[0m")
            c_input("\033[33m(Your vision fades away.) \033[0m")
            c_input("\033[33m(You barely see " + linnia_name + "\033[33m walking towards you, before everything turns black.) \033[0m")
            c_input("\033[33m(You wake up again.) \033[0m")
            print()
            c_input("" + linnia_name + ": Hahaha! \033[0m")
            c_input("" + linnia_name + ": You looked so funny the way you plummeted into the ground! \033[0m")
            c_input("" + linnia_name + ": Wait sorry, I probably shouldn't have laughed at that. \033[0m")
            door_floor1_openthedoor = 's4'
        elif door_floor1_openthedoor == 's4':
            c_input("\033[33m(The spell is still active.) \033[0m")
            c_input("\033[33m(And you don't want to experience going out again.) \033[0m")
        print()
        door_floor1()
    elif door_floor1_choice == '0':
        hall_floor1()
    else:
        door_floor1()



########################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################

# FLOOR 2
def hall_floor2():
    global current_room
    current_room = 'hall_floor2'
    c_input("\033[33m(You are in the hall. [Second floor]) \033[0m")
    print("\033[33m(Where do you wanna go?)\033[0m")
    time.sleep(1)
    print("\033[33m[1 = " + name_balcony_floor2 + "]\033[0m")
    print("\033[33m[2 = " + name_linnia_room_floor2 + "]\033[0m")
    print("\033[33m[3 = " + name_silf_room_floor2 + "]\033[0m")
    print("\033[33m[4 = " + name_bathroom_floor2 + "]\033[0m")
    print("\033[33m[5 = " + name_office_floor2 + "]\033[0m")
    print("\033[33m[0 = Stairs]\033[0m")
    hall_floor2_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if hall_floor2_choice == '1':
        if linnia_current_room != 'balcony_floor2' and linnia_alive == True and follower != 'linnia':
            linnia_random_current_room()
        if silf_current_room != 'balcony_floor2' and silf_alive == True and follower != 'silf':
            silf_random_current_room()
        if valtura_current_room != 'balcony_floor2' and valtura_alive == True:
            valtura_random_current_room()
        if leaf_current_room != 'balcony_floor2' and leaf_alive == True:
            leaf_random_current_room()
        if eerie_current_room != 'balcony_floor2' and eerie_alive == True:
            eerie_random_current_room()
        balcony_floor2()

    elif hall_floor2_choice == '2':
        if linnia_current_room != 'linnia_room_floor2' and linnia_alive == True and follower != 'linnia':
            linnia_random_current_room()
        if silf_current_room != 'linnia_room_floor2' and silf_alive == True and follower != 'silf':
            silf_random_current_room()
        if valtura_current_room != 'linnia_room_floor2' and valtura_alive == True:
            valtura_random_current_room()
        if leaf_current_room != 'linnia_room_floor2' and leaf_alive == True:
            leaf_random_current_room()
        if eerie_current_room != 'linnia_room_floor2' and eerie_alive == True:
            eerie_random_current_room()
        linnia_room_floor2()

    elif hall_floor2_choice == '3':
        if linnia_current_room != 'silf_room_floor2' and linnia_alive == True and follower != 'linnia':
            linnia_random_current_room()
        if silf_current_room != 'silf_room_floor2' and silf_alive == True and follower != 'silf':
            silf_random_current_room()
        if valtura_current_room != 'silf_room_floor2' and valtura_alive == True:
            valtura_random_current_room()
        if leaf_current_room != 'silf_room_floor2' and leaf_alive == True:
            leaf_random_current_room()
        if eerie_current_room != 'silf_room_floor2' and eerie_alive == True:
            eerie_random_current_room()
        silf_room_floor2()

    elif hall_floor2_choice == '4':
        if linnia_current_room != 'bathroom_floor2' and linnia_alive == True and follower != 'linnia':
            linnia_random_current_room()
        if silf_current_room != 'bathroom_floor2' and silf_alive == True and follower != 'silf':
            silf_random_current_room()
        if valtura_current_room != 'bathroom_floor2' and valtura_alive == True:
            valtura_random_current_room()
        if leaf_current_room != 'bathroom_floor2' and leaf_alive == True:
            leaf_random_current_room()
        if eerie_current_room != 'bathroom_floor2' and eerie_alive == True:
            eerie_random_current_room()
        bathroom_floor2()

    elif hall_floor2_choice == '5':
        if linnia_current_room != 'office_floor2' and linnia_alive == True and follower != 'linnia':
            linnia_random_current_room()
        if silf_current_room != 'office_floor2' and silf_alive == True and follower != 'silf':
            silf_random_current_room()
        if valtura_current_room != 'office_floor2' and valtura_alive == True:
            valtura_random_current_room()
        if leaf_current_room != 'office_floor2' and leaf_alive == True:
            leaf_random_current_room()
        if eerie_current_room != 'office_floor2' and eerie_alive == True:
            eerie_random_current_room()
        office_floor2()

    elif hall_floor2_choice == '0':
        stairs()
    else:
        hall_floor2()



def balcony_floor2():
    global ft_balcony_floor2
    global name_balcony_floor2
    global current_room
    current_room = 'balcony_floor2'
    if ft_balcony_floor2 == True:
        c_input("\033[33m(You take a step outside.) \033[0m")
        c_input("\033[33m(The fresh air fills your lungs.) \033[0m")
        c_input("\033[33m(There is a few flower pots around.) \033[0m")
        c_input("\033[33m(There's a lantern here too.) \033[0m")
        if follower == 'linnia':
            print()
            c_input("" + linnia_name + ": One of many reading spots I have. \033[0m")
        elif follower == 'silf':
            print()
            c_input("" + silf_name + ": placeholder \033[0m")
        name_balcony_floor2 = 'Balcony'
        print()
        ft_balcony_floor2 = False
    c_input("\033[33m(You are on the balcony. [Second floor]) \033[0m")
    print("\033[33m(What do you wanna do?)\033[0m")
    time.sleep(1)
    print("\033[33m[0 = Go back]\033[0m")
    balcony_floor2_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if balcony_floor2_choice == '0':
        hall_floor2()
    else:
        balcony_floor2()



def linnia_room_floor2():
    global ft_linnia_room_floor2
    global name_linnia_room_floor2
    global current_room
    current_room = 'linnia_room_floor2'
    if ft_linnia_room_floor2 == True:
        c_input("\033[33m(You walk into what seems like a cozy room.) \033[0m")
        c_input("\033[33m(It looks like a bedroom.) \033[0m")
        c_input("\033[33m(It's very tidy in here.) \033[0m")
        c_input("\033[33m(There are surprisingly many plants here.) \033[0m")
        if follower == 'linnia':
            print()
            c_input("" + linnia_name + ": Feel free to look around if you want to! \033[0m")
        elif follower == 'silf':
            print()
            c_input("" + silf_name + ": I don't get why you brought me here. \033[0m")
        name_linnia_room_floor2 = "" + linnia_name + "\033[33m's room"
        print()
        ft_linnia_room_floor2 = False
    c_input("\033[33m(You are in " + linnia_name + "\033[33m's room. [Second floor]) \033[0m")
    print("\033[33m((What do you wanna do?)\033[0m")
    time.sleep(1)
    print("\033[33m[1 = Examine books.]\033[0m")
    print("\033[33m[0 = Go back]\033[0m")
    linnia_room_floor2_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if linnia_room_floor2_choice == '0':
        hall_floor2()
    else:
        linnia_room_floor2()



def silf_room_floor2():
    global ft_silf_room_floor2
    global name_silf_room_floor2
    global current_room
    current_room = 'silf_room_floor2'
    if ft_silf_room_floor2 == True:
        c_input("\033[33m(You walk into a... uh... room... of some sort.) \033[0m")
        c_input("\033[33m(It's very messy in here.) \033[0m")
        c_input("\033[33m(There's a few posters on the walls.) \033[0m")
        if follower == 'linnia':
            print()
            c_input("" + linnia_name + ": Uhh... \033[0m")
            c_input("" + linnia_name + ": I don't think I'm allowed to be here... \033[0m")
        elif follower == 'silf':
            print()
            c_input("" + silf_name + ": Just do whatever I guess. \033[0m")
        name_silf_room_floor2 = "" + silf_name + "\033[33m's room"
        print()
        ft_silf_room_floor2 = False
    c_input("\033[33m(You are in " + silf_name + "\033[33m's room. [First floor]) \033[0m")
    print("\033[33m(What do you wanna do?)\033[0m")
    time.sleep(1)
    print("\033[33m[0 = Go back]\033[0m")
    silf_room_floor2_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if silf_room_floor2_choice == '0':
        hall_floor2()
    else:
        silf_room_floor2()



def bathroom_floor2(): # Might be removed.
    global ft_bathroom_floor2
    global name_bathroom_floor2
    global current_room
    current_room = 'bathroom_floor2'
    if ft_bathroom_floor2 == True:
        c_input("\033[33m(placeholder) \033[0m")
        name_bathroom_floor2 = 'Bathroom'
        print()
        ft_bathroom_floor2 = False
    c_input("\033[33m(You are in the bathroom. [Second floor]) \033[0m")
    print("\033[33m(What do you wanna do?)\033[0m")
    time.sleep(1)
    print("\033[33m[0 = Go back]\033[0m")
    bathroom_floor2_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if bathroom_floor2_choice == '0':
        hall_floor2()
    else:
        bathroom_floor2()



def office_floor2():
    global ft_office_floor2
    global name_office_floor2
    global office_floor2_examinephotosonthewall
    global office_floor2_makeacallonthetelephone_7, office_floor2_makeacallonthetelephone_17
    global current_room
    current_room = 'office_floor2'
    if ft_office_floor2 == True:
        c_input("\033[33m(You walk into a dark room.) \033[0m")
        c_input("\033[33m(There is a desk in the middle of the room.) \033[0m")
        c_input("\033[33m(The office looks kinda cozy.) \033[0m")
        c_input("\033[33m(It kinda gives off a japanese vibe.) \033[0m")
        if follower == 'linnia':
            print()
            c_input("" + linnia_name + ": This was my dad's office before he vanished. \033[0m")
            c_input("" + linnia_name + ": He used to write a lot in here. \033[0m")
        elif follower == 'silf':
            print()
            c_input("" + silf_name + ": Wasen't long ago that my dad used to write in here. \033[0m")
            c_input("" + silf_name + ": Before he vanished. \033[0m")
        name_office_floor2 = 'Office'
        print()
        ft_office_floor2 = False
    c_input("\033[33m(You are in the office. [Second floor]) \033[0m")
    print("\033[33m(What do you wanna do?)\033[0m")
    time.sleep(1)
    print("\033[33m[1 = Examine photos on the wall.]\033[0m")
    print("\033[33m[2 = Make a call on the telephone.]\033[0m")
    print("\033[33m[0 = Go back]\033[0m")
    office_floor2_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if office_floor2_choice == '1':
        if office_floor2_examinephotosonthewall == 's1':
            c_input("\033[33m(You look up at the photos on the wall.) \033[0m")
            c_input("\033[33m(Most of them are family photos.) \033[0m")
            c_input("\033[33m(But none includes the father in them.) \033[0m")
            if silf_name == '\033[36m???':
                c_input("\033[33m(There's a photo of " + linnia_name + "\033[33m and another boy standing beside her in the garden.) \033[0m")
            elif silf_name == '\033[36mSilf':
                c_input("\033[33m(There's a photo of " + linnia_name + "\033[33m and " + silf_name + "\033[33m standing in the garden.) \033[0m")
            c_input("\033[33m(They're smiling.) \033[0m")
            office_floor2_examinephotosonthewall = 's2'
        elif office_floor2_examinephotosonthewall == 's2':
            c_input("\033[33m(There's a few empty spots on the wall.) \033[0m")
            c_input("\033[33m(It's like a something used to be there.) \033[0m")
            c_input("\033[33m(Almost like something is missing.) \033[0m")
            office_floor2_examinephotosonthewall = 's3'
        elif office_floor2_examinephotosonthewall == 's3':
            c_input("" + linnia_name + ": Why are you looking at the photos so much? \033[0m")
            time.sleep(1)
            print("\033[33m[1 = I was just looking around.]\033[0m")
            print("\033[33m[2 = I was just looking at your photos.]\033[0m")
            office_floor2_examinephotosonthewall_choice = c_input("\033[33mAnswer: \033[0m")
            print()
            time.sleep(1)
            if office_floor2_examinephotosonthewall_choice == '1':
                c_input("" + linnia_name + ": Yeah, some of them are actually very pretty. \033[0m")
                c_input("" + linnia_name + ": This wall shows just how much my dad cared for our family. \033[0m")
                c_input("" + linnia_name + ": I feel like I'm forgetting him more and more for every day that goes by... \033[0m")
            elif office_floor2_examinephotosonthewall_choice == '2':
                c_input("\033[33m(" + linnia_name + "\033[33m stares into your eyes.) \033[0m")
                c_input("\033[33m(She quickly looks away.) \033[0m")
                print()
                c_input("" + linnia_name + ": (HUH??????) \033[0m")
                c_input("" + linnia_name + ": (Why would they say that??) \033[0m")
                c_input("" + linnia_name + ": (Did I hear it wrong??) \033[0m")
                c_input("" + linnia_name + ": (Or maybe I didn't...?) \033[0m")
                print()
                c_input("\033[33m(It looks like " + linnia_name + "\033[33m is thinking hard for herself.) \033[0m")
            office_floor2_examinephotosonthewall = 's4'
        elif office_floor2_examinephotosonthewall == 's4':
            c_input("\033[33m(You look up at the photos on the wall.) \033[0m")
            c_input("\033[33m(You don't find anything interesting.) \033[0m")
            c_input("\033[33m(Other then some very pretty pictures.) \033[0m")
        print()
        office_floor2()

    elif office_floor2_choice == '2':
        c_input("\033[33m(You walk to the telephone.) \033[0m")
        c_input("\033[33m(You dial a random number.) \033[0m")
        c_input("\033[33m(...) \033[0m")
        random_chance_100()
        if random_chance_100_result == 7:
            if office_floor2_makeacallonthetelephone_7 == 's1':
                print()
                c_input("\033[0m???: Hello my good sir... or madam... or whatever you are...! \033[0m")
                c_input("\033[0m???: We are SO happy you called! \033[0m")
                c_input("\033[0m???: Do you want to be a BIG SHOT? \033[0m")
                c_input("\033[0m???: Well congratulations! \033[0m")
                c_input("\033[0m???: Because nows your chance! \033[0m")
                c_input("\033[0m???: Your chance to be a- \033[0m")
                print()
                c_input("\033[33m(The connection got cut off.) \033[0m")
                c_input('\033[33m(You missed your chance to be a "BIG SHOT".) \033[0m')
                office_floor2_makeacallonthetelephone_7 = 's2'
            elif office_floor2_makeacallonthetelephone_7 == 's2':
                c_input("\033[33m(Nobody answered.) \033[0m")
        elif random_chance_100_result == 17:
            if office_floor2_makeacallonthetelephone_17 == 's1':
                print()
                c_input("\033[0m???: Hello, this is Elif. \033[0m")
                c_input("\033[0mElif: Who is this? \033[0m")
                c_input("\033[0mElif: ... \033[0m")
                c_input("\033[0mElif: Hello...? \033[0m")
                c_input("\033[0mElif: (Man, I hate these prank callers.) \033[0m")
                print()
                c_input("\033[33m(They hanged up.) \033[0m")
                office_floor2_makeacallonthetelephone_17 = 's2'
            elif office_floor2_makeacallonthetelephone_17 == 's2':
                c_input("\033[33m(Nobody answered.) \033[0m")
        else:
            c_input("\033[33m(Nobody answered.) \033[0m")
        print()
        office_floor2()

    elif office_floor2_choice == '0':
        hall_floor2()
    else:
        office_floor2()





# FLOOR 3
def attic_floor3():
    global ft_attic_floor3
    global name_attic_floor3
    global current_room
    current_room = 'attic_floor3'

    #if linnia_current_room != 'attic_floor3' and linnia_alive == True and follower != 'linnia':
    #    linnia_random_current_room()
    #if silf_current_room != 'attic_floor3' and silf_alive == True and follower != 'silf':
    #    silf_random_current_room()
    #if valtura_current_room != 'attic_floor3' and valtura_alive == True:
    #    valtura_random_current_room()
    #if leaf_current_room != 'attic_floor3' and leaf_alive == True:
    #    leaf_random_current_room()
    #if eerie_current_room != 'attic_floor3' and eerie_alive == True:
    #    eerie_random_current_room()

    if ft_attic_floor3 == True:
        c_input("\033[33m(You walk into a very dusty room.) \033[0m")
        c_input("\033[33m(It's filled to the brim with random objects.) \033[0m")
        c_input("\033[33m(It is pretty dark here.) \033[0m")
        c_input("\033[33m(Moonlight is shining through the singular window.) \033[0m")
        if follower == 'linnia':
            print()
            c_input("" + linnia_name + ": Uhm... \033[0m")
            c_input("" + linnia_name + ": How long are we gonna stay up here for...? \033[0m")
        elif follower == 'silf':
            print()
            c_input("" + silf_name + ": I remember trapping " + linnia_name + "\033[36m up here when we were younger. \033[0m")
            c_input("" + silf_name + ": Heh, such fun times. \033[0m")
        name_attic_floor3 = 'Attic'
        print()
        ft_attic_floor3 = False
    c_input("\033[33m(You are in the attic.) \033[0m")
    print("\033[33m(What do you wanna do?)\033[0m")
    time.sleep(1)
    print("\033[33m[0 = Go back]\033[0m")
    attic_floor3_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if attic_floor3_choice == '0':
        hall_floor2()
    else:
        attic_floor3()



########################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################

# Remember to ask if the person is already in that room, and make current_room the room it came from.

def linnia_random_current_room():
    global linnia_current_room
    linnia_switch_current_room = random.choice(["no", "no", "yes"])
    if linnia_switch_current_room == 'yes':
        linnia_current_room = random.choice(["parlor_floor1", "garden_floor1", "kitchen_floor1", "dining_room_floor1", "bathroom_floor1", "balcony_floor2", "linnia_room_floor2", "bathroom_floor2"])
        print("Linnia moved room. (ADMIN MESSAGE)")
    return

def silf_random_current_room():
    global silf_current_room
    silf_switch_current_room = random.choice(["no", "no", "yes"])
    if silf_switch_current_room == 'yes':
        silf_current_room = random.choice(["parlor_floor1", "garden_floor1", "kitchen_floor1", "dining_room_floor1", "bathroom_floor1", "balcony_floor2", "silf_room_floor2", "bathroom_floor2"])
        print("Silf moved room. (ADMIN MESSAGE)")
    return

def valtura_random_current_room():
    global valtura_current_room
    valtura_switch_current_room = random.choice(["no", "no", "yes"])
    if valtura_switch_current_room == 'yes':
        valtura_current_room = random.choice(["parlor_floor1", "garden_floor1", "kitchen_floor1", "dining_room_floor1", "bathroom_floor1", "valtura_room_floor1", "balcony_floor2"])
        print("Valtura moved room. (ADMIN MESSAGE)")
    return

def leaf_random_current_room():
    global leaf_current_room
    leaf_switch_current_room = random.choice(["no", "no", "yes"])
    if leaf_switch_current_room == 'yes':
        leaf_current_room = random.choice(["parlor_floor1", "garden_floor1", "kitchen_floor1", "dining_room_floor1", "door_floor1", "balcony_floor2", "linnia_room_floor2"])
        print("Leaf moved room. (ADMIN MESSAGE)")
    return

def eerie_random_current_room():
    global eerie_current_room
    eerie_switch_current_room = random.choice(["no", "no", "yes"])
    if eerie_switch_current_room == 'yes':
        eerie_current_room = random.choice(["nello_floor0", "storage_room_floor0", "parlor_floor1", "garden_floor1", "kitchen_floor1", "dining_room_floor1", "valtura_room_floor1", "bathroom_floor1", "door_floor1", "balcony_floor2", "linnia_room_floor2", "silf_room_floor2", "bathroom_floor2", "attic_floor3"])
        print("Eerie moved room. (ADMIN MESSAGE)")
    return

########################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################

def linnia_talk():
    global linnia_current_room
    global follower
    global talk_attacked
    linnia_talk_option_followme = None
    linnia_talk_option_stopfollowingme = None
    linnia_talk_option_attack = None
    linnia_talk_options = 0
    if talk_attack_linnia_scared == False:
        c_input("" + linnia_name + ": Hii " + name + "\033[35m! Is there something you wanted from me? \033[0m")
    elif talk_attack_linnia_scared == True:
        c_input("" + linnia_name + ": ...Is there something you wanted from me? \033[0m")
    time.sleep(1)
    if follower != 'linnia':
        linnia_talk_options += 1
        print(f"\033[33m[{linnia_talk_options} = Follow me.]\033[0m")
        linnia_talk_option_followme = linnia_talk_options
    if follower == 'linnia':
        linnia_talk_options += 1
        print(f"\033[33m[{linnia_talk_options} = Stop following me.]\033[0m")
        linnia_talk_option_stopfollowingme = linnia_talk_options
    if inventory_knife > 0 or inventory_revolver > 0:
        linnia_talk_options += 1
        print(f"\033[33m[{linnia_talk_options} = Attack]\033[0m")
        linnia_talk_option_attack = linnia_talk_options
    print("\033[33m[0 = Go back]\033[0m")
    linnia_talk_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if linnia_talk_choice == str(linnia_talk_option_followme) and linnia_talk_option_followme is not None:
        c_input("" + linnia_name + ": Sure! \033[0m")
        print()
        follower = 'linnia'
        c_input("\033[33m(" + linnia_name + "\033[33m is now following you.) \033[0m")
        print()
        linnia_talk()
    elif linnia_talk_choice == str(linnia_talk_option_stopfollowingme) and linnia_talk_option_stopfollowingme is not None:
        c_input("" + linnia_name + ": Okay... \033[0m")
        print()
        follower = None
        c_input("\033[33m(" + linnia_name + "\033[33m is no longer following you.) \033[0m")
        print()
        linnia_talk()
    elif linnia_talk_choice == str(linnia_talk_option_attack) and linnia_talk_option_attack is not None:
        talk_attacked = 'linnia'
        talk_attack()
    else:
        linnia_talk()



def silf_talk():
    global silf_current_room
    c_input("" + silf_name + ": talk placeholder \033[0m")


def valtura_talk():
    global valtura_current_room
    c_input("" + valtura_name + ": talk placeholder \033[0m")


def leaf_talk():
    global leaf_current_room
    c_input("Leaf: talk placeholder \033[0m")


def eerie_talk():
    global eerie_current_room
    c_input("Eerie: talk placeholder \033[0m")


def nello_talk():
    global nello_current_room
    c_input("" + nello_name + ": talk placeholder \033[0m")





def talk_attack():
    global talk_attacked
    global talk_attack_weapon
    global linnia_alive, silf_alive, valtura_alive, leaf_alive, eerie_alive
    global talk_attack_linnia_scared
    global talk_attacked_ground
    global talk_attack_choice_knife, talk_attack_choice_revolver
    if current_room == 'garden_floor1': # to specify in <person>_attacked() what floor material there is. (Floor/Ground)
        talk_attacked_ground = 'ground'
    else:
        talk_attacked_ground = 'floor'
    while True:
        talk_attack_option_knife = None
        talk_attack_option_revolver = None
        talk_attack_options = 0
        print("\033[33m(What will you use?)\033[0m")
        time.sleep(1)
        if inventory_knife > 0:
            talk_attack_options += 1
            print(f"\033[33m[{talk_attack_options} = Knife]\033[0m")
            talk_attack_option_knife = talk_attack_options
        if inventory_revolver > 0:
            talk_attack_options += 1
            print(f"\033[33m[{talk_attack_options} = Revolver]\033[0m")
            talk_attack_option_revolver = talk_attack_options
        print("\033[33m[0 = Go back]\033[0m")
        talk_attack_choice = c_input("\033[33mAnswer: \033[0m")
        print()
        time.sleep(1)

        if talk_attack_choice == str(talk_attack_option_knife) and talk_attack_option_knife is not None:
            talk_attack_weapon = 'knife'
            while True:
                print("\033[33m(How will you use the knife?)\033[0m")
                time.sleep(1)
                print("\033[33m[1 = Take out knife.]\033[0m")
                print("\033[33m[2 = Attack immediately.]\033[0m")
                print("\033[33m[0 = Go back]\033[0m")
                talk_attack_choice_knife = c_input("\033[33mAnswer: \033[0m")
                print()
                time.sleep(1)
                if talk_attack_choice_knife == '1':

                    if talk_attacked == 'linnia':
                        c_input("\033[33m(You pull out your knife.) \033[0m")
                        c_input("\033[33m(" + linnia_name + "\033[33m looks down at the knife in your hand, before looking back up into your eyes.) \033[0m")
                        c_input("\033[33m(She looks nervous.) \033[0m")
                        print()
                        c_input("" + linnia_name + ": ... \033[0m")
                        c_input("" + linnia_name + ": Why do you have that...? \033[0m")
                        c_input("" + linnia_name + ": and why did you randomly take it out now...? \033[0m")
                        c_input("" + linnia_name + ": ... \033[0m")
                        c_input("" + linnia_name + ": (It's not like they're gonna...) \033[0m")
                        c_input("" + linnia_name + ": (...) \033[0m")
                        c_input("" + linnia_name + ": (I helped them out of the basement...) \033[0m")
                        c_input("" + linnia_name + ": " + name + "\033[35m... \033[0m")
                        c_input("" + linnia_name + ": Why did you take out a knife...? \033[0m")
                        print()
                        c_input("\033[33m(" + linnia_name + "\033[33m holds her hands together over her chest.) \033[0m")
                        c_input("\033[33m(She's shaking.) \033[0m")
                        time.sleep(1)
                        while True:
                            print("\033[33m[1 = Attack " + linnia_name +"\033[33m.]\033[0m")
                            print("\033[33m[2 = Put away knife.]\033[0m")
                            talk_attack_choice_knife_takeoutknife_linnia_choice = c_input("\033[33mAnswer: \033[0m")
                            print()
                            time.sleep(1)
                            if talk_attack_choice_knife_takeoutknife_linnia_choice == '1':
                                linnia_attacked()
                            elif talk_attack_choice_knife_takeoutknife_linnia_choice == '2':
                                c_input("\033[33m(You look down at your knife.) \033[0m")
                                c_input("\033[33m(You decide to put away the knife.) \033[0m")
                                print()
                                c_input("" + linnia_name + ": ... \033[0m")
                                c_input("" + linnia_name + ": (Why...) \033[0m")
                                c_input("" + linnia_name + ": (Why did they put it away...?) \033[0m")
                                c_input("" + linnia_name + ": (Were they actually gonna...) \033[0m")
                                c_input("" + linnia_name + ": (Did they change their mind??) \033[0m")
                                c_input("" + linnia_name + ": (...) \033[0m")
                                c_input("" + linnia_name + ": (I'm probably just overthinking this, heh...) \033[0m")
                                c_input("" + linnia_name + ": (I should probably just forget about this...) \033[0m")
                                c_input("" + linnia_name + ": (" + name + "\033[35m is a good person.) \033[0m")
                                c_input("" + linnia_name + ": (It's not like they would actually want to hurt me.) \033[0m")
                                print()
                                c_input("\033[33m(" + linnia_name + "\033[33m looks less nervous.) \033[0m")
                                talk_attack_linnia_scared = True
                            else:
                                continue
                            print()
                            break
                        break


                    elif talk_attacked == 'silf':
                        c_input("placeholder (1) talk_attacked == 'silf'")
                        time.sleep(1)
                        while True:
                            print("\033[33m[1 = Attack " + silf_name + "\033[33m.]\033[0m")
                            print("\033[33m[2 = Put away knife.]\033[0m")
                            talk_attack_choice_knife_takeoutknife_silf_choice = c_input("\033[33mAnswer: \033[0m")
                            print()
                            time.sleep(1)
                            if talk_attack_choice_knife_takeoutknife_silf_choice == '1':
                                silf_attacked()
                            elif talk_attack_choice_knife_takeoutknife_silf_choice == '2':
                                c_input("placeholder (1) talk_attacked == 'silf'")
                            else:
                                continue
                            print()
                            break
                        break


                    elif talk_attacked == 'valtura':
                        c_input("placeholder (1) talk_attacked == 'valtura'")
                        time.sleep(1)
                        while True:
                            print("\033[33m[1 = Attack " + valtura_name + "\033[33m.]\033[0m")
                            print("\033[33m[2 = Put away knife.]\033[0m")
                            talk_attack_choice_knife_takeoutknife_valtura_choice = c_input("\033[33mAnswer: \033[0m")
                            print()
                            time.sleep(1)
                            if talk_attack_choice_knife_takeoutknife_valtura_choice == '1':
                                valtura_attacked()
                            elif talk_attack_choice_knife_takeoutknife_valtura_choice == '2':
                                c_input("placeholder (1) talk_attacked == 'valtura'")
                            else:
                                continue
                            print()
                            break
                        break

                    elif talk_attacked == 'leaf':
                        c_input("\033[33m(You pull out your knife.) \033[0m")
                        c_input("\033[33m(It doesn't look like Leaf has a care in the world.) \033[0m")
                        c_input("\033[33m(Leaf cuddles against your leg,) \033[0m")
                        c_input("\033[33m(before looking up at your face.) \033[0m")
                        time.sleep(1)
                        while True:
                            print("\033[33m[1 = Attack Leaf.]\033[0m")
                            print("\033[33m[2 = Put away knife.]\033[0m")
                            talk_attack_choice_knife_takeoutknife_leaf_choice = c_input("\033[33mAnswer: \033[0m")
                            print()
                            time.sleep(1)
                            if talk_attack_choice_knife_takeoutknife_leaf_choice == '1':
                                leaf_attacked()
                            elif talk_attack_choice_knife_takeoutknife_leaf_choice == '2':
                                c_input("\033[33m(You look down at your knife.) \033[0m")
                                c_input("\033[33m(You decide to put away the knife.) \033[0m")
                                c_input("\033[33m(You bend down to pet Leaf.) \033[0m")
                                c_input("\033[33m(Leaf cuddles against your hand.) \033[0m")
                            else:
                                continue
                            print()
                            break
                        break

                    elif talk_attacked == 'eerie':
                        c_input("placeholder (1) talk_attacked == 'eerie'")
                        time.sleep(1)
                        while True:
                            print("\033[33m[1 = Attack \033[0mEerie\033[33m.]\033[0m")
                            print("\033[33m[2 = Put away knife.]\033[0m")
                            talk_attack_choice_knife_takeoutknife_eerie_choice = c_input("\033[33mAnswer: \033[0m")
                            print()
                            time.sleep(1)
                            if talk_attack_choice_knife_takeoutknife_eerie_choice == '1':
                                eerie_attacked()
                            elif talk_attack_choice_knife_takeoutknife_eerie_choice == '2':
                                c_input("placeholder (1) talk_attacked == 'eerie'")
                            else:
                                continue
                            print()
                            break
                        break


                    elif talk_attacked == 'nello':
                        c_input("placeholder (1) talk_attacked == 'nello'")
                        time.sleep(1)
                        while True:
                            print("\033[33m[1 = Attack " + nello_name + "\033[33m.]\033[0m")
                            print("\033[33m[2 = Put away knife.]\033[0m")
                            talk_attack_choice_knife_takeoutknife_nello_choice = c_input("\033[33mAnswer: \033[0m")
                            print()
                            time.sleep(1)
                            if talk_attack_choice_knife_takeoutknife_nello_choice == '1':
                                eerie_attacked()
                            elif talk_attack_choice_knife_takeoutknife_nello_choice == '2':
                                c_input("placeholder (1) talk_attacked == 'nello'")
                            else:
                                continue
                            print()
                            break
                        break


                elif talk_attack_choice_knife == '2':
                    if talk_attacked == 'linnia':
                        linnia_attacked()
                        current_room_check()
                    elif talk_attacked == 'silf':
                        silf_attacked()
                        current_room_check()
                    elif talk_attacked == 'valtura':
                        valtura_attacked()
                        current_room_check()
                    elif talk_attacked == 'leaf': 
                        leaf_attacked()
                        current_room_check()
                    elif talk_attacked == 'eerie':
                        eerie_attacked()
                    elif talk_attacked == 'nello':
                        nello_attacked()
                        current_room_check()

                elif talk_attack_choice_knife == '0':
                    break
                else:
                    continue
            break


        elif talk_attack_choice == str(talk_attack_option_revolver) and talk_attack_option_revolver is not None:
            talk_attack_weapon = 'revolver'
            while True:
                print("\033[33m(How will you use the revolver?)\033[0m")
                time.sleep(1)
                print("\033[33m[1 = Point revolver torwards them.]\033[0m")
                print("\033[33m[2 = Shoot immediately.]\033[0m")
                print("\033[33m[0 = Go back]\033[0m")
                talk_attack_choice_revolver = c_input("\033[33mAnswer: \033[0m")
                print()
                time.sleep(1)
                if talk_attack_choice_revolver == '1':


                    if talk_attacked == 'linnia':
                        c_input("\033[33m(You take out your revolver.) \033[0m")
                        c_input("\033[33m(You point it towards " + linnia_name + "\033[33m's head holding the revolver with one hand.) \033[0m")
                        c_input("\033[33m(" + linnia_name + "\033[33m stares into the revolver.) \033[0m")
                        c_input("\033[33m(She looks nervous.) \033[0m")
                        print()
                        c_input("" + linnia_name + ": ... \033[0m")
                        c_input("" + linnia_name + ": What? \033[0m")
                        c_input("" + linnia_name + ": Why do you have that...? \033[0m")
                        c_input("" + linnia_name + ": For how long have you had that...? \033[0m")
                        c_input("" + linnia_name + ": Why are you pointing in at me!? \033[0m")
                        c_input("" + linnia_name + ": What did I do!? \033[0m")
                        c_input("" + linnia_name + ": " + name + "\033[35m! \033[0m")
                        c_input("" + linnia_name + ": Please... \033[0m")
                        c_input("" + linnia_name + ": Put it away... \033[0m")
                        print()
                        c_input("\033[33m(" + linnia_name + "\033[33m looks down at her hands.) \033[0m")
                        c_input("\033[33m(She's shaking.) \033[0m")
                        time.sleep(1)
                        while True:
                            print("\033[33m[1 = Shoot " + linnia_name +"\033[33m.]\033[0m")
                            print("\033[33m[2 = Put away revolver.]\033[0m")
                            talk_attack_choice_knife_takeoutknife_linnia_choice = c_input("\033[33mAnswer: \033[0m")
                            print()
                            time.sleep(1)
                            if talk_attack_choice_knife_takeoutknife_linnia_choice == '1':
                                linnia_attacked()
                            elif talk_attack_choice_knife_takeoutknife_linnia_choice == '2':
                                c_input("\033[33m(You look beyond your revolver,) \033[0m")
                                c_input("\033[33m(and see " + linnia_name + ".) \033[0m")
                                c_input("\033[33m(She's scared.) \033[0m")
                                c_input("\033[33m(You decide to put away the revolver.) \033[0m")
                                print()
                                c_input("" + linnia_name + ": ... \033[0m")
                                c_input("" + linnia_name + ": Thank you... \033[0m")
                                c_input("" + linnia_name + ": " + name + "\033[35m. \033[0m")
                                c_input("" + linnia_name + ": (What just happended??) \033[0m")
                                c_input("" + linnia_name + ": (They pointed a revolver towards me!) \033[0m")
                                c_input("" + linnia_name + ": (Why??) \033[0m")
                                c_input("" + linnia_name + ": (They are probably just confused...) \033[0m")
                                c_input("" + linnia_name + ": (I don't think they would actually want to hurt me...) \033[0m")
                                c_input("" + linnia_name + ": ... \033[0m")
                                print()
                                c_input("\033[33m(" + linnia_name + "\033[33m looks less nervous.) \033[0m")
                                talk_attack_linnia_scared = True
                            else:
                                continue
                            print()
                            break
                        break

                    elif talk_attacked == 'silf':
                        c_input("placeholder (1) talk_attacked == 'silf'")


                    elif talk_attacked == 'valtura':
                        c_input("placeholder (1) talk_attacked == 'valtura'")


                    elif talk_attacked == 'leaf':
                        c_input("placeholder (1) talk_attacked == 'leaf'")


                    elif talk_attacked == 'eerie':
                        c_input("placeholder (1) talk_attacked == 'eerie'")


                    elif talk_attacked == 'nello':
                        c_input("placeholder (1) talk_attacked == 'nello'")



                elif talk_attack_choice_revolver == '2':
                    if talk_attacked == 'linnia':
                        linnia_attacked()
                        current_room_check()
                    elif talk_attacked == 'silf':
                        silf_attacked()
                        current_room_check()
                    elif talk_attacked == 'valtura':
                        valtura_attacked()
                        current_room_check()
                    elif talk_attacked == 'leaf': 
                        leaf_attacked()
                        current_room_check()
                    elif talk_attacked == 'eerie':
                        eerie_attacked()
                    elif talk_attacked == 'nello':
                        nello_attacked()
                        current_room_check()

                elif talk_attack_choice_revolver == '0':
                    break
                else:
                    continue
            break
        elif talk_attack_choice == '0':
            break
    talk_attack_weapon = None
    if talk_attacked == 'linnia':
        linnia_talk()
    elif talk_attacked == 'silf':
        silf_talk()
    elif talk_attacked == 'valtura':
        valtura_talk()
    elif talk_attacked == 'leaf':
        leaf_talk()
    elif talk_attacked == 'eerie':
        eerie_talk()
    elif talk_attacked == 'eerie':
        nello_talk()



def linnia_attacked():
    global linnia_alive
    global follower
    global talk_attack_choice_knife, talk_attack_choice_revolver

    if talk_attack_weapon == 'knife':
        if talk_attack_choice_knife == '1':
            c_input("\033[33m(You lunge towards " + linnia_name + "\033[33m with your knife in hand.) \033[0m")
        elif talk_attack_choice_knife == '2':
            c_input("\033[33m(You pull out your revolver and lunge towards " + linnia_name + "\033[33m.) \033[0m")
        c_input("\033[33m(" + linnia_name + "\033[33m doesn't have time to react.) \033[0m")
        c_input("\033[33m(You force the knife into her stomach.) \033[0m")
        c_input("\033[33m(" + linnia_name + "\033[33m tries to scream,) \033[0m")
        c_input("\033[33m(But she makes no sound.) \033[0m")
        c_input("\033[33m(Her blood spills over your hands.) \033[0m")
        c_input("\033[33m(" + linnia_name + "\033[33m plummets onto the " + talk_attacked_ground + ".) \033[0m")
        c_input("\033[33m(She gasps for air while holding her hand on the wound.) \033[0m")
        c_input("\033[33m(You stomp on her head as hard as you can, crushing her head into the " + talk_attacked_ground + ".) \033[0m")
        c_input("\033[33m(" + linnia_name + "\033[33m lays flat on the " + talk_attacked_ground + ".) \033[0m")
        c_input("\033[33m(She doesn't move anymore.) \033[0m")
        c_input("\033[33m(You look over at your knife.) \033[0m")
        c_input("\033[33m(It's covered in blood.) \033[0m")
        c_input("\033[33m(The blood is dripping down your arm, and a few drops fall onto the " + talk_attacked_ground + ".) \033[0m")
        c_input("\033[33m(A small puddle of blood forms around " + linnia_name + "\033[33m's corpse.) \033[0m")

    elif talk_attack_weapon == 'revolver':
        if talk_attack_choice_revolver == '1':
            c_input("\033[33m(You press down the trigger.) \033[0m")
        elif talk_attack_choice_revolver == '2':
            c_input("\033[33m(You pull out your revolver and fire towards " + linnia_name + "\033[33m.) \033[0m")
        c_input("\033[33m(A loud bang goes through the entire house.) \033[0m")
        c_input("\033[33m(The bullet goes directly through " + linnia_name + "\033[33m's head.) \033[0m")
        c_input("\033[33m(Linnia falls onto the " + talk_attacked_ground + ".) \033[0m")
        c_input("\033[33m(A puddle of blood forms around her head.) \033[0m")
        c_input("\033[33m(She doesn't move anymore.) \033[0m")
        c_input("\033[33m(You look at your revolver.) \033[0m")
        c_input("\033[33m(You aim your revolver towards " + linnia_name + "\033[33m and press down the trigger.) \033[0m")
        c_input("\033[33m(Another loud bang is heard through the building.) \033[0m")
        c_input("\033[33m(The bullet goes through her chest.) \033[0m")
        c_input("\033[33m(More blood fills the " + talk_attacked_ground +".) \033[0m")
        c_input("\033[33m(You lower your revolver.) \033[0m")
        c_input("\033[33m(" + linnia_name + "\033[33m's corpse lays on the " + talk_attacked_ground +".) \033[0m")

    print()
    if follower == 'linnia':
        follower = None
    linnia_alive = False
    return

def silf_attacked():
    global silf_alive
    global follower
    if talk_attack_weapon == 'knife':
        c_input("\033[33m(placeholder silf_attacked (knife)) \033[0m")
    elif talk_attack_weapon == 'revolver':
        c_input("\033[33m(placeholder silf_attacked (revolver)) \033[0m")
    print()
    if follower == 'silf':
        follower = None
    silf_alive = False
    return

def valtura_attacked():
    global valtura_alive
    global follower
    if talk_attack_weapon == 'knife':
        c_input("\033[33m(placeholder valtura_attacked (knife)) \033[0m")
    elif talk_attack_weapon == 'revolver':
        c_input("\033[33m(placeholder valtura_attacked (revolver)) \033[0m")
    print()
    valtura_alive = False
    return

def leaf_attacked():
    global leaf_alive
    global follower
    if talk_attack_weapon == 'knife':
        c_input("\033[33m(placeholder leaf_attacked (knife)) \033[0m")
    elif talk_attack_weapon == 'revolver':
        c_input("\033[33m(placeholder leaf_attacked (revolver)) \033[0m")
    print()
    leaf_alive = False
    return

def eerie_attacked():
    global eeire_alive
    global follower
    if talk_attack_weapon == 'knife':
        c_input("\033[33m(placeholder eerie_attacked (knife)) \033[0m")
    elif talk_attack_weapon == 'revolver':
        c_input("\033[33m(placeholder eerie_attacked (revolver)) \033[0m")
    print()
    return

def nello_attacked():
    global nello_alive
    global follower
    if talk_attack_weapon == 'knife':
        c_input("\033[33m(placeholder nello_attacked (knife)) \033[0m")
    elif talk_attack_weapon == 'revolver':
        c_input("\033[33m(placeholder nello_attacked (revolver)) \033[0m")
    print()
    if follower == 'nello':
        follower = None
    nello_alive = False
    return





def current_room_check():
    if current_room == 'storage_room_floor0':
        storage_room_floor0()
    elif current_room == 'nello_floor0':
        nello_floor0()

    elif current_room == 'parlor_floor1':
        parlor_floor1()
    elif current_room == 'garden_floor1':
        garden_floor1()
    elif current_room == 'kitchen_floor1':
        kitchen_floor1()
    elif current_room == 'dining_room_floor1':
        dining_room_floor1()
    elif current_room == 'valtura_room_floor1':
        valtura_room_floor1()
    elif current_room == 'bathroom_floor1':
        bathroom_floor1()
    elif current_room == 'door_floor1':
        door_floor1()

    elif current_room == 'balcony_floor2':
        balcony_floor2()
    elif current_room == 'linnia_room_floor2':
        linnia_room_floor2()
    elif current_room == 'silf_room_floor2':
        silf_room_floor2()
    elif current_room == 'bathroom_floor2':
        bathroom_floor2()
    elif current_room == 'office_floor2':
        office_floor2()

    elif current_room == 'attic_floor3':
        attic_floor3()

    else:
        c_input("\033[33m(Uhm...) \033[0m")
        c_input("\033[33m(So i have no idea how to tell you this...) \033[0m")
        c_input("\033[33m(When trying to check what room you were currently in...) \033[0m")
        c_input("\033[33m(It failed.) \033[0m")
        c_input("\033[33m(Therefore we have no idea where to put you.) \033[0m")
        c_input("\033[33m(So...) \033[0m")
        c_input("\033[33m(Here's the credits I guess, and sorry for the bug you encountered. (Even tho I am almost 100% It's impossible to see this in game.)) \033[0m")
        c_input("\033[33m(You could even count this as a secret ending if you want to.) \033[0m")
        credits()



########################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################

# Battle Against A True Hero (Battles)


########################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################
# TESTING
print("----------------------------------------------------------------------------------------------------")
print("[ADMIN TESTING]:")

name = '\033[33mÅsmund'
linnia_name = '\033[35mLinnia'
silf_name = '\033[36mSilf'
print("name = '\033[33mÅsmund\033[0m'")
print("linnia_name = '\033[35mLinnia\033[0m'")
print("silf_name = '\033[36mSilf\033[0m'")

inventory_flower = 4
inventory_knife = 1
inventory_revolver = 1
inventory_basement_key = 0
inventory_spellbook = 0
print("inventory_flower = 4")
print("inventory_knife = 1")
print("inventory_revolver = 1")
print("inventory_basement_key = 0")
print("inventory_spellbook = 0")

#follower = 'linnia'
#follower = 'silf'
#print("follower = 'linnia'")
#print("follower = 'silf'")

current_room = 'parlor_floor1'
print("current_room = 'parlor_floor1'")

print("hall_floor1()")
#print("linnia_talk()")

print("----------------------------------------------------------------------------------------------------")

hall_floor1()
#linnia_talk()

########################################################################################################################################################################################################
########################################################################################################################################################################################################
########################################################################################################################################################################################################

# START OF GAME
print()
print("\033[33mREMEMBER; THERE ARE NO SAVE POINTS IN THIS GAME!\033[0m")
time.sleep(1)


while True:
    print()
    print("\033[33mName the Player. (PLEASE NOTE THAT THIS CAN'T BE CHANGED LATER ON)\033[0m")
    time.sleep(1)
    name = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if name.lower() == 'player':
        print("\033[34mUhh... no.\033[0m")
        time.sleep(1)
        continue
    elif name.lower() == '' or name == ' ' or name == '  ' or name == '   ' or name == '    ' or name == '     ':
        print("\033[34mYou can't have a blank name.\033[0m")
        time.sleep(1)
        continue
    elif name.lower() == 'changed later on':
        print("\033[34m...Are you actually serious?\033[0m")
        time.sleep(1)
        continue
    elif name.lower() == 'man':
        print("\033[31m...\033[0m")
        time.sleep(1)
        continue
    elif name.lower() == 'nello':
        print("\033[30mThat names taken, kid.\033[0m")
        time.sleep(1)
        continue
    elif name.lower() == 'eerie':
        print("\033[34mHeh, pretty sure that name is taken.\033[0m")
        time.sleep(1)
        continue
    elif name.lower() == 'linnia':
        print("\033[35mUhh... it's nice to see that you like my name, but I think you should have your own.\033[0m")
        time.sleep(1)
        continue
    elif name.lower() == 'leaf':
        print("\033[34mMeow! (He says that he wants you to find another name.)\033[0m")
        time.sleep(1)
        continue
    elif name.lower() == 'silf':
        print("\033[36mThat's my name dipshit.\033[0m")
        time.sleep(1)
        continue
    elif name.lower() == 'valtura':
        print("\033[32mI let you live in my house, and you dare try take my name!? You ungrateful little intruder.\033[0m")
        time.sleep(1)
        continue
    elif name.lower() == 'elif':
        print("\033[34mHmm... I think that name is taken... isn't it? \033[0m")
        time.sleep(1)
        continue
    elif name.lower() == 'program' or name == 'the program':
        print("\033[34mNegative.\033[0m")
        time.sleep(1)
        continue
    else:
        print("\033[33mIs " + name + " correct?\033[0m")
        time.sleep(1)
        print("\033[33m[1 = Yes]\033[0m")
        print("\033[33m[2 = No]\033[0m")
        confirm_name = c_input("\033[33mAnswer: \033[0m")
        if confirm_name == '1':
            break
        elif confirm_name == '2':
            time.sleep(1)
            continue
        else:
            time.sleep(1)
            continue

name = "\033[33m" + name + ""



time.sleep(2)
print()
print("\033[34m.\033[0m")
time.sleep(2)
print("\033[34m..\033[0m")
time.sleep(2)
print("\033[34m...\033[0m")
time.sleep(2)
print()
print()
print()

while True:
    print("" + nello_name + ": Rock, paper, or scissors, Shoot!\033[0m")
    time.sleep(1)
    print("\033[33m[1 = Rock]\033[0m")
    print("\033[33m[2 = Paper]\033[0m")
    print("\033[33m[3 = Scissors]\033[0m")
    rps_hand = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)

    nello_rps_hand = random.choice(["rock", "paper", "scissors"])
    
    if nello_rps_hand == 'rock' and rps_hand == '1':
        c_input("" + nello_name + ": Wow. It's a tie. \033[0m")
    elif nello_rps_hand == 'rock' and rps_hand == '2':
        c_input("" + nello_name + ": Damn, I lost. \033[0m")
    elif nello_rps_hand == 'rock' and rps_hand == '3':
        c_input("" + nello_name + ": Heh, I won. \033[0m")
    elif nello_rps_hand == 'paper' and rps_hand == '1':
        c_input("" + nello_name + ": Heh, I won. \033[0m")
    elif nello_rps_hand == 'paper' and rps_hand == '2':
        c_input("" + nello_name + ": Wow. It's a tie. \033[0m")
    elif nello_rps_hand == 'paper' and rps_hand == '3':
        c_input("" + nello_name + ": Damn, I lost. \033[0m")
    elif nello_rps_hand == 'scissors' and rps_hand == '1':
        c_input("" + nello_name + ": Damn, I lost. \033[0m")
    elif nello_rps_hand == 'scissors' and rps_hand == '2':
        c_input("" + nello_name + ": Heh, I won. \033[0m")
    elif nello_rps_hand == 'scissors' and rps_hand == '3':
        c_input("" + nello_name + ": Wow. It's a tie. \033[0m")
    else:
        continue
        

    print("" + nello_name + ": Wanna rematch?\033[0m")
    time.sleep(1)
    print("\033[33m[1 = Uhh... Sure!]\033[0m")
    print("\033[33m[2 = Uhh... No thanks.]\033[0m")
    rps_rematch_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if rps_rematch_choice == '1':
        c_input("" + nello_name + ": Bet. \033[0m")
        continue
    elif rps_rematch_choice == '2':
        break

c_input("" + nello_name + ": Okay. \033[0m")
c_input("" + nello_name + ": But it's not like there's anything else to do here. \033[0m")
print()
c_input("\033[33m(You look around.) \033[0m")
c_input("\033[33m(It seems like you are in someones basement.) \033[0m")
while True:
    if basement_girl == 's1':
        print("\033[33m(What do you wanna do?)\033[0m")
        time.sleep(1)
        print("\033[33m[1 = Talk with " + nello_name + "\033[33m]\033[0m")
        print("\033[33m[2 = Look out the small window.]\033[0m")
        print("\033[33m[3 = Try to open door.]\033[0m")
        print("\033[33m[4 = Talk with a small yellow flower growing in the corner.]\033[0m")
        basement_choice = c_input("\033[33mAnswer: \033[0m")
        print()
        time.sleep(1)

        if basement_choice == '1':
            c_input("\033[33m(You talk with " + nello_name + "\033[33m.) \033[0m")
            print()
            while True:
                print("" + nello_name + ": Is there something you wanted from me kid?\033[0m")
                time.sleep(1)
                print("\033[33m[1 = Who are you?]\033[0m")
                print("\033[33m[2 = Where are we?]\033[0m")
                print("\033[33m[0 = Go back.]\033[0m")
                basement_nello_choice = c_input("\033[33mAnswer: \033[0m")
                print()
                time.sleep(1)
                if basement_nello_choice == '1':
                    if basement_nello_whoareyou == 's1':
                        c_input("" + nello_name + ": What? \033[0m")
                        c_input("" + nello_name + ": What do you mean kid? \033[0m")
                        c_input("" + nello_name + ": I'm your buddy, Nello? \033[0m")
                        nello_name = '\033[30mNello'
                        c_input("" + nello_name + ": Did you forget? \033[0m")
                        c_input("" + nello_name + ": Come on, I couldn't have hit you that hard last time we were playing games. \033[0m")
                        c_input("" + nello_name + ": To my defence kid, you were definitively cheating. \033[0m")
                        basement_nello_whoareyou = 's2'
                        basement_nello_wherearewe = 's2'
                        print()
                    elif basement_nello_whoareyou == 's2':
                        c_input("" + nello_name + ": I just told you kid. \033[0m")
                        c_input("" + nello_name + ": I'm Nello. \033[0m")
                        print()
                elif basement_nello_choice == '2':
                    if basement_nello_wherearewe == 's1':
                        c_input("" + nello_name + ": Stop asking stupid questions you already know the answer to. \033[0m")
                        print()
                    elif basement_nello_wherearewe == 's2':
                        c_input("" + nello_name + ": Yeah, I should probably tell you, if you don't remember anything. \033[0m")
                        c_input("" + nello_name + ": We are in the basement of an old mansion. \033[0m")
                        c_input("" + nello_name + ": It kinda looks like vampires would live here. \033[0m")
                        c_input("" + nello_name + ": I have been here for about one and a half week. \033[0m")
                        c_input("" + nello_name + ": You only came here the evening before yesterday. \033[0m")
                        c_input("" + nello_name + ": I am here because I tried to rob the place, and got caught. \033[0m")
                        c_input("" + nello_name + ": But you didn't tell why you were here. \033[0m")
                        c_input("" + nello_name + ": But I guess were never finding that out, because of your sudden memory loss. \033[0m")
                        basement_nello_wherearewe = 's3'
                        print()
                    elif basement_nello_wherearewe == 's3':
                        c_input("" + nello_name + ": I'm not telling you again. You should be able to remember what I just said. \033[0m")
                        print()
                elif basement_nello_choice == '0':
                    if basement_nello_whoareyou == 's2' and basement_nello_wherearewe == 's3':
                        basement_girl = 's2'
                        break
                    else:
                        break
    
        elif basement_choice == '2':
            if basement_window == 's1':
                c_input("\033[33m(You move a chair so you can reach the window.) \033[0m")
                c_input("\033[33m(It's a garden.) \033[0m")
                c_input("\033[33m(The vibrant red nature is waving in the wind.) \033[0m")
                c_input("\033[33m(The moon is glowing in the sky.) \033[0m")
                c_input("\033[33m(Well, there is also a tree in the middle of the garden.) \033[0m")
                basement_window = 's2'
                print()
            elif basement_window == 's2':
                c_input("\033[33m(You step on the chair again so you can reach the window.) \033[0m")
                c_input("\033[33m(The chair broke.) \033[0m")
                c_input("\033[33m(" + nello_name + "\033[33m doesn't say anything, but looks at you with disappointment.) \033[0m")
                basement_window = 's3'
                print()
            elif basement_window == 's3':
                c_input("\033[33m(The chair is broken.) \033[0m")
                print()
    
        elif basement_choice == '3':
            if basement_door == 's1':
                c_input("\033[33m(You try to open the door.) \033[0m")
                c_input("\033[33m(It's locked.) \033[0m")
                print()
                c_input("" + nello_name + ": If it was open, we would be down here right now dumbass. \033[0m")
                basement_door = 's2'
                print()
            elif basement_door == 's2':
                c_input("\033[33m(You try to open the door.) \033[0m")
                print()
                c_input("" + nello_name + ": It's still locked, dumbass. \033[0m")
                print()
    
        elif basement_choice == '4':
            if basement_flower == 's1':
                c_input("\033[33m(You bend down to try to talk with the small yellow flower.) \033[0m")
                c_input("\033[33m(It doesn't respond.) \033[0m")
                c_input("\033[33m(You feel stupid for ever thinking it would respond.) \033[0m")
                basement_flower = 's2'
                print()
            elif basement_flower == 's2':
                c_input("\033[33m(You bend down to try to talk with the small yellow flower again.) \033[0m")
                c_input("\033[33m(It still doesn't respond.) \033[0m")
                c_input("\033[33m(You feel even more stupid.) \033[0m")
                basement_flower = 's3'
                print()
            elif basement_flower == 's3':
                c_input("\033[33m(You bend down to try to talk with the small yellow flower for the third time.) \033[0m")
                c_input("\033[33m(You hear a small voice coming from the flower.) \033[0m")
                c_input("\033[33m(Nevermind, it was just your imagination.) \033[0m")
                c_input("\033[33m(You've never felt more stupid before.)  \033[0m")
                basement_flower = 's4'
                print()
            elif basement_flower == 's4':
                print("\033[33m(At last, you meet the flower again.)\033[0m")
                time.sleep(1)
                print("\033[33m[1 = Step on the flower.]\033[0m")
                print("\033[33m[0 = Go back]\033[0m")
                basement_flower_choice = c_input("\033[33mAnswer: \033[0m")
                print()
                time.sleep(1)
                if basement_flower_choice == '1':
                    c_input("\033[33m(You intentionally step on the flower.) \033[0m")
                    print()
                    c_input("" + nello_name + ": I don't think \033[0mEerie\033[30m will appreciate you stepping on their flower. \033[0m")
                    basement_flower = 's5'
                    print()
                elif basement_flower_choice == '0':
                    continue
            elif basement_flower == 's5':
                c_input("\033[33m(The flower is two-dimensional.) \033[0m")
                print()
    elif basement_girl == 's2':
        break

time.sleep(1)
c_input("\033[33m(You hear someone outside the door.) \033[0m")
print()
c_input("" + linnia_name + ": H-hello...? \033[0m")
c_input("" + linnia_name + ": I am here to meet... \033[0m")
c_input("" + linnia_name + ": Uhh... \033[0m")
c_input("" + linnia_name + ": I don't know your name but... \033[0m")
c_input("" + linnia_name + ": The person who just got here. \033[0m")
print()
c_input("" + nello_name + ": Wait, why is she here? \033[0m")
c_input("" + nello_name + ": Well, she's talking about you, kid. \033[0m")
c_input("" + nello_name + ": Either way, I don't really want to meet her mother again. \033[0m")
c_input("" + nello_name + ": And you will probably help me out of here later, right kid? \033[0m")
c_input("" + nello_name + ": Welp, goodbye for now, kid. \033[0m")
c_input("" + nello_name + ": I hope to see you come visit sometime. \033[0m")
print()
c_input("\033[33m(The girl opens the door.) \033[0m")
c_input("\033[33m(You walk out of the room.) \033[0m")
c_input("\033[33m(The girl shuts the door and locks it.) \033[0m")
c_input("\033[33m(In front of you is a girl, looks around your age. She has brown hair, and glasses.) \033[0m")
c_input("\033[33m(You look around in the room. It's a pretty old basement with a few spider webs here and there.) \033[0m")
c_input("\033[33m(The girl looks over at you, and it looks like she doesn't know what to say next.) \033[0m")
c_input("\033[33m(It turns quiet for a few seconds.) \033[0m")
print()
c_input("" + linnia_name + ": Soo... umm... hi! \033[0m")
c_input("" + linnia_name + ": Sorry for my mom trapping you down here... \033[0m")
c_input("" + linnia_name + ": She's a pretty stange person to be honest. \033[0m")
c_input("" + linnia_name + ": She didn't really like the idea of letting you out, \033[0m")
c_input("" + linnia_name + ": But I still managed to convince her to let you out. \033[0m")
c_input("" + linnia_name + ": Kinda convinced her... \033[0m")
c_input("" + linnia_name + ": I don't really know, but I think I can figure it out with her. \033[0m")
c_input("" + linnia_name + ": ... \033[0m")
c_input("" + linnia_name + ": Uhh... so whats your name? \033[0m")
print()
c_input("\033[33m(You tell the girl your name.) \033[0m")
print()
c_input("" + linnia_name + ": " + name +  "\033[35m?\033[0m")
c_input("" + linnia_name + ": Well it's nice to meet you, " + name + "\033[35m!\033[0m")
c_input("" + linnia_name + ": My name is Linnia!\033[0m")
linnia_name = '\033[35mLinnia'

while True:
    if basement_girl_leave == 's1':
        print("" + linnia_name + ": Is there anything you want to ask me? \033[0m")
        time.sleep(1)
        print("\033[33m[1 = Where am I?]\033[0m")
        print("\033[33m[2 = Tell me more about you.]\033[0m")
        print("\033[33m[3 = Why did you let me out?]\033[0m")
        print("\033[33m[4 = Can you let out " + nello_name + "\033[33m?]\033[0m")
        print("\033[33m[5 = Continue.]\033[0m")
        basement_girl_choice = c_input("\033[33mAnswer: \033[0m")
        print()
        time.sleep(1)
        if basement_girl_choice == '1':
            if basement_girl_whereami == 's1':
                c_input("" + linnia_name + ": We are in the basement of where i live. \033[0m")
                c_input("" + linnia_name + ": My mom trapped you down here, \033[0m")
                c_input("" + linnia_name + ": But she haven't told me why? \033[0m")
                c_input("" + linnia_name + ": Well, I'll just have to hope it wasn't for murdering someone or something like that. \033[0m")
                c_input("" + linnia_name + ": ... \033[0m")
                c_input("" + linnia_name + ": Right...? \033[0m")
                basement_girl_whereami = 's2'
                print()
            elif basement_girl_whereami == 's2':
                c_input("" + linnia_name + ": Uhh... do you want me to tell you again? \033[0m")
                c_input("" + linnia_name + ": We are in the basement of where i live. \033[0m")
                c_input("" + linnia_name + ": My mom trapped you down here, \033[0m")
                c_input("" + linnia_name + ": But she haven't told me why. \033[0m")
                print()

        elif basement_girl_choice == '2':
            if basement_girl_tellmemoreaboutyou == 's1':
                c_input("" + linnia_name + ": oh yeah! \033[0m")
                c_input("" + linnia_name + ": I'm Linnea, which I already told you haha... \033[0m")
                c_input("" + linnia_name + ": I like reading. \033[0m")
                c_input("" + linnia_name + ": I live here with my mom and my just barely bigger brother. \033[0m")
                basement_girl_tellmemoreaboutyou = 's2'
                print()
            elif basement_girl_tellmemoreaboutyou == 's2':
                c_input("" + linnia_name + ": Do you want to hear even more about me...? \033[0m")
                c_input("\033[33m(" + linnia_name + "\033[33m looks away and blushes a little.) \033[0m")
                c_input("" + linnia_name + ": (Pull yourself together Linnea, probably didn't mean it in a weird way.) \033[0m")
                c_input("" + linnia_name + ": I can't come to think of anything right now... \033[0m")
                c_input("" + linnia_name + ": Uhh... I have brown cat named Leaf? \033[0m")
                basement_girl_tellmemoreaboutyou = 's3'
                print()
            elif basement_girl_tellmemoreaboutyou == 's3':
                c_input("\033[33m(" + linnia_name + "\033[33m looks away again and kinda tries to hide her face.) \033[0m")
                c_input("" + linnia_name + ": (Why are they asking again???) \033[0m")
                c_input("" + linnia_name + ": (Do they want to know even more about me???) \033[0m")
                c_input("" + linnia_name + ": Umm... I can't think of anything more right now... \033[0m")
                c_input("" + linnia_name + ": If your interested, I could probably tell you about some more of my interests later? \033[0m")
                basement_girl_tellmemoreaboutyou = 's4'
                print()
            elif basement_girl_tellmemoreaboutyou == 's4':
                c_input("" + linnia_name + ": (...) \033[0m")
                c_input("\033[33m(" + linnia_name + "\033[33m doesn't answer.) \033[0m")
                print()
                
        elif basement_girl_choice == '3':
            if basement_girl_whydidyouletmeout == 's1':
                c_input("" + linnia_name + ": Umm... \033[0m")
                c_input("" + linnia_name + ": Well I heard that mom had captured you and put you down here with \033[30mNello\033[35m. \033[0m")
                c_input("" + linnia_name + ": And it isn't very often we get visitors. \033[0m")
                c_input("" + linnia_name + ": Especially not people around my age... \033[0m")
                c_input("" + linnia_name + ": So I kinda wanted to get to know you... \033[0m")
                c_input("" + linnia_name + ": I don't mean anything weird with that! I Just like to have more friends. \033[0m")
                basement_girl_whydidyouletmeout = 's2'
                print()
            elif basement_girl_whydidyouletmeout == 's2':
                c_input("" + linnia_name + ": Uhh... do you want me to tell you again? \033[0m")
                c_input("" + linnia_name + ": Well I heard that mom had captured you and put you down here with \033[30mNello\033[35m.\033[0m")
                c_input("" + linnia_name + ": And It isn't very often my visitors. \033[0m")
                c_input("" + linnia_name + ": Especially not people around my age... \033[0m")
                c_input("" + linnia_name + ": So I kinda wanted to get to know you... \033[0m")
                c_input("" + linnia_name + ": And like I said, I don't mean anything weird with that. I Just like to have more friends. \033[0m")
                print()

        elif basement_girl_choice == '4':
            if basement_girl_canyouletoutnello == 's1':
                c_input("" + linnia_name + ": I barely convinced my mom to let you out, \033[0m")
                c_input("" + linnia_name + ": So sadly not. \033[0m")
                c_input("" + linnia_name + ": I kinda stole the key from her... \033[0m")
                c_input("" + linnia_name + ": But I will give it back to her when she's home again. \033[0m")
                basement_girl_canyouletoutnello = 's2'
                print()
            elif basement_girl_canyouletoutnello == 's2':
                c_input("" + linnia_name + ": I already said I can't! \033[0m")
                c_input("" + linnia_name + ": Sorry... \033[0m")
                print()

        elif basement_girl_choice == '5':
            if basement_girl_whereami == 's2' and basement_girl_tellmemoreaboutyou == 's2' or basement_girl_tellmemoreaboutyou == 's3' or basement_girl_tellmemoreaboutyou == 's4' and basement_girl_whydidyouletmeout == 's2' and basement_girl_canyouletoutnello == 's2':
                basement_girl_leave = 's2'
                break
            else:
                while True:
                    print("" + linnia_name + ": Are you sure there isn't anything else you wanted to ask me? \033[0m")
                    time.sleep(1)
                    print("\033[33m[1 = Yes.]\033[0m")
                    print("\033[33m[0 = Go back]\033[0m")
                    basement_girl_choice_leave = c_input("\033[33mAnswer: \033[0m")
                    print()
                    time.sleep(1)
                    if basement_girl_choice_leave == '1':
                        basement_girl_leave = 's2'
                        break
                    elif basement_girl_choice_leave == '0':
                        break
    elif basement_girl_leave == 's2':
        break

c_input("" + linnia_name + ": Let's leave the basement then. \033[0m")
c_input("" + linnia_name + ": I don't really like being down here. \033[0m")
c_input("" + linnia_name + ": Just follow me. \033[0m")
print()
c_input("\033[33m(You follow " + linnia_name + "\033[33m up the stairs.) \033[0m")
print()
c_input("" + linnia_name + ": Mom isn't home right now, but she will be back later. \033[0m")
c_input("" + linnia_name + ": I guess you should probably get to know the place. \033[0m")
while True:
    print("" + linnia_name + ": Would you want me to follow you to show you around? \033[0m")
    time.sleep(1)
    print("\033[33m[1 = Yes.]\033[0m")
    print("\033[33m[2 = No.]\033[0m")
    basement_girl_follow_choice = c_input("\033[33mAnswer: \033[0m")
    print()
    time.sleep(1)
    if basement_girl_follow_choice == '1':
        c_input("" + linnia_name + ": Okay then! \033[0m")
        c_input("" + linnia_name + ": So just say where you wanna go first! \033[0m")
        follower = 'linnia'
        break
    elif basement_girl_follow_choice == '2':
        c_input("" + linnia_name + ": Oh... \033[0m")
        c_input("" + linnia_name + ": That's fine! \033[0m")
        c_input("" + linnia_name + ": If you are wondering about anything, feel free to ask me! \033[0m")
        c_input("" + linnia_name + ": (It's not like I wanted to go with you anyway...) \033[0m")
        break
print()
c_input("\033[33m(You look around.) \033[0m")
hall_floor1()