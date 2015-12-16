print("Enter amount of purchases, in cents")
y = raw_input()
cents = int(y)
yycent = int(cents * .10)
yx = (yycent)
zx = str(yx)
yxcent = (cents - yycent)
zyz = str(yxcent)
if y >= 10:
	 print("You spent over $10! Your final price is" + zyz + "cents.") 
else:
   print("Sorry, you have no discount")
