def po2(n):
  if n <= 0:
      return False
  return (n & (n - 1)) == 0

badapple = int(input("Nagarete ku toki no naka de demo "))
if po2(badapple) == False:
   print("Kedarusa ga hora guru guru mawatte (no)")
else:
   print("Watashi kara hana reru kokoro mo (ye)")