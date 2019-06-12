import math
play = False
replay = True
while replay == True:
    triangle = input("What kind of triangle are you working with (right angled/regular)? ")
    if triangle == "right angled":
        looking_for = input("What are you looking for (side/angle)? ")
        if looking_for == "side":
            right_angled = open('ra_pythagoras_labelled.txt','r')
            ra_triangle = right_angled.read()
            print("\n"+ra_triangle)
            right_angled.close()
            side = input("Which side are you looking for? ")
            side = side.lower()
            angle = input("Do you have an angle (y/n)? ")
            angle = angle.lower()
            if angle == "y":
                which_angle = input("Which angle do you have (X/Y)? ")
                which_side = input("Which side do you have (A,B,C)? ")
                which_angle = which_angle.lower()
                which_side = which_side.lower()
                if which_angle == "x":
                    X = int(input("X: "))
                    X = math.radians(X)
                    if which_side == "a":
                        A = int(input("A: "))
                        if side == "c":
                            C = A/math.cos(X)
                            print("C: "+str(C))
                        if side == "b":
                            B = A*math.tan(X)
                            print("B: "+str(B))
                    if which_side == "b":
                        B = int(input("B: "))
                        if side == "a":
                            A = B/math.tan(X)
                            print("A: "+str(A))
                        if side == "c":
                            C = B/math.sin(X)
                            print("C: "+str(C))
                    if which_side == "c":
                        C = int(input("C: "))
                        if side == "a":
                            A = C*math.cos(X)
                            print("A: "+str(A))
                        if side == "b":
                            B = C*math.sin(X)
                            print("B "+str(B))
            if angle == "n":
                if side == "a":
                    B = int(input("B: "))
                    C = int(input("C: "))
                    A = math.sqrt((C*C)-(B*B))
                    print("A: "+str(A))
                if side == "b":
                    A = int(input("A: "))
                    C = int(input("C: "))
                    B = math.sqrt((C*C)-(A*A))
                    print("B: "+str(B))
                if side == "c":
                    A = int(input("A: "))
                    B = int(input("B: "))
                    C = math.sqrt((A*A)+(B*B))
                    print("C: "+str(C))
        if looking_for == "angle":
            while play == False:
                right_angled = open('ra_labelled.txt','r')
                ra_triangle = right_angled.read()
                print("\n"+ra_triangle)
                right_angled.close()
                looking_for_2 = input("Which angle are you looking for (X/Y)? ")
                looking_for_2 = looking_for_2.lower()
                sides = input("Which sides do you have (answer in the form [side,side])? ")
                #code to find X angle
                if looking_for_2 == "x":
                    #A and B
                    if sides == "A,B" or sides == "B,A":
                        A = int(input("A: "))
                        B = int(input("B: "))
                        print("")
                        print("""    |\\
    | \\
    |  \\
    |   \\
    | X  \\
    |____/\\
    |      \\
    |       \\
    |        \\ """+str(A)+"""
    |         \\
    |          \\
    |           \\
    |            \\
    |           / \\
    |          /   \\
    |_ _ _ _ _/_ _ _\\

           """+str(B)+"""
                        """)
                        correct = input("Is this correct (y/n)? ")
                        if correct == "y":
                            X_value = math.degrees(math.asin(B/A))
                            print("\nX = "+str(X_value)+"°")
                            play = True
                        elif correct == "n":
                            play = False
                    #B and C
                    if sides == "B,C" or sides == "C,B":
                        B = int(input("B: "))
                        C = int(input("C: "))
                        print("")
                        print("""    |\\
    | \\
    |  \\
    |   \\
    | X  \\
    |____/\\
    |      \\
    |       \\
"""+str(C)+"""  |        \\
    |         \\
    |          \\
    |           \\
    |            \\
    |           / \\
    |          /   \\
    |_ _ _ _ _/_ _ _\\

           """+str(B)+"""
                        """)
                        correct = input("Is this correct (y/n)? ")
                        if correct == "y":
                            X_value = math.degrees(math.atan(B/C))
                            print("\nX = "+str(X_value)+"°")
                            play = True
                        elif correct == "n":
                            play = False
                    #A and C
                    if sides == "A,C" or sides == "C,A":
                        A = int(input("A: "))
                        C = int(input("C: "))
                        print("""    |\\
    | \\
    |  \\
    |   \\
    | X  \\
    |____/\\
    |      \\
    |       \\
"""+str(C)+"""  |        \\ """+str(A)+"""
    |         \\
    |          \\
    |           \\
    |            \\
    |           / \\
    |          /   \\
    |_ _ _ _ _/_ _ _\\

                        """)
                        correct = input("Is this correct (y/n)? ")
                        if correct == "y":
                            X_value = math.degrees(math.acos((C/A)))
                            print("\nX = "+str(X_value)+"°")
                            play = True
                        elif correct == "n":
                            play = False
                #code to find Y angle
                if looking_for_2 == "y":
                    #A and B
                    if sides == "A,B" or sides == "B,A":
                        A = int(input("A: "))
                        B = int(input("B: "))
                        print("")
                        print("""    |\\
    | \\
    |  \\
    |   \\
    |    \\
    |____/\\
    |      \\
    |       \\
    |        \\ """+str(A)+"""
    |         \\
    |          \\
    |           \\
    |            \\
    |           / \\
    |          / Y \\
    |_ _ _ _ _/_ _ _\\

           """+str(B)+"""
                        """)
                        correct = input("Is this correct (y/n)? ")
                        if correct == "y":
                            Y_value = math.degrees(math.acos(B/A))
                            print("\nY = "+str(Y_value)+"°")
                            play = True
                        elif correct == "n":
                            play = False
                    #B and C
                    if sides == "B,C" or sides == "C,B":
                        B = int(input("B: "))
                        C = int(input("C: "))
                        print("")
                        print("""    |\\
    | \\
    |  \\
    |   \\
    |    \\
    |____/\\
    |      \\
    |       \\
"""+str(C)+"""  |        \\
    |         \\
    |          \\
    |           \\
    |            \\
    |           / \\
    |          / Y \\
    |_ _ _ _ _/_ _ _\\

           """+str(B)+"""
                        """)
                        correct = input("Is this correct (y/n)? ")
                        if correct == "y":
                            Y_value = math.degrees(math.atan(C/B))
                            print("\nY = "+str(Y_value)+"°")
                            play = True
                        elif correct == "n":
                            play = False
                    #A and C
                    if sides == "A,C" or sides == "C,A":
                        A = int(input("A: "))
                        C = int(input("C: "))
                        print("""    |\\
    | \\
    |  \\
    |   \\
    | X  \\
    |____/\\
    |      \\
    |       \\
"""+str(C)+"""  |        \\ """+str(A)+"""
    |         \\
    |          \\
    |           \\
    |            \\
    |           / \\
    |          /   \\
    |_ _ _ _ _/_ _ _\\

                        """)
                        correct = input("Is this correct (y/n)? ")
                        if correct == "y":
                            Y_value = math.degrees(math.asin((C/A)))
                            print("\nY = "+str(Y_value)+"°")
                            play = True
                        elif correct == "n":
                            play = False
    else:
        print("Please enter a valid answer.")
    replay_ = input("Again (y/n)? ")
    replay_ = replay_.lower()
    if replay_ == "y":
        replay = True
        play = False
    if replay_ == "n":
        replay = False
