# The first way to solve the problem
import math 

def factorial_module(num):
	return math.factorial(num)

# Second way to apply logic

def factorial_logic(num):
	#We’ve added def as we have started a function next we’ve written the name of the function and lastly num is the variable.
	ans = 1 
	#Here we have defined a variable named ans and assigned the value 1 to it.
	if num == 0:
		return ans
	#We’re telling python if the number is 0 then return the 1 as the answer.
	else:
		for a in range (num):
            ans *= a + 1
	return ans
	#Python has been ordered that if the number is not zero then find all the numbers before the given number and multiply them all and add one or simply calculate the factorial and return the number.
