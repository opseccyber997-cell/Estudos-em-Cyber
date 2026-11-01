produto1 = float(input("Digite um preço: "))
produto2 = float(input("Digite outro preço: "))
produto3 = float(input("Digite mais um preço: "))

if produto1 <= produto2 and produto1 <= produto3:
    print(f"O mais barato e recomendado é o de {produto1}")
elif produto2 <= produto1 and produto2 <= produto3:
    print(f"O mais barato e recomendado é o de {produto2}")
else:
    print(f"O mais barato e recomendado é o de {produto3}") 

# O programa pede ao usuário digitar três diferentes preços de um produto e o programa recomenda imprimindo o mais barato entre eles.