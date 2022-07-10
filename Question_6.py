def mostFrequent(arr):
  map = dict()
  for element in arr:
    if element in map.keys():
      map[element] += 1
    else:
      map[element] = 1
  count = 0
  freq = 0

  for key in map:
    if(count < map[key]):
      freq = key
      count = map[key]
  return key

array = [1 , 2 , 2 , 3, 3 , 3 , 4 , 4 , 4 , 4]
print(mostFrequent(array))
