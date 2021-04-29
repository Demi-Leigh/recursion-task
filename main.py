#Recursion Task
#Writing a fucntion that returns first 20 Fibonacci numbers
def fibonacci(number):
   if number <= 1:
       return number
   else:
       return(fibonacci(number - 1) + fibonacci(number - 2))
# take input from the user
amount_of_numbers = 20
for i in range(amount_of_numbers):
       print(fibonacci(i), end=" g")

