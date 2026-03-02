# Jogo de Adivinhação em Python

numero_secreto = 0 # aqui é definido o numero secreto que o jogador tem que adivinhar

print('Coloque um numero para ser o numero secreto:') #aqui ele vai coletar o numero para a variavel numero_secreto e vai transforma em int
numero_secreto = int(input()) #aqui ele vai coletar o numero para a variavel numero_secreto e vai transforma em int

print('Bem vindo ao jogo de adivinhação!\nVocê tem 5 tentativas para adivinhar o número secreto!') #imprimi a mensagem que esta dentro das ''

x = 0 # aqui é definido o número de tentativas
while x <= 5: # aqui ele verifica se a tentativa é menor que 1 ou maior que 100, se for ele vai executar o bloco de código abaixo
    
    print('Tente adivinhar o número secreto entre 1 e 100') #imprimi a mensagem que esta dentro das ''
    tentativa = int(input('Digite o seu palpite: ')) #aqui ele vai coletar o numero para a variavel tentativa e vai transforma em int

    if tentativa == numero_secreto:
        print('Parabéns! Você adivinhou o número secreto!') #imprimi a mensagem que esta dentro das ''
        break # aqui ele vai parar o loop
    
    elif tentativa < numero_secreto:
        print('O número secreto é maior do que o seu palpite!') #imprimi a mensagem que esta dentro das ''
    
    else:
        print('O número secreto é menor do que o seu palpite!') #imprimi a mensagem que esta dentro das '' 

    x += 1 # aqui ele vai adicionar 1 a variavel x para contar as tentativas
