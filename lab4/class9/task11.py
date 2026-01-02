n1 = int(input("1st number: "))
n2 = int(input("2st number: "))
n3 = int(input("3st number: "))

if (n1>n2 and n2>n3):
  print("N1 largest", n1)
elif (n2>n3 and n2>n1):
  print("N2 largest", n2)
else:
  print("N3 largest", n3)