import math
play = False
replay = True
triangle = input("What kind of triangle are you working with (right angled/regular)? ")
if triangle == "regular":
    regular_triangle = open("triangle notation.txt","r")
    print(regular_triangle.read())
    side_or_angle = input("What are you looking for (side/angle)? ")
    side_or_angle = side_or_angle.lower()
    if side_or_angle == "side":
        side = input("Which side are you looking for (a/b/c)? ")
        matching = input("Do you have a matching pair (y/n)? ")
        #sine rule
        if matching == "y":
            #inputs for the matching pair
            pair = input("Which pair do you have? Answer in the form [Angle,side]: ")
            if pair == "A,a":
                A = int(input("A: "))
                A = math.radians(A)
                a = int(input("a: "))
                missing_side = math.sin(angle)*(a/math.sin(A))
                print(missing_side)
            if pair == "B,b":
                B = int(input("B: "))
                B = math.radians(B)
                b = int(input("b: "))
                missing_side = math.sin(angle)*(b/math.sin(B))
                print(missing_side)
            if pair == "C,c":
                C = int(input("C: "))
                C = math.radians(C)
                c = int(input("c: "))
                missing_side = math.sin(angle)*(c/math.sin(C))
                print(missing_side)
            print("If you have a matching pair, you should also have the angle opposite the side you're looking for.")
            if side == "a":
                angle = int(input("A: "))
                if pair == "B,b":
                    
            if side == "b":
                angle = int(input("B: "))
            if side == "c":
                angle = int(input("C: "))
            angle = math.radians(angle)
