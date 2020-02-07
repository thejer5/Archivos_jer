def collatz(n):
   print(int(n))
   if n == 1:
      return 1
   if n % 2 == 0:
      collatz(n/2)
   else:
      collatz(n * 3 + 1)
print(collatz(100))