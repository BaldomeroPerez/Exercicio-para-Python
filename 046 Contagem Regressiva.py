# Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for contar in range(10,-1, -1):
    print(contar)
    sleep(1)
print('Bum, Bum, Poow')

