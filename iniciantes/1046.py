comeco , fim = map(int,input().split())

if comeco >= 12 and fim < 12:
   n1= (24 -comeco  ) + fim
   print(f"O JOGO DUROU {n1} HORA(S)")

elif comeco == fim:
   print("O JOGO DUROU 24 HORA(S)")

elif comeco <= 12 and fim > 12:
   n1= (24 - comeco  ) - (24 - fim)
   print(f"O JOGO DUROU {n1} HORA(S)")
