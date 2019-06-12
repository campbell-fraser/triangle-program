angle = input("angle: ")
f = open('right angled triangle.txt','w')
f.write("""|\\
| \\
|  \\
|   \\
| """+str(angle)+""" \\
|____/\\
|      \\
|       \\
|        \\
|         \\
|          \\
|           \\
|            \\
|           / \\
|          /   \\
|_ _ _ _ _/_ _ _\\
""")
f.close()
f = open('right angled triangle.txt','r')
triangle = f.read()
print(triangle)
f.close()
