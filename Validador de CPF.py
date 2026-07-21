def verificar_repeticao(digito1, cpf):
    repeticao = 0
    for numero in range(0,11):
        if digito1 == int(cpf[numero]):
            repeticao += 1
    if repeticao == 11:
        return True
    else:
        return False

def validar_verificadores(lista):
    multiplicadores = 10
    soma = 0
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
    if int(lista[0][9]) != validacao:
        return 'CPF inválido!'
    else:
        soma = 0 # Redefinição da variável pra segunda validação
        multiplicadores = 11
        for item in lista:
            for numero in item: # Realização da verificação do segundo dígito através da soma
                if multiplicadores == 1:
                    break
                numero = int(numero)
                soma = soma + (numero * multiplicadores)
                multiplicadores -= 1
        validacao2 = ((soma * 10) % 11)
        if validacao2 == 10:
            validacao2 = 0
        #print(lista[0][10])
        #print(validacao2)
        if int(lista[0][10]) != validacao2:
            return 'CPF inválido!'
        else:
            return 'CPF totalmente validado com sucesso!'

def leiaint(msg):
    while True:
        try:
            entrada = input(msg).strip()
            if '.' in entrada:
                entrada = entrada.replace('.','')
            if '-' in entrada:
                entrada = entrada.replace('-','')
            numero = int(entrada)
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número')
            numero = 0
            return numero
        except (TypeError, ValueError):
            print('\033[31m ERRO! O tipo de dado não é válido.\033[m')
        except Exception as erro:
            print(f'O programa encontrou um erro {erro.__class__}. Tente novamente.')
        else:
            return numero








#Programa Principal
primeiro_digito = 0
cpf = str(leiaint('Insira seu CPF: ')) # Tratamento de exceções caso o CPF não seja um número
lista = cpf.split() # Separação do CPF em algarismos
if len(cpf) == 10: # Tratando o bug quando o CPF começa com zero
    cpf = str('0') + lista[0]
    lista.append(cpf)
    lista.pop(0)
    primeiro_digito = 0
elif len(cpf) != 11 and not len(cpf) == 10: # Loop caso o cpf inserido anteriormente não esteja com 11 algarismos ou não tenha 10 algarismos
    while len(cpf) != 11:
        print('Insira corretamente o seu CPF: ')
        cpf = str(leiaint('Insira seu CPF: '))
        lista = cpf.split()
        if len(cpf) == 10: # Tratando o bug do 0 dentro do loop
            cpf = str('0') + lista[0]
            lista.append(cpf)
            lista.pop(0)
            primeiro_digito = 0
            break
if len(cpf) == 11:
    primeiro_digito = int(lista[0][0]) #Selecionando o primeiro digíto como base
if not verificar_repeticao(primeiro_digito, lista[0]):
    print(validar_verificadores(lista))
else:
    print('CPF inválido!')



