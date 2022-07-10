def intersection(arr1 , arr2):
  left = 0
  right = 0
  result = []
  while(left < len(arr1) and right < len(arr2)):
    if arr1[left] == arr2[right]:
      result.append(arr1[left])
      left += 1
      right += 1
    elif arr1[left] > arr2[right]:
      right += 1
    else:
      left += 1
  return result

a1 = [1 , 3 , 5]
a2 = [1 , 2 , 4 , 5]
print(intersection(a1 , a2))
