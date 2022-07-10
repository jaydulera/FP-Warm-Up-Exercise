def getFrequency(arr):
  freq = [0] * 101
  for element in arr:
    freq[element] += 1
  return freq

array = [1 , 3 , 5 , 7 , 9, 1 , 3 , 5 , 7 , 9]
print(getFrequency(array))
