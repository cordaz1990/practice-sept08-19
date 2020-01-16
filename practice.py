#conditional Expressions
if x > 0:
  y = math.log(x)
else:
  y = float('nan')
  
y = math.log(x) if x > 0 else float('nan')

def factor(n):
    if n == 0:
       return 1
    else:
       return n * factorial(n - 1)
      
def factorial(n)
     return 1 if n == 0 else n * factorial(n - 1)
