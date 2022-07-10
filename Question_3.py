import sys
def getMax(arr):
  maxOne = - sys.maxsize - 1
  maxTwo = - sys.maxsize - 1
  for element in arr:
    if element > maxOne:
      maxTwo = maxOne
      maxOne = element
    elif element > maxTwo:
      maxTwo = element
  return [maxOne , maxTwo]


array = [1 , 2 , 3 , 4, 5, 6, 7, 8, 9]
print(getMax(array))
