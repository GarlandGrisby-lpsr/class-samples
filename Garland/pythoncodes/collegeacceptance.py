print("How old are you?")
age = int(input())

print("whats your GPA?")
GPA = float(input())

#if GPA is over 3.0 and age is over 16, accept
if GPA > 3.0 and age > 16:
	print("congrats. you're in!!!")
else:
	print("sorry' guess youll have to go to harvard instead")
