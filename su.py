

"""n,b,c=map(int,input().split())
if 0<=( n and b and c )<360:
  g=n+b+c
  if g==180:
    print("Yes")
  else:
    print("No")"""

"""n,b,c=map(int,input().split())
if 0<( n or b or c )<360:
  g=n+b+c
  if g==180:
    print("Yes")
  else:
    print("No")"""

n,b,c=map(int,input().split())
if 0<( n and b and c )<360:
  g=n+b+c
  if g==180:
    print("Yes")
  else:
    print("No")
else:
  print("No")