#Debugging activity Mia Carozza

#Code Snippet 1:
# Incorrect: Divie by zero error
x = 10
y = 2
result = x / y
print("Result:", result)

#Code Snippet 2:
# Incorrect: index out of range error
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers) - 1):
   print(numbers[i])


#Code Snippet 3:
# Incorrect: syntax error in function definition
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area
 
radius = 5
print(calculate_area(radius))



#Code Snippet 4:
# Incorrect: syntax error in if statement and function definition
def is_even(number):
   if number % 2 == 0 :
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))


# Code Snippet 5:
# Incorrect: syntax error in for loop
for i in range(5):
   print(i)


   #Code Snippet 6:
# Incorrect: needed f string for string concatenation
def greet(name):
   return f"Hello, {name}"
 
print(greet("Alice"))


#Code Snippet 7:
# Incorrect: indentation error in for loop
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
   sum += number
print("Sum of numbers:", sum)



#Code Snippet 8:
# Incorrect: n-1 not n+1
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
 
print(factorial(5))



#Code Snippet 9:
# Incorrect: Needed parentheses for the or condition
name = input("Enter your name: ")
if name == ("Alice" or "Bob"):
   print("Hello, " + name)
else:
   print("Hello, stranger!")


   #Code Snippet 10:
# Incorrect: division by zero error
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 2
print(divide_numbers(num1, num2))
















