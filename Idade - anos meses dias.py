# -*- coding: utf-8 -*-

idade = int(input("Digite sua idade em dias: "))

# Conversão
anos = idade // 365
meses = (idade % 365) // 30
dias = (idade % 365) % 30

# resultado
print("A idade é {} anos, {} meses e {} dias.".format(anos, meses, dias))