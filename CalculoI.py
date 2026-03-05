# Aqui vai ser um projeto para eu colocar o conteudo que estou vendo em Calculo I

print('Boas Vindas aqui você vai aprender Calculo I\n')

print('Qual tema você quer ver agora?\n')
print('1. Numeros Reais\n')
escolha_do_tema = int(input('Escolha o tema: '))

if escolha_do_tema == 1:
    print(
        '\n1. Estrutura Algébrica: o Corpo dos Números Reais\n\n'
        'A estrutura de corpo garante que as operações de adição e mutiplicação se comportem de maneira familiar e consistente. Um corpo é um conjunto onde podemos somar, subtrair, mutiplicar e dividir(exceto por zero) sem sair do conjunto\n\n'
        'Operações e Propriedades\n\n'
        'Para quaisquer números reais a,b,c.\n\n'
        'Opereção     Propriedade     Descrição\n'
        'Adição  |   Associativa   |  (a + b) + c = a + (b + c)\n'
        'Adição  |   Comutativa   |  a + b = b + a\n'
        'Adição  |   Elemento Neutro   |  Existe o 0 tal que a + 0 = a\n'
        'Adição  |   Simetrico/Inverso aditivo   |  Para todo a, existe -a tal que a + (-a) = 0\n\n'
        'Mutiplicação  |   Associativa   |  (a * b) * c = a * (b * c)\n'
        'Mutiplicação  |   Comutativa   |  a * b = b * a\n'
        'Mutiplicação  |   Elemento Neutro   |  Existe o 1(com 1 != 0) tal que a * 1 = a\n'
        'Mutiplicação  |   Simetrico/Inverso mutiplicativo   |  Para todo a != 0, existe a -¹ tal que a * a-¹ = 1\n\n'
        'A Conexão entre as Operações\n\n'
        'Propriedade     Descrição\n'
        'Distributiva   |  a * (b + c) = (a * b) + (a * c)\n'
        'Esta propriedade é a base para a fatoração e a expansão de expressões algébricas'
          )
