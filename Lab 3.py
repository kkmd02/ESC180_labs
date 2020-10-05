#have to do cd Downloads/Class/ECS180/Assignments
#pwd = print current directory
#when importing should run as a script

# import Calculator
# if __name__ == '__main__':
#     Calculator.initialize()
#     Calculator.add(42)
#     if Calculator.get_current_value() == 42:
#       print("Test 1 passed")
#     else:
#       print("Test 1 failed")

##Problem 2
def sum_cubes (number):
  total = 0
  for i in range (0, number + 1):
    total = total + i**3
  return total

def cubes_using_squares (number):
  total = 0
  inside = 0
  for i in range (0, number + 1):
    inside += i
  total = inside**2
  return total

def check_sum(n):
  if sum_cubes(n) == cubes_using_squares(n):
    return True
  else:
    return False

def check_sums_up_to_n(N):
  for i in range (0, N + 1):
    if check_sum(i) == False:
      return False
    else:
      return True


#is there a way to check code if it should always return true

## why does this loop not work
def Leibniz(n):
    fraction = 0
    for i in range (0, n + 1):
        numerator = (-1)**i
        denom = 2 * i + 1
        fraction += (numerator / denom)
    return fraction

Leibniz(10)

## why does this work
def leibniz(n):
    fraction = 0
    i = 0
    while i <= n:
        numerator = (-1)**i #need the brackets
        denom = 2 * i + 1
        fraction += numerator / denom
        i += 1
    return fraction

def pi_approx(n):
    quart_pi = leibniz(n)
    return quart_pi * 4

pi_approx (10000)



