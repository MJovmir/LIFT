 # LIFT SIMULATION / realms simulation
# conditionals / looping / branching
# logic wrapping / indie-out
# logic

# HW1* write the logic for no ROOF and no PARKING
# HW2* write the logic for the Human inside the lift  
# HW2* write the logic for the LIFT TOP
from os import system 

DIR_UP   = -1
DIR_STOP = 0
DIR_DOWN = 1

building_roof = True
building_floors = 9
building_parking = True

lift_floor= 7
lift_open = False
lift_dir = DIR_STOP

human_floor = 3
human_in_lift = False



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


###############################  RENDER FRAME #################################

system("cls")
if building_roof:
    print(        "---|-----|----")
    print(        " R |     |    ")
    
for floor in range(9,0,-1):  # (9,8,7,.....,0)
    
    if floor == lift_floor -1:
        lb = "|---|"
    else:
        lb = "     "
              
    print(f"---|{lb}|----")
    
    if floor == human_floor and not human_in_lift:
        h = " H  "
    else:
        h = "    "
        
    if floor == lift_floor + 1:
        if lift_open: 
            l = " < > "
        else:
            if lift_dir == DIR_UP:
                l = "  ^  "
            elif lift_dir == DIR_DOWN:
                l = "  v  "
            else:
                l = "     "    
    else:
        l = "     "
    if floor == lift_floor:
        l = "|   |"
   
        
    
            
    print(f"{floor:^3}|{l}|{h}")
    
    
    
if building_parking:
    print(        "---|     |----")
    print(        " P |     |    ")
    print(        "---|-----|----")
###############################  RENDER FRAME #################################