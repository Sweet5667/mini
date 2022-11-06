total=0
while True:
	num1=float(input("enter your first no: "))
	num2=float(input("enter your second no: "))
	operation=input("""enter your choice
addition press +
subtraction press -
multiplication press *
division press /
floor division press //
modulas press %
power operator ** :""")
	if operation=="+":
		total=num1+num2
	elif operation=="-":
		total=num1-num2
	elif operation=="*":
		total=num1*num2
	elif operation=="/":
		total=num1/num2
	elif operation=="//":
		total=num1//num2
	elif operation=="%":
		total=num1%num2
	elif operation=="**":
		total=num1**num2		
	else:
		print("please enter correct input")
		
	print(total)
	again=input("press y for another calculation")
	if again.upper()!="Y":
		break
