import art
from time import sleep
from random import choice

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_info = {
    'player': {
        'hand': [],
        'isplaying': True,
    },
    'dealer': {
        'hand': [],
        'isplaying': True,
    },
    'game_on': False
}

turn = 'player'


def dealCards():
    # deal Player and dealer two cards
    player_hand = game_info['player']['hand']
    dealer_hand = game_info['dealer']['hand']

    for deal in range(1, 3):
        player_hand.append(choice(cards))
        dealer_hand.append(choice(cards))

    printInfo('dealer')
    printInfo('player')


def extraCard(user):
    # Give player or dealer extra card
    random_card = choice(cards)
    game_info[user]['hand'].append(random_card)


def playerPlay():
    print('\n....Player Turn....\n')

    extra = ''
    while extra not in ['e', 's']:
        printInfo('player')
        extra = input('Extra card(e) or Stop(s)? ').lower()
        if extra == 'e':
            extraCard('player')
            extra = ''
        elif extra == 's':
            game_info['player']['isplaying'] = False
        else:
            print('invalid input')

    checkMore21('player')


def dealerPlay():
    print('\n....Dealer Turn....\n')

    # check if hands sum is <17 else stop play
    hand_sum = sumHand('dealer')
    while hand_sum < 17:
        sleep(2)
        extraCard('dealer')
        hand_sum = sumHand('dealer')
        printInfo('dealer')

    game_info['dealer']['isplaying'] = False
    checkMore21('dealer')


def lost(user):
    if user == 'player':
        printInfo(user)
    else:
        print(game_info['dealer']['hand'])
    print(f'{user} got more than 21, {user} Lost.\n')
    game_info[user]['isplaying'] = False
    game_info['game_on'] = False


def compareWinner():
    print('\n....Checking the winner...\n')
    player_cards_sum = sumHand('player')
    dealer_cards_sum = sumHand('dealer')

    print('\nPlayer:')
    print(game_info['player']['hand'])
    print('Sum:', player_cards_sum)
    print('\nDealer:')
    print(game_info['dealer']['hand'])
    print('Sum:', dealer_cards_sum)

    if player_cards_sum > dealer_cards_sum:
        print('\nYou won.\n')
    elif player_cards_sum == dealer_cards_sum:
        print('\nDraw.\n')
    else:
        print('\nDealer won.\n')


def printInfo(user):
    user_cards = game_info[user]['hand']
    print(f'{user} hand: [{user_cards[0]}', end='')
    for card in range(len(user_cards) - 1):
        if user == 'player':
            print(f', {user_cards[card + 1]}', end='')
        else:
            print(', X', end='')

    print(']\n')


def checkFor21():
    player_hand = game_info['player']['hand']
    dealer_hand = game_info['dealer']['hand']

    if sum(player_hand) == 21:
        game_info['game_on'] = False
        print(player_hand, ' You won.\n')
    elif sum(dealer_hand) == 21:
        game_info['game_on'] = False
        print(dealer_hand, ' Dealer won.\n')
    elif sum(player_hand) == 21 and sum(dealer_hand) == 21:
        print('Draw.\n')


def sumHand(user):
    hand = game_info[user]['hand']
    sum = 0
    for card in hand:
        if card == 11:
            sum += 1
        else:
            sum += card
    return sum


def checkMore21(user):
    hand_sum = sumHand(user)
    if hand_sum > 21:
        lost(user)


start = ''
while start != 'y':
    start = input('Start game? (y) or (q/n) to close: ').lower()
    if start == 'y':
        print('\n')
        dealCards()
        game_info['game_on'] = True
        checkFor21()
    elif start in ['q', 'n']:
        exit()
    else:
        print('Not valid input')

while game_info['game_on']:
    if turn == 'player' and game_info['player']['isplaying']:
        playerPlay()
        if game_info['dealer']['isplaying']:
            turn = 'dealer'
    elif turn == 'dealer' and game_info['dealer']['isplaying']:
        dealerPlay()
        if game_info['player']['isplaying']:
            turn = 'player'
    else:
        compareWinner()
        game_info['game_on'] = False
