cod , quant = map(float,input().split())


if cod == 1:
    resultado= 4.00 * quant 

elif cod == 2:
    resultado = 4.50 * quant

elif cod == 3:
    resultado= 5 * quant
elif cod == 4:
    resultado = 2* quant
elif cod == 5:
    resultado = 1.50* quant


print(f"Total: R$ {resultado:.2f}")
