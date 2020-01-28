while True:
	try:
		amount = int(input("Enter the amount you wish to withdraw "))
		print("Collect your cash")
		break
	except ValueError:
		print("Enter a valid amount")