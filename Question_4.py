def round(num):
  temp = num * 10
  if temp % 10 == 0:
    return num
  elif temp % 10 < 5:
    temp -= temp % 10
    return int(temp // 10)
  else:
    temp += temp % 10
    return int(temp // 10)

no = 8.6
print(round(no))
