
n1 , n2, n3 = map(int,input().split())
a = 1
cont = n1 
cont2 = n2
cont3 =n3

if n1 > n3:
    a = n1 
    n1 = n3 
    n3 = a 

if n1 > n2:
    a = n1 
    n1 = n2 
    n2 = a

if n2 > n3:
    a  = n3 
    n3 = n2 
    n2 = a

    

print(n1)
print(n2)
print(n3)

print()

print(cont)
print(cont2)
print(cont3)





