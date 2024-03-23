def forca():

    import random

    print('***********************************')
    print('    Bem vindo ao jogo da Forca!    ')
    print('Você perde o jogo se errar 5 vezes!')
    print('***********************************')

    arquivo = open('palavras_adivinhacao.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    letras_acertadas = ['_' for letra in palavra_secreta]
    erros = 0

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        print(f'\nVocê tem {erros} erro(s)!')

        print('\n', letras_acertadas)
        chute = input('Qual letra? ').strip().upper()

        if chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[posicao] = letra

                posicao += 1

        else:
            print('\nVocê errou!')
            erros += 1

            if erros == 5:
                print('\nVocê já tem 5 erros!')
                print('\nVocê perdeu!')
                enforcou = True

        print('\n', letras_acertadas)

        if '_' not in letras_acertadas:
            acertou = True

            print('\nVocê adivinhou a palavra!')


print('\nFim do Jogo!')

if __name__ == '__main__':
    forca()
