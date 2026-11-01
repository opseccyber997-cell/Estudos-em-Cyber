# Estudos em Cyber BR

Aqui ficam as minhas anotações e exercícios de estudo para a minha carreira em cibersegurança.

**Observações:** tenho **13 anos** (em 2026) e já estou estudando porque eu realmente quero entrar nessa área. Sei um pouco de HTML e CSS bem básico e tenho alguma experiência com programação em Python. Meu inglês é **básico**, mas está indo para o intermediário, então já consigo ler alguns artigos nessa língua, já que a maior parte do conteúdo de cibersegurança está em inglês.

## O que eu estudei em geral

| Tema | Anotações neste repositório |
| --- | --- |
| Linux básico e comandos de rede no terminal | ✅ abaixo |
| Redes | ✅ abaixo (lista de tópicos) |
| Python | ✅ abaixo, nas pastas `python_conceitos` e `exercicios_py` |
| Fundamentos da Web | 🔜 em breve |
| Fundamentos de Segurança | 🔜 em breve |
| Segurança Web | 🔜 em breve |
| Ferramentas de Análise | 🔜 em breve |
| Blue Team | 🔜 em breve |
| Pentest e Red Team | 🔜 em breve |
| Cloud e Contêineres | 🔜 em breve |

## Estrutura do repositório

```
python_conceitos/   anotações com exemplos de cada conceito de Python
exercicios_py/      exercícios organizados por tema
```

Para rodar um arquivo: `python3 python_conceitos/loops.py` (no Windows, `python` em vez de `python3`).

---

## 🐧 Linux

Quanto ao Linux, ainda não me aprofundei muito: peguei a maioria dos comandos básicos e os comandos de rede. Como os profissionais da área geralmente usam **Kali** ou **Parrot**, achei melhor ir me acostumando aos poucos.

> Os comandos do Linux são escritos em **minúsculo**: o Linux diferencia maiúsculas de minúsculas.

### Navegação e alteração de arquivos

| Comando | O que faz |
| --- | --- |
| `mkdir` | Cria um novo diretório/pasta |
| `cd` | Entra em um diretório/pasta |
| `cd ..` | Volta um diretório (sai da pasta) |
| `ls` | Lista arquivos e pastas |
| `ls -l` | Lista com mais detalhes |
| `ls -a` | Lista todos os arquivos, inclusive os ocultos |
| `cat` | Mostra o conteúdo de um arquivo |
| `mv` | Move ou renomeia um arquivo ou pasta |
| `cp` | Copia um arquivo para outro lugar |
| `rm` | Apaga arquivos |
| `rmdir` | Apaga pastas vazias |
| `rm -rf` | Apaga a pasta e TUDO dentro dela, sem perguntar e sem lixeira. ⚠️ Use com muito cuidado! |

### Informações do sistema

| Comando | O que faz |
| --- | --- |
| `hostname` | Mostra o nome da máquina |
| `hostname -I` | Mostra o IP da máquina |
| `free -h` | Leitura rápida da memória |
| `ps aux` | Mostra todos os processos rodando no sistema |
| `kill PID` | Fecha um processo pelo **PID** (dá para ver o PID com `ps aux`) |
| `df -h` | Mostra quanto espaço livre há no disco |

### Permissões de arquivos

| Comando | O que faz |
| --- | --- |
| `chmod` | Muda as permissões de um arquivo ou diretório |
| `umask` | Define quais permissões são removidas **automaticamente** quando um arquivo ou diretório é criado |

Para entender como mudar permissões, eu tive que aprender a ler as permissões de um arquivo/pasta. Um exemplo:

```
drwxr-xr-x 2 usuário grupo 4096 fev 20 10:17
```

A primeira letra mostra o que é: como é um `d`, isso é um **diretório**. Depois vêm três grupos de três letras: as permissões do dono, do grupo e dos outros usuários.

**Essa tabela me ajudou muito!**

| Permissão | Binário | Decimal |
| --- | --- | --- |
| `---` | 000 | 0 |
| `--x` | 001 | 1 |
| `-w-` | 010 | 2 |
| `-wx` | 011 | 3 |
| `r--` | 100 | 4 |
| `r-x` | 101 | 5 |
| `rw-` | 110 | 6 |
| `rwx` | 111 | 7 |

---

## 🛜 Redes

- O que é uma rede
- LAN, WAN e internet
- IP e endereço MAC
- IPv4 e IPv6
- Gateway
- Máscaras de sub-rede
- Portas
- TCP e UDP
- DNS
- DHCP
- NAT
- HTTP e HTTPS
- Modelo TCP/IP
- Modelo OSI
- Comandos de rede no Linux

---

## 🐍 Python

### O que já tem neste repositório

- `python_conceitos/`: conceitos iniciais, condicionais, loops, funções, coleções (listas, tuplas e dicionários), módulos e bibliotecas
- `exercicios_py/`: exercícios de estrutura sequencial, de decisão e (em breve) de repetição

### Roadmap

**Fase 1: fundamentos essenciais**
- [x] Variáveis e tipos de dados (textos/strings, números/integers e booleanos)
- [x] Estruturas de decisão (`if`, `elif`, `else`): fazer o programa tomar decisões baseadas em regras
- [x] Estruturas de repetição (`for`, `while`): rodar o código várias vezes ou varrer listas e arquivos linha por linha
- [x] Listas e dicionários: organizar dados (como uma lista de senhas proibidas ou um dicionário de critérios)

**Fase 2: manipulação e bibliotecas básicas**
- [x] Funções (`def`): isolar pedaços de código para reutilizá-los
- [ ] Manipulação de textos (métodos de string): `.lower()`, `.upper()`, `.split()` e o operador `in`
- [ ] Expressões regulares (módulo `re`): criar "filtros" para encontrar padrões de texto (como e-mails, IPs e senhas). Esse é um superpoder do analista de segurança

**Fase 3: Python aplicado à segurança**
- [ ] Manipulação de arquivos (`open()`): essencial para abrir arquivos de log e ler relatórios
- [ ] Módulos nativos de rede e sistema: `socket` (conexões de rede), `os` e `sys` (interagir com o sistema operacional)
