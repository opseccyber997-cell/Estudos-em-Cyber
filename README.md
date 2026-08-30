# Estudos em Cyber BR
Aqui está literalmente **TUDO QUE ESTUDEI**, para minha carreira de ser um cybersecurity.
OBSERVAÇÕES: Tenho **13 anos** no ano de 2026 e já estou estudando porque eu realmente quero entrar nessa área Sei um pouco de HTML e CSS bem básico e um pouco de experiência com programação em python, também tenho um inglês **básico** mas que está indo para o intermediário, então já consigo ler certo artigos nessa linguagem, já que a maioria do conteúdo de cybersecurity é tudo em inglês

## O QUE EU ESTUDEI EM GERAL
+ Linux Básico e Comandos de Rede no Terminal
+ Redes
+ Python
+ Fundamentos da Web
+ Fundamentos de Segurança
+ Segurança Web
+ Ferramentas de Análise
+ Blue Team
+ Pentest e Red Team
+ Cloud e Contêineres

## O QUE EU ESTUDEI DE LINUX  🐧 
Em questão ao Linux eu não me aprofundei muito, peguei a maioria dos comandos básicos e comandos de rede. Já que geralmente os profissionais dessa área usam o **Kali** ou **Parrot**... Então achei melhor já ir me sentindo confortável aos poucos.

### NAVEGAÇÃO E ALTERAÇÃO DE ARQUIVOS
+ MKDIR - Cria um Novo Diretório/Pasta
+ CD - Entra dentro de um Diretório/Pasta
+ CD .. - Volta um diretório, sair da pasta.
+ LS - Lista itens e pastas.
+ LS -L - Lista os itens mais detalhadamente.
+ LS -A - Lista todos os arquivos ocultos e normais.
+ CAT - Mostra o conteúdo de uma pasta
+ MV - Altera o nome de um arquivo ou pasta.
+ CP - Copia o arquivo para outro lugar.
+ RM - Apaga arquivos.
+ RMDIR - Apaga PAstas/Diretórios.
+ RM -RF - Apaga TUDO sem excessão.
+ MV - Altera o nome do arquivo ou da pasta.

### INFORMAÇÕES DO SISTEMA
+ HOSTNAME - Mostra o nome da Máquina.
+ HOSTNAME - MostrAa o IP da Máquina.
+ FREE -H - Leitura rápida de memória.
+ PS AUX - Mostra todos os processos rodando no sistema operacional.
+ KILL - Fecha um processo pelo **PID**. "É possível ver o PID de um processo pelo PS AUX."
+ DF -H - Mostra quanto espaço livre há na máquina e outra informações de memória.

### PERMISSÕES DE ARQUIVOS
+ CHMOD - Muda as permissões de um arquivos ou diretório
+ UMASK - Remove permissões **AUTOMATICAMENTE** quando for criado um arquivo ou diretório
Para eu entender como funciona para mudar as permissões, eu tive que aprender como funcionava e como lia as permissões de um arquivos/pasta. Um exemplo:
*drwxr-xr-x 2 usuário grupo 4096 fev 20 10:17*
A primeira letra representa o que é, mas como é um "d", isso seria um **DIRETÓRIO**


### ESSA TABELA ME AJUDOU MUITO!!!
| Permissão | Binário | Decimal |
| --- | --- | --- |
| ---... | 000 | 0 |
| --X | 001 | 1 |
| -W- | 010 | 2 |
| -WX | 011 | 3 |
| R-- | 100 | 4 |
| R-X | 101 | 5 |
| RW- | 110 | 6 |
| RWX | 111 | 7 |

## REDES  🛜
+ O que é uma rede
+ LAN, WAN e internet
+ IP e endereço MAC
+ IPV4 e IPV6
+ Gateway
+ Máscaras de Sub-rede
+ Portas
+ TCP e UDP
+ DNS
+ DHCP
+ NAT
+ HTTP e HTTPS
+ Modelo TCP/IP
+ Modelo OSI
+ Comandos de Rede no Linux
 
## PYTHON  🐍

 
Fase 1: Fundamentos EssenciaisVariáveis e Tipos de Dados: Entender como armazenar textos (Strings), números (Integers) e booleanos (True/False).Estruturas de Decisão (if, elif, else): Fazer o seu programa toma
 r decisões baseadas em regras.Estruturas de Repetição (for, while): Fazer o código rodar várias vezes ou varrer listas e arquivos linha por linha.Listas e Dicionários: Organizar dados (como a lista de senhas proibidas ou o dicionário de critérios).Fase 2: Manipulação e Bibliotecas BásicasFunções (def): Aprender a isolar pedaços de código para reutilizá-los.Manipulação de Textos (Métodos de String): Funções como .lower(), .upper(), .split() e o operador in.Expressões Regulares (Módulo re): Aprender a criar "filtros" mágicos para encontrar padrões de texto (como e-mails, IPs e senhas). Esse é o superpoder do analista de segurança.Fase 3: Python Aplicado à SegurançaManipulação de Arquivos (open()): Essencial para abrir arquivos de log e ler relatórios.Módulos Nativos de Rede e Sistemas: Conhecer bibliotecas como socket (para conexões de rede), os e sys (para interagir com o sistema operacional).
