import math
replay = True
while replay == True:
	triangle = input("What kind of triangle are you working with (right angled/regular)? ")
	#code for regular triangle stuff
	if triangle == "regular":
		regular_triangle = open('D:\\not photography\\Triangle Program\\text files\\triangle_notation.txt','r')
		print(regular_triangle.read())
		side_or_angle = input("What are you looking for (side/angle)? ")
		side_or_angle = side_or_angle.lower()
		
		#side
		if side_or_angle == "side":
			side = input("Which side are you looking for? ")
			matching = input("Do you have a matching pair? ")
			if matching == "y":
				print("If you have a matching pair, to find the missing side, you must also have the angle opposite the side you're looking for.")
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
				print("You need to use the cosine rule.")
				if side == "a":
					angle = float(input("A: "))
				if side == "b":
					angle = float(input("B: "))
				if side == "c":
					angle = float(input("C: "))
				angle = math.radians(angle)
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
			#cosine rule for sides
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
	#code for right angled triangle stuff
	if triangle == "right angled":
		right_angled = open('D:\\not photography\\Triangle Program\\text files\\ra_pythagoras_labelled.txt','r')
		print("\n"+right_angled.read())
		right_angled.close()
		looking_for = input("What are you looking for (side/angle)? ")
		if looking_for == "side":
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
					X = float(input("X: "))
					X = math.radians(X)
					if which_side == "a":
						A = float(input("A: "))
						if side == "c":
							C = A/math.cos(X)
							print("C: "+str(C))
						if side == "b":
							B = A*math.tan(X)
							print("B: "+str(B))
					if which_side == "b":
						B = float(input("B: "))
						if side == "a":
							A = B/math.tan(X)
							print("A: "+str(A))
						if side == "c":
							C = B/math.sin(X)
							print("C: "+str(C))
					if which_side == "c":
						C = float(input("C: "))
						if side == "a":
							A = C*math.cos(X)
							print("A: "+str(A))
						if side == "b":
							B = C*math.sin(X)
							print("B "+str(B))
				if which_angle == "y":
					Y = float(input("Y: "))
					Y = math.radians(Y)
					if which_side == "a":
						A = float(input("A: "))
						if side == "b":
							B = A/math.tan(Y)
							print("B: "+str(B))
						if side == "c":
							C = A/math.sin(Y)
							print("C: "+str(Y))
					if which_side == "b":
						B = float(input("B: "))
						if side == "a":
							A = B*math.tan(Y)
							print("A: "+str(A))
						if side == "c":
							C = B/math.cos(Y)
							print("C: "+str(C))
					if which_side == "c":
						C = float(input("C: "))
						if side == "a":
							A = C*math.sin(Y)
							print("A: "+str(A))
						if side == "b":
							B = C*math.cos(Y)
							print("B: "+str(B))
			if angle == "n":
				if side == "a":
					B = float(input("B: "))
					C = float(input("C: "))
					A = math.sqrt((C*C)-(B*B))
					print("A: "+str(A))
				if side == "b":
					A = float(input("A: "))
					C = float(input("C: "))
					B = math.sqrt((C*C)-(A*A))
					print("B: "+str(B))
				if side == "c":
					A = float(input("A: "))
					B = float(input("B: "))
					C = math.sqrt((A*A)+(B*B))
					print("C: "+str(C))
		if looking_for == "angle":
				right_angled = open('D:\\not photography\\Triangle Program\\text files\\ra_labelled.txt','r')
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
						A = float(input("A: "))
						B = float(input("B: "))
						X_value = math.degrees(math.asin(B/A))
						print("\nX = "+str(X_value)+"°")
					#B and C
					if sides == "B,C" or sides == "C,B":
						B = float(input("B: "))
						C = float(input("C: "))
						X_value = math.degrees(math.atan(B/C))
						print("\nX = "+str(X_value)+"°")
					#A and C
					if sides == "A,C" or sides == "C,A":
						A = float(input("A: "))
						C = float(input("C: "))
						X_value = math.degrees(math.acos((C/A)))
						print("\nX = "+str(X_value)+"°")
				#code to find Y angle
				if looking_for_2 == "y":
					#A and B
					if sides == "A,B" or sides == "B,A":
						A = float(input("A: "))
						B = float(input("B: "))
						Y_value = math.degrees(math.acos(B/A))
						print("\nY = "+str(Y_value)+"°")
					#B and C
					if sides == "B,C" or sides == "C,B":
						B = float(input("B: "))
						C = float(input("C: "))
						Y_value = math.degrees(math.atan(C/B))
						print("\nY = "+str(Y_value)+"°")
					#A and C
					if sides == "A,C" or sides == "C,A":
						A = float(input("A: "))
						C = float(input("C: "))
						Y_value = math.degrees(math.asin((C/A)))
						print("\nY = "+str(Y_value)+"°")
	replay_ = input("Again (y/n)? ")
	replay_ = replay_.lower()
	if replay_ == "y":
		replay = True
	if replay_ == "n":
		replay = False