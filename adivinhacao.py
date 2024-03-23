# Define a função para chamar o jogo de adivinhação
def adivinhacao():

    # Importa a biblioteca Random
    import random

    # Introdução bonitinha sobre o jogo
    print('*********************************')
    print('Bem vindo ao jogo de Adivinhação!')
    print('     Você tem 5 tentativas!      ')
    print('*********************************\n')

    # Explicando as dificuldades do jogo
    print('Escolha um nível de Dificuldade!')
    print('1 - Fácil    - 15 Tentativas')
    print('2 - Normal   - 10 Tentativas')
    print('3 - Difícil  -  5 Tentativas\n')

    # Definindo a dificuldade do jogo
    dificuldade = int(input('Digite aqui o número da dificuldade: '))

    # Inicio a variável 'rodada'
    rodada = 0

    # Defino o número de tentativas com base na escolha o usuário
    if dificuldade == 1:
        tentativas = 15

    elif dificuldade == 2:
        tentativas = 10

    else:
        tentativas = 5

    # Uso para indicar o usuário de quantas rodadas faltam
    rodada_total = tentativas

    # Escolhe um número inteiro aleatório entre 1 e 100
    numero_secreto = random.randrange(1, 101)

    # Mantem o laço até o usuário acertar ou usar todas as tentativas
    for tentativas in range(1, tentativas + 1):

        # Defino a rodada atual
        rodada = rodada + 1
        print(f'\nRodada {rodada} de {rodada_total}')

        # Pego a resposta do usuário e analiso
        chute = input('\nDigite o seu número entre 1 e 100: ')
        chute = int(chute)

        # Defino que caso o Usuário tenha escolhido um número maior que 100 ou menor que 1 ele não avance
        while chute < 1 or chute > 100:
            chute = input('\nO número precisa estar entre 1 e 100: ')
            chute = int(chute)

        # Define se o chute foi maior ou igual do que o número sorteado
        maior = chute > numero_secreto
        acertou = numero_secreto == chute

        # Sai do laço se o usuário acertar o número
        if acertou:
            print('\nVocê acertou!')
            break

        # Avisa o usuário se o número for maior ou menor do que o sorteado
        else:
            if maior:
                print('\nVocê errou! Você chutou muito alto!\n')

            else:
                print('\nVocê errou! Você chutou muito baixo!\n')

    # Anuncia o fim do jogo
    print('\nFim do Jogo!')


# Só executa o programa se ele for rodado como principal ('Sem o menu')
if __name__ == '__main__':
    adivinhacao()
