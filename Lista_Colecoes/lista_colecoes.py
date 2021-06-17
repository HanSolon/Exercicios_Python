"""1 - Faça um programa que possua um vetor denominado A que armazene 6 números
inteiros. O programa deve executar os seguintes passos:
a) Atribua os seguintes valores a esse vetor 1, 0, 5, -2, -5, 7.
b) Armazene em uma variavel inteira (simples) a soma entre os valores das posições 
A[0], A[1], e A[5] do vetor e mostre na tela esta soma
c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
d) Mostre na tela cada valor do vetor A , um em cada linha."""
"""a = [1, 0, 5, -2, -5, 7]
soma = (a[0] + a[1] + a[5])
print(soma) 
a[4] = 100
print(a)"""
"""2 - Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos."""
"""numeros = []
for num in range(6):
    num = int(input())
    numeros.append(num)
print(numeros)"""
"""3 - Ler um conjunto de números reais, aramzenando-o em um vetor e calcular o quadrado dos componentes
desse vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os 
conjuntos. """ 
"""from math import pow
vetor = []
quadrado = []
def receber_float():
    num = float(input())
    return num
for num in range(10):
    num = receber_float()
    vetor.append(num)
for num in vetor:
    quadrado.append(pow(num, 2))
print(vetor)
print(quadrado)"""

""" 4 - Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y quaisquer
correspondentes a duas posições no vetor. Ao final seu programa devera escrever a soma dos valores nas respectivas
posições X e Y."""
"""vetor = []
def receber_valor():
    num = int(input())
    return num
print("Valores do Vetor: ")
for num in range(8):
    num = receber_valor()
    vetor.append(num)
print("Posição do Vetor: ")
x = receber_valor()
y = receber_valor()
print(vetor[x])
print(vetor[y])
print(vetor[x] + vetor[y])"""
""" 5 - Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui. """
"""vetor = []
qtd = 0
def receber_valor():
    num = int(input())
    return num
for num in range(10):
    num = receber_valor()
    vetor.append(num)
    if num % 2 == 0:
        qtd += 1
print(qtd)
print(vetor)"""
""" 6 - Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá
ser impresso o maior e o menor elemento do vetor."""
"""vetor = []
def receber_valor():
    num = int(input())
    return num
for num in range(10):
    num = receber_valor()
    vetor.append(num)
print(f"maior: {max(vetor)}")
print(f"menor: {min(vetor)}")"""
""" 7 - Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima 
o vetor, o maior elemento e a posição que ele se encontra"""
"""vetor = []
def receber_valor():
    num = int(input())
    return num
for num in range(10):
    num = receber_valor()
    vetor.append(num)
print(f"N[{max(vetor)}] = P[{vetor.index(max(vetor))}]")"""
"""8 - Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores 
lidos na ordem inversa. """
"""vetor = []
def receber_valor():
    num = int(input())
    return num
for num in range(6):
    num = receber_valor()
    vetor.append(num)
vetor.reverse()
print(vetor)"""
"""9 - Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os
valores na ordem inversa """
"""vetor = []
def receber_valor():
    num = int(input())
    return num
def verificar_par():
    if num % 2 == 0:
        return num
for num in range(6):
    num = receber_valor()
    num = verificar_par()
    if num == None:
        num = receber_valor()
        num = verificar_par()
    vetor.append(num)
vetor.reverse()
print(vetor)"""
""" 10 -  Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule
e imprima a média geral."""
"""vetor = []
def receber_valor_float():
    num = float(input())
    return num
for num in range(15):
    print("Digite nota do Aluno: ")
    num = receber_valor_float()
    vetor.append(num)
print(vetor)
print(f"{sum(vetor) / 15:,.2f}")"""
"""11 - Faça um programa que preencha um vetor com 10 numeros reais , calcule e mostre a 
quantidade de números negativos e a soma dos números positivos desse vetor. """ 
"""vetor = []
qtd = 0
soma = 0
for num in range(5):
    num = float(input())
    vetor.append(num)
for num in vetor:
    if num < 0:
        qtd += 1
    else: 
        soma += num
print(f'Qtd de negativos: {qtd}')
print(f"Soma dos positivos: {soma}")"""
"""12 - Fazer um programa para ler  5 valores e, em seguida, mostrar todos os 
valores lidos juntamente com o maior, menor e a média dos valores."""
"""vetor = []
def receber_int():
    num = int(input())
    return num
for num in range(5):
    num = receber_int()
    vetor.append(num)
print(f"Maior: {max(vetor)}")
print(f"Menor: {min(vetor)}")
print(f"Média: {sum(vetor) / 5}")"""
"""13 - Fazer um programa que ler 5 valores e, em seguida, mostrar a posição onde
se encontram o maior e o menor valor. """
"""vetor = []
def receber_valor():
    num = int(input())
    return num
for num in range(5):
    num = receber_valor()
    vetor.append(num)
print(f"Maior[{vetor.index(max(vetor))}] == {max(vetor)}")
print(f"Menor[{vetor.index(min(vetor))}] == {min(vetor)}")"""
"""14 - Faça um programa que leia um vetor de 10 posições e verifique se existem 
valores iguais e os escreva na tela. """
"""from collections import defaultdict
# Define a lista de volares:
vetor = []
for num in range(10):
    num = int(input())
    vetor.append(num)
# Define o objeto que armazenará os índices de cada elemento:
indices = defaultdict(list)

# Percorre todos os elementos da vetor:
for i, num in enumerate(vetor):
    # Adiciona o índice do valor no vetor de índices:
    indices[num].append(i)
# Exibe o resultado:
for num in indices:
    if len(indices[num]) > 1:
        print(num, indices[num])"""
