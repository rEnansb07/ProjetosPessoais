from ex111.utilidadesCeV import dados
multiplicadores = 10
multiplicadores2 = 11
soma = igualdade = repeticao = 0
cpf = str(dados.leiaint('Insira seu CPF: ')) #Tratamento de exceções caso o CPF não seja um número
lista = cpf.split() #Separação do CPF em algarismos
print(lista)
if len(cpf) != 11:
    while len(cpf) != 11:
        print('Insira corretamente o seu CPF: ')
        cpf = str(dados.leiaint('Insira seu CPF: '))
        lista = cpf.split()
igualdade = int(lista[0][0]) #Selecionando o primeiro digíto como base
for numero in range(0,11): #Verificando se todos os dígitos são iguais
    if igualdade == int(lista[0][numero]):
        repeticao += 1
if repeticao != 11:
    for item in lista: #Multiplicando cada número
        for numero in item:
            if multiplicadores == 1:
                break
            numero = int(numero)
            soma = soma + (numero * multiplicadores)
            multiplicadores = multiplicadores-1

    validacao = (soma * 10) % 11 #Realização da verificação do primeiro dígito através da soma
    if validacao == 10:
        validacao = 0
    print(lista[0][9])
    print(validacao)
    print(repeticao)
    if int(lista[0][9]) != validacao:
        print('CPF inválido')
else:
    print('CPF inválido!')
soma = 0 # Redefinição da variável pra segunda validação
for item in lista:
    for numero in item:
        if multiplicadores == 1:
            break
        numero = int(numero)
        soma = soma + (numero * multiplicadores2)
        multiplicadores = multiplicadores - 1
validacao2 = ((soma * 10) % 11)
if validacao2 == 10:
    validacao2 = 0
print(lista[0][10])
print(validacao2)
if int(lista[0][10]) != validacao2:
    print('CPF inválido')
print('CPF totalmente validado com sucesso!')


