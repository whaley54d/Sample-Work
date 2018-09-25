import sys
class Math:
	def __init__(this):
		this.initialize_values()
	
	def initialize_values(this):
		this.x = 0
		this.y = 0
	def reset_values(this, x, y):
		this.x = 0
		this.y = 0
	def addition(this, x, y):
		z = x + y
		return z
	def subtracton(this, x, y):
		z = x + (y * -1)
		return z
	def multiplication(this, x, y):
		if y == 0: 
			return 0
		else:
			return x + this.multiplication(x, y-1)
	def division(this, x, y):
		if x == 0: return 0
		else:
			return ((1/y)) + this.division(x-1, y)
math_a = Math()
a1 = math_a.addition(4,5)
a2 = math_a.subtracton(4,5)
a3 = math_a.multiplication(4,5)
a4 = math_a.division(4,5)


print(a1, " ", a2, " ", a3, " ", a4)