import math
side = input("Which side are you looking for? ")
side = side.lower()
which_angle = input("Which angle do you have (X/Y)? ")
which_side = input("Which side do you have (A,B,C)? ")
which_angle = which_angle.lower()
which_side = which_side.lower()
if which_angle == "x":
    X = int(input("X: "))
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
