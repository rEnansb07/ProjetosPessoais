from ex111.utilidadesCeV import dados
multiplicadores = 10
soma = 0
contador = 0
cpf = str(dados.leiaint('Insira seu CPF: ')) #Tratamento de exceções caso o CPF não seja um número
lista = cpf.split() #Separação do CPF em algarismos
if len(cpf) != 11:
    while len(cpf) != 11:
        print('Insira corretamente o seu CPF: ')
        cpf = str(dados.leiaint('Insira seu CPF: '))
        lista = cpf.split()
for item in lista: #Multiplicando cada número
    for numero in item:
        if multiplicadores == 1:
            break
        numero = int(numero)
        soma = soma + (numero * multiplicadores)
        multiplicadores = multiplicadores-1
validacao = (soma * 10) % 11
if validacao == 10:
    validacao = 0
print(lista[0][9])
print(validacao)
if int(lista[0][9]) != validacao:
    print('CPF inválido')



