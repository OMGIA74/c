def oo(argh):
  res = 0
  for element in arr:
      res = res ^ element
  return res
arr = []
n = int(input("RNEAJA array size:"))
while(n):
  num = int(input("AANANA number:"))
  arr.append(num)
  n-=1

print("oo is", oo(arr))