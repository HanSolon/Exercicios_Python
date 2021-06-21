""" 1 - Faça um programa que determine e mostre os cincos 
primeiros múltiplos de 3, considerando números maiores que 0."""
"""for n in range(1, 16):
    if n % 3 == 0:
        print(n)"""

"""2 - Escreva um programa que escreva na tela, de 1 até 100, de 1 
em 1, 3 vezes. A primira vez deve usar a estrutura de repetição
for, a segunda while, e a terceira do while.""" 
"""
for n in range(1, 101):
    print(n)
print("\nPROXIMA SEQUENCIA\n")
int: minimo = 1
while minimo < 101:
    print(minimo)
    minimo += 1
print("\nPROXIMA SEQUENCIA\n")
int: numero = 0
while True:
    if numero < 100:
        numero += 1
        print(numero)
    else:
        break
"""

""" 3 - Faça um algoritimo utilizando o comando while que mostra
uma constagem regressiva na tela, iniciando em 10 e terminando em 0.
Mostrar um mensagem 'FIM!', após a contagem"""
"""regressiva: int = 11
while regressiva > 0:
    regressiva -= 1
    print(regressiva)
print('FIM!')"""

""" 4 - Escreva um programa que declare um inteiro, inicialize-o
com 0, e incremente-o de 1000 em 1000, imprimindo seu valor na
tela, até que seu valor seja 100000(cem mil)."""
"""for n in range(0, 100001, 1000):
    print(n)
"""
""" 5 - Faça um programa que peça ao usuario para digitar
10 valores e some-os"""
"""soma: int = 0 
for valor in range(1, 11):
    valor: int = int(input("Digite um valor inteiro: "))
    soma += valor
print(soma)"""

""" 6 - Faça um programa que leia 10 inteiros e imprima sua média."""
"""soma: int = 0
for i in range(10):
    valor: int = int(input("Informe o valor: "))
    soma += valor
print("A média é", soma / 10)"""

""" 7 - Faça um programa que leia 10 inteiros positivos, ignorando 
não positivos, e imprima sua media.""" 
"""qtd: int = 0
soma: int = 0
while qtd != 10:  
  qtd += 1
  numero: int = int(input("Digite o seu número: "))
  while numero <= 0:
       numero: int = int(input("O número digitado deve ser positivo"))
  soma += numero
print(f"A média é {soma/10}")"""
    
"""for qtd in range(4):
    valor = int(input(" Informe o valor: "))
    if valor >= 0:
        soma += valor
    else:
        valor = None
print("A media é: ", soma / 4)"""

""" 8 - Escreva um programa que leia 10 numeros eescreva o menor
valor e o maior valor lido. """
"""num: int = int(input("Digite valor: ")) 
maior: int = num
menor: int = num
qtd: int = 1
while qtd != 10:
    qtd += 1
    num: int = int(input("Digite numero: "))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(maior, menor)

lista = []
for numeros in range(1, 11):
    valor = int(input("Informe um numero: "))
    lista.append(valor)
    
print("Maior valor: ", max(lista))
print("Menor valor: ", min(lista))"""

""" 9 - Faça um programa que leia um número inteiro N e depois imprima
os N primeiros numeros naturais ímpares"""
"""valor: int = int(input("Informe um numero N: "))
while valor > 0:
    valor -= 1
    if valor % 2 != 0:
        print(valor)      
"""
""" 10 - Faça um programa que calcule e mostre a soma dos 50 primeiros 
números pares""" 
"""soma: int = 0
for num in range(51):
    if num % 2 == 0:
        soma += num
print(soma)"""
"""11 - Faça um programa que leia um numero inteiro N e imprima todos os 
números naturais de 0 até N em ordem crescente.
"""
"""numero: int = int(input("Digite um número: "))
for num in range(0, numero+1, 1):
    print(num)"""

""" 12 - Faça um programa que leia um numero inteiro positivo N e im-
prima todos os numeros naturais de 0 até N em ordem decrescente."""
"""numero: int = int(input("Digite um número N: "))
for num in range(numero,-1, -1):
    print(num)
"""

""" 13 e 14 - Faça um programa que leia um número inteiro positivo par N
e imprima todos os números pares de 0 até N em ordem crescente e decrecente"""
"""numero: int = int(input("Digite um numero N PAR: "))
print("Ordem crescente")
for num in range(0, numero+1):
    if num % 2 == 0:
        print(num)
print("Ordem Decrecente")
for num in range(numero, -1, -1):
    if num % 2 == 0:
        print(num)
"""
""" 15 e 16 - Faça um programa que leia um numero inteiro positivo im-
par N e imprima todos os números impares de 1 até N em ordem crescente
e decrescente"""
"""numero: int = int(input("Digite um número N IMPAR: "))
for num in range(1, numero+1):
    if num % 2 != 0:
        print(num)
for num in range(numero, -1, -1):
    if num % 2 != 0:
        print(num)"""
