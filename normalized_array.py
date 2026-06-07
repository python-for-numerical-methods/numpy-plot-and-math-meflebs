def factors(x):
  f_list = []
  for i in range(1, x + 1):
    if x % i == 0:
      f_list.append(i)

  return f_list
#check your code
print(factors(6))
print(factors(17))
print(factors(24))
print(factors(48))
