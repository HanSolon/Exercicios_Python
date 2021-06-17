"""
1 - Crie uma função que recebe como parâmetro um numero inteiro e devolva o seu dobro
"""
"""
def dobro(numero: int) -> None:
    return numero * 2
print(dobro(3))"""
""" 
2 - Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a na tela 
no formato textual por extenso. Exemplo: Data 01/01/2000, imprimir: 1 de  janeiro de 2000
"""
"""
from datetime import date
data_atual = date.today()
def formato_textual_date(data_atual: date) -> str:
    if data_atual.strftime('%m') == "01":    
        return data_atual.strftime('%d de janeiro de %Y')
    elif data_atual.strftime("%m") == "02":
        return data_atual.strftime('%d de fevereiro de %Y')
    elif data_atual.strftime("%m") == "03":
        return data_atual.strftime('%d de março de %Y')
    elif data_atual.strftime("%m") == "04":
        return data_atual.strftime('%d de Abril de %Y')
    elif data_atual.strftime("%m") == "05":
        return data_atual.strftime('%d de Maio de %Y')
    elif data_atual.strftime("%m") == "06":
        return data_atual.strftime('%d de Junho de %Y')
    elif data_atual.strftime("%m") == "07":
        return data_atual.strftime('%d de Julho de %Y')
    elif data_atual.strftime("%m") == "08":
        return data_atual.strftime('%d de Agosto de %Y')
    elif data_atual.strftime("%m") == "09":
        return data_atual.strftime('%d de Setembro de %Y')
    elif data_atual.strftime("%m") == "10":
        return data_atual.strftime('%d de Outubro de %Y')
    elif data_atual.strftime("%m") == "11":
        return data_atual.strftime('%d de Novembro de %Y')
    elif data_atual.strftime("%m") == "12":
        return data_atual.strftime('%d de dezembro de %Y')
print(formato_textual_date(data_atual))"""
"""
3 - Faça uma função para verificar se um número é positivo ou negativo. Sendo que o valor
de retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0. 
"""
"""
numero = int(input())
def verificar_positivo_negativo(num: int) -> int:
    if num > 0:
        print(1)
    elif num < 0:
        print(-1)
    elif num == 0:
        print(0)
verificar_positivo_negativo(numero)
"""
"""
4 - Faça um função para verificar se um numero é um quadrado perfeito. Um quadrado perfeito
é um numero inteiro não negativo que pode ser expresso como o quadrado de outro número inteiro
Ex: 1, 4, 9...
"""
"""
from math import sqrt
numero: int = int(input())
def quadrado_perfeito(num: int) -> int:
    if (sqrt(num) * sqrt(num)) == num:
        return True
    return False 
print(f"({numero}):É quadrado perfeito? {quadrado_perfeito(numero)}")"""
"""
5 - Faça um função e um programa de teste para calculo do volume de uma esfera.
Sendo que o raio é passado por parametro.
V = 4/3 * PI * RAIO**3
"""
"""
from math import pow
raio: float = float(input("Digite raio: "))
def volume_esfera(raio: float) -> float:
     return (4 * 3.14 * pow(raio, 3) / 3)
print(f'O volume da esfera é {volume_esfera(raio)} cm(cubicos)')"""
"""
6 - Faça uma função que receba 3 numeros inteiros como parâmetro, representando horas,
minutos e segundo, e os converta em segundos.
"""
"""hora: int = int(input("Digite Hora: "))
minuto: int = int(input("Digite Minutos: "))
segundos: int = int(input("Digite Segundos: "))
uma_hora = 3600
um_minuto = 60
def converte_hora_minuto_para_segundo(hora: int, minuto: int, segundos: int):
    return (hora * uma_hora) + (minuto * um_minuto) + segundos
print(converte_hora_minuto_para_segundo(2, 30, 60))"""    
"""
7 - Faça uma função que receba uma temperatura em graus Celsis e retorne-a convertida
em graus Fahrenheit. A fórmula de conversão é: F = C * (9.0/5.0) + 32.0, sendo F a
temperatura em Fahrenheit e C a temperatura em Celsius. 
"""
"""
celsis: float = float(input("Digite temperatura em Celsis: "))
def celsis_fahrenheit(celsis: float):
    return celsis * (9/5) + 32
print(f"Sua conversão para Fahrenheit: {celsis_fahrenheit(celsis)}°F")"""
"""
8 - Sejama a e b os catetos de um triangulo, onde a hipotenusa é obtida pela equação:
hipotenusa = raiz(a**2 + b**2). Faça uma função que receba os valores de a e b e calcule o
valor da hipotenusa através da equação.
"""
"""
from math import sqrt, pow
cateto_A: int = int(input("Digite valor do Cateto A: "))
cateto_B: int = int(input("Digite o valor do Cateto B: "))
def calcular_hipotenusa(a: int, b: int):
    return sqrt(pow(a, 2) + pow(b, 2))
print(f"Hipotenusa de {calcular_hipotenusa(cateto_A, cateto_B)}")"""
"""
9 - Faça uma função que receba a altura e o raio de um circulo circular e retorne o volume 
do cilindro. O volume de um cilindro é calculado por meio da seguinte formula:
V = PI * raio**2 * altura, onde pi = 3.141592. 
"""
"""
from math import pi, pow
altura: float = float(input("Digite altura: "))
raio: float = float(input("Digite o raio: "))
def volume_cilindro(h: float, r: float):
    return pi * pow(r, 2) * h
print(f"O volume do cilindro: {volume_cilindro(altura, raio):.2f}")"""
"""
10 - Faça uma função que receba dois números e retorne qual deles é o maior
"""
"""
def maior_numero(primeiro_numero: int, segundo_numero: int):
    if primeiro_numero > segundo_numero:
        return primeiro_numero
    
    return segundo_numero
print(f'O maior numero: {maior_numero(9, 2)}')"""
"""
11 - Elabore uma função que receba três notas de um aluno como parâmetros e uma letra.
Se a letra for A, a função deverá calcular a média aritmética das notas do aluno; se for P,
deverá calcular a média ponderada, com pesos 5, 3 e 2.
notas*peso1 + nota2*peso2/ peso1+peso2
"""
"""
def notas(nota1: float, nota2: float, nota3: float, tipo_media: str) -> float:
    if tipo_media == "A":
        return (nota1 + nota2 + nota3) / 3
    elif tipo_media == "P":
        return (nota1 * 5 + nota2 * 3 + nota3 * 2) / 10
    return 0
print(notas(8, 9, 6, "A"))
print(notas(8, 9, 6, "P"))"""
"""
12 - Escreva uma função que receba um número inteiro maior do que zero e retorne a soma
de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1).
Se o numero lido não for maior do que zero, o programa termirá com a mensagem "Numero inválido" 
"""
"""
numero: int = int(input("Informe numero: "))
def soma_algarismos(num: int) -> int:
    if num > 0:
        global u, d, c, m
        u = num // 1 % 10
        d = num // 10 % 10
        c = num // 100 % 10
        m = num // 1000 % 10
        return u + d + c + m
    else:
        print("Numero invalido")
print(f"A Soma dos Algarismos de {numero} é {soma_algarismos(numero)}")"""
"""
13 - Faça uma função que receba dois valores numéricos e um símbolo. Este simbolo repre-
sentará a operação que se deseja efetuar com os números. Se o síbolo for + deverá 
ser realizada uma adição, se for - uma subtração, se for / uma divisão e se for * será
efetuada uma multiplicação 
"""
"""
def operacao(num1: float, num2: float, op: str) -> float:
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        return num1 / num2
    elif op == "*":
        return num1 * num2
print(operacao(8, 6, '+'))
print(operacao(8, 6, '-'))
print(operacao(8, 2, '/'))
print(operacao(8, 6, '*'))"""

