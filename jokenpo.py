# Jokenpo
import random


def computer_option():
    return random.randint(0, 2)


def player_option():
    try:
        player = int(input('Enter your choice: '))
        # range(start,stop,step)
        if player in range(0, 3):
            return player
        else:
            raise ValueError()
    except ValueError:
        print("Error: The input was not a valid integer. Only integers between 0 and 2.")
        play()


def result_check(player, computer):
    """
    Function that checks who won.
    returns a string
    """
    if player == computer:
        return 'It\'s a Draw!!'
    elif (player == 0 and computer == 2) or (
            player > computer and not (player == 2 and computer == 0)):
        return 'You Win!!'
    return 'You Loose!!'


def play():
    """
    Function that prints the options selected by the player and computer
    and print the result
    """
    print('-----------------------------------------')
    print('Lets play Rock - Paper - Scissors')
    print('   Choose between the options:')
    print('   0 = Rock')
    print('   1 = Paper')
    print('   2 = Scissors')

    option_dict = {0: 'Rock', 1: 'Paper', 2: 'Scissors'}

    player = player_option()

    computer = computer_option()

    player_choice = option_dict[player]
    computer_choice = option_dict[computer]

    print(f'  Your choice: {player_choice}')
    print(f'  Computer\'s choice: {computer_choice}')

    result = result_check(player, computer)

    print(f'The result is: \n      {result}')
    print('-*-*-')


if __name__ == '__main__':
    play_again = ''
    # Do a loop until player decide not play again, pressing 'n' letter
    while play_again.lower() != 'n':
        play()

        play_again = input('Let\'s play Again? Press \'y\' to Yes or \'n\' to No: ')
