
# insert logo

import art
from game_data import data
from random import randrange
from os import system

round = {
    'a': 0,
    'b': 0,
}

score = 0


def main():
    # define de icons A and B from database and display them for the user
    setNextRound()

    game_on = True
    while game_on:
        # get users input
        guess_input = ''
        while guess_input not in ['a', 'b']:
            guess_input = input('\nWho have more followers? (A or B) ').lower()
        # check if user is right or wrong
        game_on = checkGuess(guess_input)
        setNextRound(round['b'])

    endGame()


def endGame():
    system('clear')
    print(art.logo)
    print(f"Sorry not right. Your final score: {score}\n")


def printRound():
    system('clear')
    print(art.logo)
    if score > 0:
        print(f"You got right! Your score: {score}")
    a = round['a']
    b = round['b']
    print(f"\nA: {data[a]['name']}, an {data[a]['description']} from {data[a]['country']}.\n")
    print(art.vs)
    print(f"\nB: {data[b]['name']}, an {data[b]['description']} from {data[b]['country']}.")


def getRandomIcon():
    return randrange(0, len(data))


def setNextRound(a=getRandomIcon()):
    a = a
    b = getRandomIcon()
    while a == b:
        b = getRandomIcon()
    round['a'] = a
    round['b'] = b
    printRound()


def add_score():
    global score
    score += 10


def checkGuess(guess):
    a_count = data[round['a']]['follower_count']
    b_count = data[round['b']]['follower_count']

    if a_count > b_count:
        most_follower = round['a']
    else:
        most_follower = round['b']

    if round[guess] == most_follower:
        add_score()
        return True
    else:
        return False


main()
