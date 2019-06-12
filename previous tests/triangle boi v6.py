import math
play = False
replay = True
while replay == True:
    triangle = input("What kind of triangle are you working with (right angled/regular)? ")
    if triangle == "regular":
        #opens a text file of a regular triangle
        regular_triangle = open("triangle notation.txt","r")
        print(regular_triangle.read())
        side_or_angle = input("What are you looking for (side/angle)? ")
        side_or_angle = side_or_angle.lower()
        #code to find a missing side
        if side_or_angle == "side":
            side = input("Which side are you looking for? ")
            matching = input("Do you have a matching pair? ")
            #sine rule for side
            if matching == "y":
                print("If you have a matching pair, you also have the angle opposite the side you're looking for.")
                if side == "a":
                    angle = int(input("A: "))
                if side == "b":
                    angle = int(input("B: "))
                if side == "c":
                    angle = int(input("C: "))
                angle = math.radians(angle)
                #inputs for the matching pair
                pair = input("Which pair do you have? Answer in the form [Angle,side]: ")
                if pair == "A,a":
                    A = int(input("A: "))
                    A = math.radians(A)
                    a = int(input("a: "))
                    missing_side = math.sin(angle)*(a/math.sin(A))
                    print(side+": "+str(missing_side))
                if pair == "B,b":
                    B = int(input("B: "))
                    B = math.radians(B)
                    b = int(input("b: "))
                    missing_side = math.sin(angle)*(b/math.sin(B))
                    print(side+": "+str(missing_side))
                if pair == "C,c":
                    C = int(input("C: "))
                    C = math.radians(C)
                    c = int(input("c: "))
                    missing_side = math.sin(angle)*(c/math.sin(C))
                    print(side+": "+str(missing_side))
    if triangle == "right angled":
        looking_for = input("What are you looking for (side/angle)? ")
        if looking_for == "side":
            right_angled = open('E:\\not photography\\Triangle Program\\ra_pythagoras_labelled.txt','r')
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
                if which_angle == "y":
                    Y = int(input("Y: "))
                    Y = math.radians(Y)
                    if which_side == "a":
                        A = int(input("A: "))
                        if side == "b":
                            B = A/math.tan(Y)
                            print("B: "+str(B))
                        if side == "c":
                            C = A/math.sin(Y)
                            print("C: "+str(Y))
                    if which_side == "b":
                        B = int(input("B: "))
                        if side == "a":
                            A = B*math.tan(Y)
                            print("A: "+str(A))
                        if side == "c":
                            C = B/math.cos(Y)
                            print("C: "+str(C))
                    if which_side == "c":
                        C = int(input("C: "))
                        if side == "a":
                            A = C*math.sin(Y)
                            print("A: "+str(A))
                        if side == "b":
                            B = C*math.cos(Y)
                            print("B: "+str(B))
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
                right_angled = open('E:\\not photography\\Triangle Program\\ra_labelled.txt','r')
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
                        print("")
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
                        print("")
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
    replay_ = input("Again (y/n)? ")
    replay_ = replay_.lower()
    if replay_ == "y":
        replay = True
        play = False
    if replay_ == "n":
        replay = False
