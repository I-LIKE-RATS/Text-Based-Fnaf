import os
import time
speed = 5

stage = 0
dining = 0
cove = 0
hallL = 0
closet = 0
hallR = 0
backstage = 0
kitchen = 0
restroom = 0

cams = False

for i in range(round(902/speed) + 1):

    if restroom > 99:
        cams = True

    os.system("clear")

    print("###########################################################")
    print("#                                                         #")
    print("#   Remote security system 8.7                            #")
    print("#   Copywright (c) Afton Robotics                         #")
    print("#                                                         #")
    print("#                                                         #")

    if stage < 10:
        print("#   Stage-1A % " + str(stage) + "                                          #")
    elif stage > 9 and stage < 100:
        print("#   Stage-1A % " + str(stage) + "                                         #")
    else:
        print("#   Stage-1A % " + str(stage) + "                                        #")

    print("#                                                         #")

    if dining< 10:
        print("#   Dining-1B % " + str(dining) + "                                         #")
    elif dining > 9 and dining < 100:
        print("#   Dining-1B % " + str(dining) + "                                        #")
    else:
        print("#   Dining-1B % " + str(dining) + "                                       #")

    print("#                                                         #")

    if cove < 10:
        print("#   Pirate_Cove-1C % " + str(cove) + "                                    #")
    elif cove > 9 and cove < 100:
        print("#   Pirate_Cove-1C % " + str(cove) + "                                   #")
    else:
        print("#   Pirate_Cove-1C % " + str(cove) + "                                  #")

    print("#                                                         #")

    if hallL < 10:
        print("#   Left_Hall-2A-2B % " + str(hallL) + "                                   #")
    elif hallL > 9 and hallL < 100:
        print("#   Left_Hall-2A-2B % " + str(hallL) + "                                  #")
    else:
        print("#   Left_Hall-2A-2B % " + str(hallL) + "                                 #")

    print("#                                                         #")

    if closet < 10:
        print("#   Supply_Closet-3 % " + str(closet) + "                                   #")
    elif closet > 9 and closet < 100:
        print("#   Supply_Closet-3 % " + str(closet) + "                                  #")
    else:
        print("#   Supply_Closet-3 % " + str(closet) + "                                 #")

    print("#                                                         #")

    if hallR < 10:
        print("#   Right_Hall-4A-4B % " + str(hallR) + "                                  #")
    elif hallR > 9 and hallR < 100:
        print("#   Right_Hall-4A-4B % " + str(hallR) + "                                 #")
    else:
        print("#   Right_Hall-4A-4B % " + str(hallR) + "                                #")

    print("#                                                         #")

    if backstage < 10:
        print("#   Backstage-5 % " + str(backstage) + "                                       #")
    elif backstage > 9 and backstage < 100:
        print("#   Backstage-5 % " + str(backstage) + "                                      #")
    else:
        print("#   Backstage-5 % " + str(backstage) + "                                     #")

    print("#                                                         #")

    if kitchen < 10:
        print("#   Kitchen-6 % " + str(kitchen) + "                                         #")
    elif kitchen > 9 and kitchen < 100:
        print("#   Kitchen-6 % " + str(kitchen) + "                                        #")
    else:
        print("#   Kitchen-6 % " + str(kitchen) + "                                       #")

    print("#                                                         #")
    
    if restroom < 10:
        print("#   Restroom-7 % " + str(restroom) + "                                        #")
    elif restroom > 9 and restroom < 100:
        print("#   Restroom-7 % " + str(restroom) + "                                       #")
    else:
        print("#   Restroom-7 % " + str(restroom) + "                                      #")
 
    print("#                                                         #")
    if not cams:
        print("#   Cams online: False                                    #")
    else:
        print("#   Cams online: True                                     #")
    
    print("#                                                         #")
    print("#                                                         #")
    print("###########################################################")

    if not stage == 100:
        stage += speed
    elif not dining == 100:
        dining += speed
    elif not cove == 100:
        cove += speed
    elif not hallL == 100:
        hallL += speed
    elif not closet == 100:
        closet += speed
    elif not hallR == 100:
        hallR += speed
    elif not backstage == 100:
        backstage += speed
    elif not kitchen == 100:
        kitchen += speed
    elif not restroom == 100:
        restroom += speed

time.sleep(1)