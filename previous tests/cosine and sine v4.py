import math
play = False
replay = True
triangle = input("What kind of triangle are you working with (right angled/regular)? ")
if triangle == "regular":
	regular_triangle = open("D:\\not photography\\Triangle Program\\triangle_notation.txt","r")
	print(regular_triangle.read())
	side_or_angle = input("What are you looking for (side/angle)? ")
	side_or_angle = side_or_angle.lower()
	if side_or_angle == "side":
		side = input("Which side are you looking for? ")
		matching = input("Do you have a matching pair? ")
		print("If you have a matching pair, to find the missing side, you must also have the angle opposite the side you're looking for.")
		if matching == "y":
			if side == "a":
				angle = float(input("A: "))
			if side == "b":
				angle = float(input("B: "))
			if side == "c":
				angle = float(input("C: "))
			angle = math.radians(angle)
			num_sides = float(input("How many sides do you have? "))
			#sine rule for sides
			if num_sides == 1:
				pair = input("Which pair do you have? Answer in the form [Angle,side]: ")
				if pair == "A,a":
					A = float(input("A: "))
					A = math.radians(A)
					a = float(input("a: "))
					missing_side = math.sin(angle)*(a/math.sin(A))
					print(side+": "+str(missing_side))
				if pair == "B,b":
					B = float(input("B: "))
					B = math.radians(B)
					b = float(input("b: "))
					missing_side = math.sin(angle)*(b/math.sin(B))
					print(side+": "+str(missing_side))
				if pair == "C,c":
					C = float(input("C: "))
					C = math.radians(C)
					c = float(input("c: "))
					missing_side = math.sin(angle)*(c/math.sin(C))
					print(side+": "+str(missing_side))
			#cosine rule for sides
			if num_sides == 2:
				if side == "a":
					b = float(input("b: "))
					c = float(input("c: "))
					missing_side = math.sqrt((b*b)+(c*c)-(2*b*c*math.cos(angle)))
					print(side+": "+str(missing_side))
				if side == "b":
					a = float(input("a: "))
					c = float(input("c: "))
					missing_side = math.sqrt((a*a)+(c*c)-(2*c*a*math.cos(angle)))
					print(side+": "+str(missing_side))
				if side == "c":
					a = float(input("a: "))
					b = float(input("b: "))
					missing_side = math.sqrt((a*a)+(b*b)-(2*a*b*math.cos(angle)))
					print(side+": "+str(missing_side))
		if matching == "n":
			print("You can't find a missing side of a regular triangle without a matching pair.")
	if side_or_angle == "angle":
		angle = input("Which angle are you looking for? ")
		angle = angle.upper()
		matching = input("Do you have a matching pair? ")
		#sine rule for angles
		if matching == "y":
			pair = input("Which pair do you have? Answer in the form [Angle,side]: ")
			if pair == "A,a":
				A = float(input("A: "))
				a = float(input("a: "))
				A = math.radians(A)
			if pair == "B,b":
				B = float(input("B: "))
				b = float(input("b: "))
				B = math.radians(B)
			if pair == "C,c":
				C = float(input("C: "))
				c = float(input("c: "))
				C = math.radians(C)
			print("If you have a matching pair, you must also have the side opposite the angle you're looking for, and the sine rule must be used.")
			if angle == "A":
				a = float(input("a: "))
				if pair == "B,b":
					A = math.asin((math.sin(B)/b)*a)
				if pair == "C,c":
					A = math.asin((math.sin(C)/c)*a)
				A = math.degrees(A)
				print("A: "+str(A)+"°")
			if angle == "B":
				b = float(input("b: "))
				if pair == "A,a":
					B = math.asin((math.sin(A)/a)*b)
				if pair == "C,c":
					B = math.asin((math.sin(C)/c)*b)
				B = math.degrees(B)
				print("B: "+str(B)+"°")
			if angle == "C":
				c = float(input("c: "))
				if pair == "A,a":
					C = math.asin((math.sin(A)/a)*c)
				if pair == "B,b":
					C = math.asin((math.sin(B)/b)*c)
				C = math.degrees(C)
				print("C: "+str(C)+"°")
		if matching == "n":
			print("If you don't have a matching pair, you must have all three sides, and must use the cosine rule.")
			a = float(input("a: "))
			b = float(input("b: "))
			c = float(input("c: "))
			if angle == "A":
				A = math.acos(((b*b)+(c*c)-(a*a))/(2*b*c))
				A = math.degrees(A)
				print("A: "+str(A)+"°")
			if angle == "B":
				B = math.acos(((a*a)+(c*c)-(b*b))/(2*a*c))
				B = math.degrees(B)
				print("B: "+str(B)+"°")
			if angle == "C":
				C = math.acos(((a*a)+(b*b)-(c*c))/(2*a*b))
				C = math.degrees(C)
				print("C: "+str(C)+"°")