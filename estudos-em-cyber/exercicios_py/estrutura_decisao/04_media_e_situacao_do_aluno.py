nota1 = 10
nota2 = 10
nota_media = (nota1 + nota2) / 2

if nota_media == 10:
    print("Aprovado com Distinção!")
elif nota_media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")

# O programa analisa a nota do aluno. Ele junta as duas notas e divide por 2, adquirindo sua média. Caso a média do aluno for 10, o sistema imprime Aprovado com distinção, se for 7, 8 ou 9, o sistema imprime Aprovado, caso seja menor que 7, imprime Reprovado.