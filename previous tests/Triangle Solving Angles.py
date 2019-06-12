import math
play = False
triangle = input("What kind of triangle are you working with (right angled/regular)? ")
if triangle == "right angled":
    looking_for = input("What are you looking for (side/angle)? ")
    right_angled = open('ra_labelled.txt','r')
    ra_triangle = right_angled.read()
    print("\n"+ra_triangle+"\n")
    right_angled.close()
    if looking_for == "angle":
        while play == False:
            looking_for_2 = input("Which angle are you looking for (X/Y)? ")
            if looking_for_2 == "X":
                sides = input("Which sides do you have (answer in the form [side,side])? ")
                #A and B
                if sides == "A,B" or sides == "B,A":
                    A = int(input("A: "))
                    B = int(input("B: "))
                    print("")
                    r_a = open('right angled triangle.txt','w')
                    r_a.write("""    |\\
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
                    r_a.close()
                    f = open('right angled triangle.txt','r')
                    check = f.read()
                    print(check)
                    f.close()
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
                    r_a = open('right angled triangle.txt','w')
                    r_a.write("""    |\\
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
                    r_a.close()
                    f = open('right angled triangle.txt','r')
                    check = f.read()
                    print(check)
                    f.close()
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
                    r_a = open('right angled triangle.txt','w')
                    r_a.write("""    |\\
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
                    r_a.close()
                    f = open('right angled triangle.txt','r')
                    check = f.read()
                    print(check)
                    f.close()
                    correct = input("Is this correct (y/n)? ")
                    if correct == "y":
                        X_value = math.degrees(math.acos((C/A)))
                        print("\nX = "+str(X_value)+"°")
                        play = True
                    elif correct == "n":
                        play = False
