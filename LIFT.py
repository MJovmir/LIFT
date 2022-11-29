 # LIFT SIMULATION / realms simulation
# conditionals / looping / branching
# logic wrapping / indie-out
# logic


# HW1* write the logic for no ROOF and no PARKING
# HW2* write the logic for the Human inside the lift  
# HW3* write the logic for the LIFT Bottom at 1st level
# HW4* write the logic for the LIFT TOP at 9th level
# HW5* add code se when the lift arrives -> human exists
from os import system 
from time import sleep
DIR_UP = -1
DIR_STOP = 0
DIR_DOWN = 1

building_roof = True # or False
building_floors = 9
building_parking = True   # or False

lift_floor= 8
lift_open = True
lift_dir = DIR_STOP
lift_target_floor = 7

human_floor = 3
human_in_lift = True



# ---|-----|----
#  R |     |
# ---|     |----
#  9 |     |
# ---|     |----
#  8 |     |
# ---|     |----
#  7 |     |
# ---|     |----
#  6 |     |
# ---|     |----
#  5 |     |
# ---|     |----
#  4 | < > |
# ---||---||----
#  3 ||   || H 
# ---||---||----
#  2 |     |
# ---|     |----
#  1 |     |
# ---|     |----
#  P |     |
# ---|-----|----


system("cls")    
while True:
    human_floor = int(input("Where is the Human? "))
    human_in_lift = input("Is Human in lift? y/n: ") == "y"
    call_lift = input("Call the lift? (y/n): ") == "y"
    
    if call_lift:
        if not human_in_lift:
            lift_target_floor = human_floor
        else:
            lift_target_floor = int(input("Where to go? "))
    
    else:
        lift_target_floor = lift_floor
         
    lift_open = False    
       
    if lift_floor < lift_target_floor:
        speed = + 1
        lift_dir = DIR_UP
    if lift_floor > lift_target_floor:
        speed = - 1
        lift_dir = DIR_DOWN
    if lift_floor == lift_target_floor:
        speed = 0
        
        
    ############### ANIMATION #################################
    while True:
        
        if not DIR_STOP:
            lift_floor += speed
# HW5
            if lift_floor == lift_target_floor:
                
              
                lift_open = True
                lift_dir = DIR_STOP
                    
                if human_in_lift:
                    human_in_lift = False
                    human_floor= lift_floor
                else:
                    human_in_lift= True

        ###############################  RENDER FRAME #################################
        system("cls") 
        a = "     "
        
        if building_roof:
            print(        "---|-----|----")
            print(        " R |     |    ")
# HW1   
        # if lift_open == True:
        #     print(       f" R |{a}|    ")
        else:
            print(        "---|-----|----")

        for floor in range(9,0,-1):  # (9,8,7,.....,0)

        #  4 | {a} |        floor +1

        # ---| {t} |----
        #  3 | {c} | {s}     floor 

        # ---| {t} |----     floor -1
            a = "     "
            c = "     "
            t = "     "
            s = "" 
            
            if floor == 9 and not building_roof:
                t = "-----"
            if floor == 1 and not building_floors:
                t = "-----"
            if floor == lift_floor +1:
                if lift_dir == DIR_UP:
                    a = "  ^  "
                elif lift_dir == DIR_STOP and lift_open:
                    a = " < > "
                elif lift_dir == DIR_DOWN:
                    a = "  v  " 
            elif floor == lift_floor:
                a = "|   |"
                t = "|---|"
  # HW2              
                if human_in_lift:
                    a = "| H |"
            elif floor == lift_floor -1:
                t = "|---|"

            if floor == human_floor and not human_in_lift:
                s = " H"
            else:
                s = "    "

            print(f"---|{t}|----")        
            print(f"{floor:^3}|{a}|{s}")
# HW3
        if lift_floor == 1:
            t = "|---|"
        else: 
            t = "     "

        if building_parking:
            print(        f"---|{t}|----")
            print(        " P |     |    ")
            print(        "---|-----|----")
        ###############################  RENDER FRAME #################################
        sleep(1)
        if lift_floor != lift_target_floor:
            break
    ############## ANIMATION  #################################
    sleep(.5)
    
    
