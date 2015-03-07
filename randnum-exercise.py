# import random

# def fizzbuzz(): #Puts everything indented in the function fizzbuzz()
# 	i = 0
# 	while i <= 50: #Make sure you add the ":"; while the variable i is less than or equal to 50, the code below executes
# 		i = random.randint(0, 50)
# 		if i % 5 == 0 and i % 3 == 0:
# 			print('fizzbuzz')
# 		elif i % 5 == 0:
# 			print('fizz')
# 		elif i % 3 == 0:
# 			print('buzz')
# 		else:
# 			print(i)
# 		i += 1 #Increase the variable 

# fizzbuzz() #Call the function at the end!



# def sum2(int_list):
# 	sum3 = 0
# 	for value in int_list:
# 		sum3 += value
# 	return sum3

# print(sum2([1, 2, 3,]))



# def fizzbuzz(num):
# 	i = 0
# 	while i <= num:
# 		if i % 5 == 0 and i % 3 == 0:
# 			print('fizzbuzz ' + str(i))
# 		elif i % 5 == 0:
# 			print('fizz ' + str(i))
# 		elif i % 3 == 0:
# 			print('buzz ' + str(i))
# 		else:
# 			print(i)
# 		i += 1

# fizzbuzz(50)



# def fizzbuzz(default_variable=50): #If you don't specify a variable, it will default to 50. If you do specify a variable, it will overrule 50
# 	i = 0
# 	while i <= default_variable:
# 		if i % 5 == 0 and i % 3 == 0:
# 			print('fizzbuzz ' + str(i))
# 		elif i % 5 == 0:
# 			print('fizz ' + str(i))
# 		elif i % 3 == 0:
# 			print('buzz ' + str(i))
# 		else:
# 			print(i)
# 		i += 1

# fizzbuzz(100)



# class SimpleClass:
# 	def __init__(self, some_var):
# 		self.bob = some_var
# 		self.dan = some_var + 1

# obj = SimpleClass(9)
# print(obj.bob)



class Product:
	def __init__(self, num1, num2):
		self.result = num1 * num2

class SquareNumber:
	def __init__(self, num):
		times = Product(num, num) #Called Product here so I can use the self.result method
		self.result = times.result

square_num = SquareNumber(20)
print(square_num.result)



#A simpler one step way to do the above:
class SquareNumber:
	def __init__(self, num):
		self.result = Product(num, num).result

square_num = SquareNumber(20)
print(square_num.result)



#Exercise using float
class Quotient:
	def __init__(self, num1, num2):
		self.result = float(num1) / float(num2)

quotient = Quotient(10, 20)
print(quotient.result) #0.5


#Using the Product class to prove the point of building upon other classes; you don't want to keep reinventing things and starting from scratch
class Quotient:
	def __init__(self, num1, num2):
		times = Product(float(num1), 1 / float(num2))
		self.result = times.result

		#Or you can condense it into one line
		self.result = Product(num1, 1/float(num2)).result

quotient = Quotient(10, 20)
print(quotient.result) #0.5

















