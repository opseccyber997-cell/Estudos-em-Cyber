frutas = ["Maçã", "Banana", "Uva"]
frutas[1] = "Abacaxi"


# O Comando "append" serve para adicionar algo no fim de uma lista,
# Mas o "insert" adiciona algo em um lugar específico da lista.
# "remove" remove um valor.

frutas.append ("Morango")
frutas.insert(1, "Kiwi")
frutas.remove("Abacaxi")

# -------------------------------------------------------------------------

if "Maçã" in frutas:
    print("Tem maçã nas frutas!")
print(frutas)

# ------------------------------------------------------------------------

# As "tuplas" são praticamente listas, mas não podem ser modificadas.

cores = ("Vermelho", "Verde", "Azul")

# Tentar mudar uma tupla dá erro (TypeError). Por isso a linha abaixo fica
# comentada: tire o "#" para ver o erro acontecendo.
# cores[1] = "Amarelo"

minhas_tuplas = [("Maçã", "Banana"), ("Vermelho", "Verde")]
print(minhas_tuplas[1][0])


# DICIONÁRIO
dados= {"nome": "Lan Code", "idade": 22}
dados["idade"] = 23
print(dados)