"""15 - Leia um vetor com 20 números interios. Escreva os elementos do vetor 
eliminando elementos repetidos """
#from collections import defaultdict
"""vetor = []
def remove_repetidos(lista):
    nova_lista = []
    for i in lista:
        if i not in nova_lista: # se i não estiver em nova lista, adicione i.
            nova_lista.append(i)
    nova_lista.sort()
    return nova_lista
for num in range(7):
    num = int(input())
    vetor.append(num)
vetor = remove_repetidos(vetor)
print(vetor)"""
"""indices = defaultdict(list)
for i, num in enumerate(vetor):
    indices[num].append(i)
for num in indices:
    if len(indices[num]) > 1:
        print(num, indices[num])
print(set(vetor)) # elimianar elementos repetidos 
print(len(set(vetor)))
print(len(vetor))"""
"""16 - Faça um programa que leia um vetor de 5 posições para números reais e, depois,
um código inteiro. Se o código for zero, finalize o programa; se for 1, mostre o vetor 
na ordem direta; se for 2, mostre o vetor na ordem inversa. Caso, o código for diferente
de 1 e 2 escreva uma mensagem informando que o código é inválido. """
"""vetor = []
for num in range(5):
    num = float(input("Digite numero: "))
    vetor.append(num)
while True:
    op = int(input('''Digite OPÇÃO: 
    [1 - imprimir ordem direta] 
    [2 - Ordem inversa] 
    [0 - SAIR]: '''))
    if op == 1:
        for num in vetor:
            print(num)
    elif op == 2:
        vetor.reverse()
        for num in vetor:
            print(num)
    elif op == 0:
        break
    else:
        print("Opcão Invalida!")"""
"""17 - Leia um vetor de 10 posições e atribua valor 0 para todos os elementos
que possuirem valores negativos. """
"""vetor = []
nova_lista = []
for num in range(10):
    num = int(input())
    vetor.append(num)
print(vetor)
for num in vetor:
    if num > 0:
        nova_lista.append(num)
    else:
        nova_lista.append(0)
print(nova_lista)"""
"""18 - Faça um programa que leia um vetor de 10 números. Leia um número x.
Conte os múltiplos de um número inteiro x nem vetor e mostre-os na tela. """
"""vetor = []
def receber_valor(num):
    num = int(input())
    return num
for num in range(6):
    print("Digte valores")
    num = receber_valor(num)
    vetor.append(num)
print("Multi: ")
x = receber_valor(num)
qtd = 0
for num in vetor:
    if num % x == 0:
        qtd += 1
        print(f"Multiplos {x}: {num}")
print(f"Qtd: {qtd}")"""
"""19 - Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i + 5 * i) % (i + 1),
sendo i a posição do elemento no vetor. Em seguida imprima o vetor na tela. """
"""vetor = []
i = 0
while i < 50:
    vetor.append((i + 5 * i) % (i + 1))
    i += 1
print(vetor)"""
"""20 - Escreva um programa que leia números inteiros no intervalo [0, 50] e os 
armazene em um vetor de 10 posições. Preenha um segundo vetor apenas com os números
impares do primeiro vetor. Imprima os dois vetores, 2 elementos por linha. """
"""vetor = []
v_impares = []
for num in range(10):
    num = int(input())
    if num > 0 and num <= 50:
        vetor.append(num)
    else:
        num = int(input())
for num in vetor:
    if num % 2 != 0:
        v_impares.append(num)
    print(f'{vetor} # {v_impares}')
"""
"""21 - Faça um programa que receba do usuario dois valores, A e B, com 10 números
inteiros cada. Crie um novo valor denominado C calculando C = A - B. Mostre na tela 
os dados do vetor C."""
"""a = []
b = []
c = []
for num_a in range(10):
    num_a = int(input("Valor de A: "))
    a.append(num_a)
for num_b in range(10):
    num_b = int(input("Valor de B: "))
    b.append(num_b)
i = 0
while len(c) < 10:
    if a[i] > b[i]:
        c.append(a[i] - b[i])
    else:
        c.append(b[i] - a[i])
    i += 1
print(f"A == {a}")
print(f'B == {b}')
print(f'C == {c}')"""
"""22 - Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo,
nas posições pares os valores do primeiro e nas posições impares os valores do segundo."""

