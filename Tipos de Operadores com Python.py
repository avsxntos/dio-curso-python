#Adição, Subtração e Multiplicação
#Operadores Aritméticos


 # Adição
print(1 + 2)
# 3

# Subtração
print(10 - 2)
# 8

# Multiplicação
print(4 * 3)
# 12

# Divisão  e Divisão Inteira
# Divisão 
print(12 / 3)
# 4.0

# Divisão Inteira 
print(12 // 2)
# 6


# Módulo e exponenciação 
# Módulo 
print(10 % 3)
# 1

# Exponenciação
print(2 ** 3)
# 8




# Hierarquia de Cálculos

print(10 - 5 * 2)
# 0

print((10 - 5) * 2) # o parenteses tendo a ser feito antes, por conta de sua importancia
# 10

print(10 ** 2 * 2)
# 200

print(10 ** (2 * 2))
# 10000

print(10 / 2 * 4)
# 20.0

# Exemplo 
produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2) # % vai exibir o resto de sobra da conta
print(produto_1 ** produto_2)


# Operadores de Comparação
# Igualdade
saldo = 450
saque = 200

print(saldo == saque)
# False

print(saldo != saque) # este simbolo significa diferente
# True

# Maior que / maior ou igual

saldo = 450
saque = 200
print(saldo > saque)
#True

print(saldo >= saque)
# True

# Menor que / menor ou igual
print(saldo < saque)
# False

print(saldo <= saque)
# False


# Operadores de Atribuição

#Atribuição Simples
saldo = 500 

print(saldo)
# 500

# Atribuição de Adição

saldo = 500
saldo += 200

print(saldo)
# 700

# Atribuição de Subtração
saldo = 500
saldo =- 100

print(saldo)
# 400

# Atribuição de Multiplicação
saldo = 500
saldo *= 2

print(saldo)
# 1000

# Atribuição de Divisão
saldo = 500
saldo /= 5

print(saldo)
# 100.0

saldo = 500
saldo //= 5

print(saldo)
# 100


# Atribuição com Módulo
saldo = 500
saldo %= 480

print(saldo)
# 20

# Atribuição com Exponenciação
saldo = 80
saldo **= 2

print(saldo)
# 6400


# Operadores Lógicos
#Exemplo

saldo = 100
saque = 200
limite = 100

saldo >= saque
# true

saque <= limite
# false

# Operador Lógico E
saldo = 100
saque = 200
limite = 100

saldo >= saque and saque <= limite
# false


# Operador OU
saldo = 100
saque = 200
limite = 100

saldo >= saque or saque <= limite
# true

# Operador de Negação
contatos_emergencia = []

not 1000 > 1500
# true

not contatos_emergencia
# true

not "saque 1500;"
# false

not ""
# false

# Parenteses
# AND = PARA SER TRUE, TUDO TEM QUE SER TRUE
# OR = PARA SER TRUE, APENAS UM TEM QUE SER TRUE

saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
# true

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
#true


# Operadores de Identidade

# Exemplo
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print (curso is nome_curso)
# true

print (curso is not nome_curso)
# false

print (saldo is limite)
# true
 



 # Operadores de Assoociação - Eles são operadores utializados para verificar se um objeto está presente em uma sequência.

 #Exemplo
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

# Operador de associação, pra verificar se aql objeto tá mesmo na sequencia já preescrita ali em cima, a maçã não existe ali, então vai dar verdadeiro dizendo que realmente a maçã não está contida lá
"Python" in curso 
# true

"maçã" not in frutas
# true

200 in saques 
# false

