# -*- coding: utf-8 -*-
import math

# Lendo os valores
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

# Verificando se é possível formar um triângulo
if a < b + c and b < a + c and c < a + b:
    semi_perimetro = (a + b + c) / 2.0
    area = math.sqrt(semi_perimetro * (semi_perimetro - a) * (semi_perimetro - b) * (semi_perimetro - c))

    print("Os valores formam um triângulo.")
    print("A área do triângulo é: {:.2f}".format(area))
else:
    # Exibe os valores se não formarem um triângulo
    print("Os valores não formam um triângulo.")
    print("Valores lidos: a = {}, b = {}, c = {}".format(a, b, c))
    print("A soma dos dois valores menores não podem ser inferiores ou igual ao valor maior")
    print("Exemplo: ")

    # Ordenando os valores
    ordem = [a, b, c]
    ordem.sort()

    soma_menores = ordem[0] + ordem[1]
    print("A soma dos dois menores valores é: {} menor ou igual a: {}".format(soma_menores, ordem[2]))
    print("Então não formam um triângulo")