factElement = int(input("Enter the element find the factorial : "))
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
if factElement < 0:
   print(" factorial does not exist for negative searchElementbers")
elif factElement == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", factElement, "is", recur_factorial(factElement))
