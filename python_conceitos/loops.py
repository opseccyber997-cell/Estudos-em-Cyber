        #LOOP WHILE
#contador = 10
#while contador >=1:
#    print(f"Contagem atual + {contador}")
#    contador-=1

#senha = "calabreso123"
#tentative_senha = ""
#while senha != tentative_senha:
#    tentative_senha = input("Digite sua senha: ")
#    if tentative_senha != senha:
#        print("Senha Incorreta!")
#    else:
#        print("Acertou!")

#compras = ["Arroz", "Feijão", "leite", "Pão"]
#for item in compras:
#    print(f"Você precisa comprar: {item}")

numeros = [5, 6, 1, 0, 8, 7, 9, 2, 4]
for numero in numeros:
    if numero % 2 == 0:
        break
    print(numero)

# o "break" serve para que quando aquele valor seja verdadeiro, o loop "for" pare.
# o "continue" faz com que continue a lista mas nao chame o valor verdadeiro.