"""17 -  Faça um programa que leia um número inteiro positivo N e calcule
a soma dos N primeiros números naturais."""
"""numero: int = int(input("Digite um número N: "))
soma = 0
for num in range(0, numero):
    soma += num
print(soma)"""
""" 18 - Escreva um algoritimo que leia certa quantidade de números e im-
prima o maior deles e quantas vezes o maior número foi lido. A quantidade
de números a serem lidos deve ser fornecida pelo usuário"""
"""qtd: int = int(input("Digite a quantidade de numeros que devem ser lidos: "))
num: int = int(input("Digite numero: ")) 
maior: int = num
contador_maior: int = 0
while qtd > 1:
    qtd -= 1
    num: int = int(input("Digite numero: "))
    if num > maior:
        maior = num
        if maior == num:
            contador_maior += 1
print(maior, contador_maior)"""
''' 19 - Escreva um algoritimo que leia um número inteiro entre 100 e 999 e
imprima na saída cada um dos algarismos que compôem o número'''
'''numero: int = int(input("Digite um numero entre 100 e 999: "))
while True:
    if numero >= 100 and numero <= 999:
        u: int = numero // 1 % 10
        d: int = numero // 10 % 10        
        c: int = numero // 100 % 10
        print(f"""Numero {numero}
        Unidade: {u}
        Dezena: {d}0
        Centena: {c}00""")
        break
    else: 
        print("Numero invalido! ")
        numero: int = int(input("Digite um numero entre 100 e 999: "))
'''
""" 20 - Ler uma sequêcia de números inteiros e determinar se eles são pares
ou não. Deverá ser informado o número de dados lidos e número de valores pares.
O processo termina quando for digitado o número 1000."""
"""contador = contador_pares = 0
num: int = int(input("Digite um numero [1000 para parar]: "))
while num != 1000:
    contador += 1
    if num % 2 == 0:
        contador_pares += 1
        print(f"Vc digitou {contador_pares} numeros pares, {num} é par")
    else:
        print(f"{num} é impar, vc digitou {contador} numeros")
    num: int = int(input("Digite um numero [1000 para parar]: "))"""
"""21 - Faça um programa que receba dois números. Calcule e mostre:
* a Soma dos números pares desse intervalo de números, incluindo os numeros
digitados; 
* a multiplicação dos números impares desse intervalo, incluindo os digitados;
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
soma = 0
multi = 1
if num1 < num2:
    for num in range(num1, num2+1):
        if num % 2 == 0:
            soma += num
        else:
            multi *= num 
else:
    for num in range(num2, num1+1):
        if num % 2 == 0:
            soma += num
        else:
            multi *= num 
print(f"Soma: {soma}")
print(f"Multiplicação: {multi}")"""
"""22 -  Escreva um programa completo que permita qualquer aluno introdudir,
pelo teclado uma seguencia arbritrária de notas (válidas no intervalo de 10 a 20) e
que mostre na tela, como resultado, correspondente média aritmética. o número de
notas com que o aluno pretenda efetuar o calculo não será fornecido ao programa, o 
qual terminara quando for introduzido um valor que não seja válido como nota de
aprovação.
# Entrada sequecia de notas (10 a 20)
nota = int(input("Digite uma nota: "))
count = 0
soma = 0
while nota >= 10 and nota <= 20:
    count += 1
    soma += nota
    nota = int(input("Digite outra nota: "))
print(f"Media: {soma / count}")
"""
"""23 - Faça um algoritmo que leia um número positivo e imprima seus divisores. 
numero = int(input("Digite um numero: "))
lista = []
if numero > 0:
    for num in range(1, numero, 1):
        if numero % num == 0: 
            lista.append(num)
else: 
    print("Numero < 0")
print(f"Divisores de {numero} == {lista}")
"""
"""24 - Escreva um programa que leia um número inteiro e calcule a soma de todos
de todos os divisoes desse numero, com execeção dele próprio Ex: a soma dos divisores
do número 66 é 1 + 2 + 3 + 6 + 22 + 33 = 78
numero = int(input("Digite um numero: "))
lista = []
if numero > 0:
    for num in range(1, numero-1, 1):
        if numero % num == 0: 
            lista.append(num)
else: 
    print("Numero < 0")
print(f"A soma dos divisores de {numero} == {lista, numero} == {sum(lista)}")"""

"""25 - Faça um programa que some todos os números abaixo de 1000 que são multiplos de 3 ou 5
lista = []
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        lista.append(i)
print(sum(lista))
print(lista)"""
"""26 - Faça um algoritimo que encontre o primeiro multiplo
11, 13 ou 17 após um numero de dados""" 
"""numero: int = int(input("Digite um numero: "))
lista = []
for num in range(numero, numero + 12):
    if num % 11 == 0 or num % 13 == 0 or num % 17 == 0:
        lista.append(num)
print(lista)
"""
"""27 - Em Matemática, o numero harmonico designado por H(n) 
define-se como sendo a soma da série harmónica: 
H(n) = 1 + 1/2 + 1/3 + 1/4 +...+ 1/n
Faça um programa que leia um valor n inteiro e positivo e apre-
sente o valor de H(n).
"""
