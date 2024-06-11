# Aqui podemos ver um pouco sobre funções de entrada saída, e a seguir terão alguns exemplos

nome = "Arthur"
sobrenome = "Santos"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="#")

# imprime Arthur Santos
# Imprime Arthur Santos...
# Imprime Arthur#Santos

# Aqui é a função de entrada, onde colocamos uma função que nos permite fazer com que o usuário possa inserir algo dado que nós pedirmos

nome = input("Informe o seu nome: ")
idade = input("Informe sua idade:")

# Após termos criado aquela função, já criamos uma variavél para conter ela, e poder usar para mostrar uma imagem como no código de exemplo abaixo
print("Entendi! Seu nome então é", nome, "e você tem", idade, "anos!")






