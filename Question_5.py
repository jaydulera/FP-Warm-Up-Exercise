def solve(left , right):
  for i in range(left , right):
    res = 0
    if(i == power(i)):
      res += i
  return res

def power(num):
  sum = 0
  for element in str(num):
    sum += int(element) ** 5
  return sum


print(solve(2 , 1000))
