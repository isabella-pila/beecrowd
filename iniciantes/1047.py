horaInicial , minInicial , horaFinal, minFinal = map(int,input().split())

if horaInicial >= 12 and horaFinal < 12:
   totalinicio = (horaInicial * 60) + minInicial
   totalfinal = (horaFinal * 60 ) + minFinal
   totaltudo = (24 * 60 - totalinicio ) + totalfinal
   horas = totaltudo // 60
   minutos = totaltudo % 60
   print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
   
elif horaFinal == horaInicial and minFinal == minInicial:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")


elif horaInicial <= 12 and horaFinal > 12:
    totalinicio = (horaInicial * 60) + minInicial
    totalfinal = (horaFinal * 60 ) + minFinal
    total = (totalfinal  - totalinicio) 
    horas = total // 60
    minutos = total % 60
    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

elif horaInicial < 12  :
    totalinicio = (horaInicial * 60) + minInicial
    totalfinal = (horaFinal * 60 ) + minFinal
    total = (24 * 60 + totalfinal ) - totalinicio
    horas = total // 60
    minutos = total % 60
    if horas >= 24 :
        horas =  horas - 24
        print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
    else:
        print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
else:
    totalinicio = (horaInicial * 60) + minInicial
    totalfinal = (horaFinal * 60 ) + minFinal
    total = (totalfinal  - totalinicio) 
    horas = total // 60
    minutos = total % 60
    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")


