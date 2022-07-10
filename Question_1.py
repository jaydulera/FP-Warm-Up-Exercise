def reverse(arr):
  if len(arr) < 2:
    return arr
  else:
    left = 0;
    right = len(arr) - 1
    while left < right:
      temp = arr[left]
      arr[left] = arr[right]
      arr[right] = temp
      left += 1
      right -= 1
    return arr

str = ["a" , "b" , "c"]
print(reverse(str))
