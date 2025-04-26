i = int(input())


if i >= 365:
    ano = i // 365 
    restomes = (i % 365) 
    mes = restomes // 30 
    if restomes >= 30 :
         dia = restomes - (mes * 30)
    print(f"{ano} ano(s)")
    print(f"{mes} mes(es)")
    print(f"{dia} dia(s)")

elif i < 365 and i >= 30:
    restomes = (i % 365) 
    mes = restomes // 30 
    if restomes >= 30 :
         dia = restomes - (mes * 30)
    ano = 0
    print(f"{ano} ano(s)")
    print(f"{mes} mes(es)")
    print(f"{dia} dia(s)")
else:
    ano = 0 
    mes =0
    print(f"{ano} ano(s)")
    print(f"{mes} mes(es)")
    print(f"{i} dia(s)")
     