num1 = int(input("Selecione um número: "))
num2 = int(input("Selecione um segundo número: "))
num3 = int(input("Selecione um terceiro número: "))

if num1 >= num2 and num1 >= num3:
    print(f"O número {num1} é maior que {num2} e {num3} ")
elif num2 >= num1 and num2 >= num3:
    print(f"O número {num2} é maior que {num1} e {num3}")
else:
    print(f"O número {num3} é maior que {num1} e {num2}")

# O sistema pede 3 números para o usuário digitar e imprime o maior entre os 3.