"""
    CONSUMO   | (Km/l) |     MENSAGEM     |
    menor que |   8    | Venda o carro!   |
    entre     | 8 e 14 |     Economico!   |
    maior que |   12   | Super econômico! |
14 - Faça uma função que receba a distancia em Km e a quantidade de litros de gasolina
consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma 
mensagem de acordo com a tabela abaixo:
"""
"""
def consumo_gasolina(km: float, l: float) -> float:
    if km / l < 8:
        print(f"Venda o carro!(Consumo de {km / l} Km/l")
    elif km / l >= 8 and km / l <= 12:
        print(f"Economico!(Consumo de {km / l} Km/l)")
    elif km / l > 14:
        print(f"Super econômico!(Consumo de {km / l} Km/l")
    return km/l
print(consumo_gasolina(5, 2)) 
print(consumo_gasolina(20, 2)) 
print(consumo_gasolina(30, 2)) """
"""
15 - Crie um programa que receba três valores (Obrigatoriamente maiores que zero), repre-
sentando as medidas dos três lados de um triangulo. Elabore funções para:
a) Determinar se esse lados formam um triangulo, sabendo que:
    * O comprimento de cada lado de um triangulo é menor do que a soma dos outros
    dois lados
b) Determinar e mostrar o tipo de triangulo, caso as medidas formem um triangulo,
Sendo que: 
    * Chama-se equilatero o triangulo que tem três lados iguais.
    * Denominam-se isoceles o triangulo que tem o comprimento de dois lados iguais.
    * Recebe o nome de escaleno o triangulo que tem os três lados diferentes.
    | b - c | < a < b + c
    | a - c | < b < a + c
    | a - b | < c < a + b
"""
"""
def qual_triangulo(a: int, b: int, c: int) -> str: 
    if a < b + c or b < a + c or c < a + b:
        if a == b == c:
            return "Equilatero"
        elif a != b == c or b != a == c or c != a == b:
            return "Isoceles"
        elif a != b != c:
            return "Escaleno"
print(qual_triangulo(10, 10, 12))
print(qual_triangulo(5, 10, 9))
print(qual_triangulo(6, 6, 6))"""
"""
16 - Faça uma função chamada DesenhaLinha. Ele deve desenhar uma linha na tela usando
varios simbolos de igual (Ex: ==========). A função recebe por parâmetro quantos sinais
de igual serão mostrados.  
"""
"""
qtd_sinais: int = int(input("Digite quantidade de sinais que devem ser mostrados: "))
def desenhalinha(qtd: int) -> str:
    return "=" * qtd
print(desenhalinha(qtd_sinais))"""
"""
17 - Faça uma função que receba dois números inteiros positivos por parametro e retorne a
soma dos N números inteiros existentes entre eles.
"""





"""
18 - Faça uma questão que receba por parâmetro dois valores x e z. Calcule e retorne o 
resultado de x**z para o programa principal. Atenção não utilize nenhuma função pronta
de exponenciação
"""
"""def exponencial(x: int, z: int) -> int:
    return x**z
print(exponencial(2, 3))"""
"""
19 - Faça uma função que retorne o maior fator primo de um numero.
"""
#alteração
a = 1
b = 2
