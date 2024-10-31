# -*- coding: utf-8 -*-

def inverter_frase(frase):
    frase_invertida = frase[::-1]
    return frase_invertida

frase = raw_input(u"Digite uma frase: ")
print(inverter_frase(frase))


"""não consegui ajustar para resolver o problema de caracteres"""