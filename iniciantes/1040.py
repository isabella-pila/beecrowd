n1 , n2 ,n3 ,n4 = map(float,input().split())

media = (n1*2 + n2*3 + n3*4 + n4*1) / 10



if media >= 7.0:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")

elif media >= 5.0 and media <= 6.9 :
    
    n5 = float(input())
    mediafinal = (n5 + media) / 2
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    print(f"Nota do exame: {n5:.1f}")
    if mediafinal >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {mediafinal:.1f}")

elif media <= 4.9:
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")






