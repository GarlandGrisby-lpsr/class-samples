print("Enter amount of purchases, in cents")
cents = int(input())
cents = (cents / .10)
if cents > 1000:
	print("You spent over $10! Your final price is" + str(cents))
print("cents")
