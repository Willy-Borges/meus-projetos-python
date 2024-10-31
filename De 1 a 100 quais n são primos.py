# -*- coding: utf-8 -*-

def primo(n):
    """Retorna True se n for um número primo, caso contrário False."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Testando de 1 a 100
for numero in range(1, 101):
    if primo(numero):
        print("{} VERDADEIRO - é primo.".format(numero))
    else:
        print("{} FALSO - não é primo.".format(numero))