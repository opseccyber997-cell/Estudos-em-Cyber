def ola(nome):
    print(f"Olá, {nome}")

# ----------------------------------------------------------------------

def somar(n1, n2):
    resultado = n1 + n2
    return resultado

# Variáveis criadas dentro de uma função só podem ser usadas na função.

def cumprimento(nome):
    print(f"Olá, {nome}!")

# ----------------------------------------------------------------------

# Tudo que está dentro deste "if" só roda quando você executa ESTE arquivo
# direto (python funcao.py). Quando outro arquivo faz "from funcao import somar"
# (como o modulos.py), este bloco é ignorado e o input() não aparece.
if __name__ == "__main__":
    nome_inserido = input("Digite seu nome: ")
    ola(nome_inserido)

    resultado_da_soma = somar(5, 7)
    print(f"Resultado: {resultado_da_soma}")
