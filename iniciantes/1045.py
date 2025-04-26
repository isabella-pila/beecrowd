a , b, c = map(float, input().split())
num = 1 

if a < b:
    num = b
    b = a
    a = num
if a < c:
    num = c
    c = a
    a = num 
if b < c:
    num = c
    c = b 
    b = num 
if a >= b+c:
    print("NAO FORMA TRIANGULO")
elif a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")
elif a**2 > b**2 + c**2:
    print("TRIANGULO OBTUSANGULO")

elif a**2 < b**2 + c**2:
    print("TRIANGULO ACUTANGULO")

if a == b and b == c and a==c:
    print("TRIANGULO EQUILATERO")
elif (a == b) or (b == c ) or (a==c):
    print("TRIANGULO ISOSCELES")


