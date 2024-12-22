def add(a, b):
  answer = a + b
  return answer

def subtract(a, b):
  answer = a - b
  return answer

def multiply(a, b):
  answer = a * b
  return answer

def divide(a, b):
  answer = a / b
  return answer

def exp(a, b):
  answer = pow(a, b)
  return answer

a = int(input('Enter number a: '))
b = int(input('Enter number b: '))

print('\na + b =', add(a, b))
print('\na - b =', subtract(a, b))
print('\na x b =', multiply(a, b))
print('\na / b =', divide(a, b))
print('\na ^b =', exp(a, b))



