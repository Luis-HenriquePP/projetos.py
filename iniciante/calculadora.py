# Calculadora simples em Python


def somar(a,b): # Função de somar
    return a + b

def subtrair (a,b): # Função de subtrair
    return a - b

def mutiplicar (a,b): # Função de mutiplicar
    return a*b

def dividir (a,b): #Função  de dividir
    if b == 0:
        return 'não é possivel fazer a divisão por zero'
    else:
        return a/b
    
print('Bem vindo a calculadora simples em Python') #imprimi a mensagem que esta dentro das ''

print('Escolha a operação que deseja realizar: ') #imprimi a mensagem que esta dentro das ''

print('1 - Somar \n2 - Subtrair \n3 - Mutiplicar \n4 - Dividir \n') #imprimi a mensagem que esta dentro das ''

operacao = input('Digite o número da operação: ') #aqui ele vai coletar o numero da operação para a variavel operação

a = float(input('Digite o primeiro número: ')) #aqui ele vai coletar o numero para a variavel a e vai transforma em float

b = float(input('Digite o segundo número: ')) #aqui ele vai coletar o numero para a variavel a e vai transforma em float

if operacao == '1': # aqui ele verifica se a operção ´[e igual a 1, se for ele vai executar o bloco de código abaixo]
    resultado = somar(a,b) # aqui e determino que a variavel é a função somar com isso ele vai realizar a função que foi determinada para a variavel resultado
    print( 'o resultado da soma é :',resultado) #aqui vai imprimir o resultado da soma

elif operacao == '2': # aqui ele verifica se a operção ´[e igual a 2, se for ele vai executar o bloco de código abaixo]
    resultado = subtrair(a,b) # aqui e determino que a variavel é a função subtrair com isso ele vai realizar a função que foi determinada para a variavel resultado
    print('o resultado da subtração é :',resultado) #aqui vai imprimir o resultado da subtração

elif operacao == '3': # aqui ele verifica se a operção ´[e igual a 3, se for ele vai executar o bloco de código abaixo]
    resultado = mutiplicar(a,b) # aqui e determino que a variavel é a função mutiplicar com isso ele vai realizar a função que foi determinada para a variavel resultado
    print('o resultado da mutiplicação é :',resultado) #aqui vai imprimir o resultado da mutiplicação

elif operacao == '4':   # aqui ele verifica se a operção ´[e igual a 4, se for ele vai executar o bloco de código abaixo]
    resultado = dividir(a,b) # aqui e determino que a variavel é a função dividir com isso ele vai realizar a função que foi determinada para a variavel resultado
    print('o resultado da divisão é :',resultado) #aqui vai imprimir o resultado da divisão