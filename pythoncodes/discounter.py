# find out price from the user
print("what is the price?")
price = int(input())


# calculate the discount price
discount_price = .9 * price

# if the user gets a discount, tell them.
# if not tell them.
if price > 1000:
	print("Your price is " + str(discount_price))
else:
	print("sorry you dont have enough cents")
