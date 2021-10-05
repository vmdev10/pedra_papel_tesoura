import random

print('''
                        PEDRA, PAPEL E TESOURA....
Regras: Você e o computador escolhem entre pedra, papel ou tesoura. O vencedor é decidido por estas regras:

(I) A pedra quebra a tesoura;
(II) O papel embrulha a pedra e
(III) A tesoura corta o papel;

● Poder jogar mais de uma vez;
● Acumular pontos;
● Ter versões com outros elementos;
''')

objects_list = ['PEDRA',  'PAPEL', 'TESOURA']
player_one_score = 0
player_two_score = 0
try_again = 'SIM'

while (try_again == 'SIM'):
    player_one = input('Nome do jogador: ')
    player_two = 'Computador'
    computer_choice = random.choice(objects_list)
    player_choice = input(
        'Qual você escolhe? pedra, papel ou tesoura? ').upper()

    if (player_choice == 'PEDRA' and computer_choice == 'TESOURA'):
        player_one_score += 1
        print(f'{player_one}: ✊')
        print(f'{player_two}: ✌')
        print('Pedra quebra tesoura')
        print(f'{player_one} ganhou!!')

    elif (player_choice == 'PAPEL' and computer_choice == 'PEDRA'):
        player_one_score += 1
        print(f'{player_one}: ✋')
        print(f'{player_two}: ✊')
        print('O papel embrulha a pedra')
        print(f'{player_one} ganhou!!')

    elif (player_choice == 'TESOURA' and computer_choice == 'PAPEL'):
        player_one_score += 1
        print(f'{player_one}: ✌')
        print(f'{player_two}: ✋')
        print('A tesoura corta o papel')
        print(f'{player_one} ganhou!!')

    elif (player_choice == 'TESOURA' and computer_choice == 'PEDRA'):
        player_two_score += 1
        print(f'{player_one}: ✌')
        print(f'{player_two}: ✊')
        print('Pedra quebra tesoura')
        print(f'{player_two} ganhou!!')

    elif (player_choice == 'PEDRA' and computer_choice == 'PAPEL'):
        player_two_score += 1
        print(f'{player_one}: ✊')
        print(f'{player_two}: ✋')
        print('O papel embrulha a pedra')
        print(f'{player_two} ganhou!!')

    elif (player_choice == 'PAPEL' and computer_choice == 'TESOURA'):
        player_two_score += 1
        print(f'{player_one}: ✋')
        print(f'{player_two}: ✌')
        print('A tesoura corta o papel')
        print(f'{player_two} ganhou!!')
    else:
        print('Resultado indefinido!')

    try_again = input('Iniciar nova partida? Sim ou não? ').upper()

    if (try_again == 'NÃO' or try_again == 'NAO'):
        print(f'''
            JOGADOR:  PLACAR

            {player_one}: {player_one_score}
            ___________________________________

            {player_two}: {player_two_score}

      ''')
