'''
Exercicio: Escreva uma função que recebe um objeto de coleção e retorna
o valor do maior numero digitado dessa coleção.Faça outra função que retorna
o menor numero dessa coleção.
'''


#Nome da função = maior
# Maior item começa com 0
#De item em coleção
#SE o item for maior do  o numero inicializado
#RETORNA o maior item da coleção


def maior(colecao):
    maior_i = colecao[0]
    for item in colecao:
        if item >  maior_i:
            maior_i = item
    return maior_i

def menor(colecao):
    menor_i = colecao[0]
    for item in colecao:
        if item < menor_i:
            menor_i = item
    return menor_i

print(maior([1,5,6,100,333]))
print(menor([4,3,7,0.1,0.60]))
