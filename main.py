def suma(n):
  if(n<9):
    return n
  else:
    return n%10+suma(n//10)
n=int(input("enter a number:"))
print("suma cifrelor:")
print(suma(n))