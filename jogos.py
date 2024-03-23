import adivinhacao
import forca

print('*********************************')
print('Escolha qual jogo você quer jogar')
print('*********************************')

print('1 - Jogo da Adivinhação')
print('2 - Jogo da Forca')

jogo = int(input('Digite aqui: '))

if jogo == 1:
    adivinhacao.adivinhacao()

elif jogo == 2:
    forca.forca()
