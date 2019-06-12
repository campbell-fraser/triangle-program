A = input("A: ")
B = input("B: ")
f = open('right angled triangle.txt','w')
f.write("""    |\\
    | \\
    |  \\
    |   \\
    |    \\
    |____/\\
    |      \\
    |       \\
[C] |        \\ """+str(A)+"""
    |         \\
    |          \\
    |           \\
    |            \\
    |           / \\
    |          /   \\
    |_ _ _ _ _/_ _ _\\

           """+str(B)+"""
""")
f.close()
f = open('right angled triangle.txt','r')
triangle = f.read()
print(triangle)
f.close()
