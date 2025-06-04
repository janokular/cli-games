#!/usr/bin/env python3

import sys

P1_NAME = 'P1'
P1_SYMBOL = 'x'
P2_NAME = 'P2'
P2_SYMBOL = 'o'
BOARD = [[' ', ' ', ' ',], [' ', ' ', ' ',], [' ', ' ', ' ',]]
AVAILABLE_MOVES = ['11', '12', '13', '21', '22', '23', '31', '32', '33']

def welcome():
    """Prints welcome message and player symbols."""
    print('Welcome to Tic Tac Toe!')
    print(f'{P1_NAME} symbol: {P1_SYMBOL}')
    print(f'{P2_NAME} symbol: {P2_SYMBOL}')


def print_row(row):
    """Prints a single row of the board."""
    print(f'| {row[0]} | {row[1]} | {row[2]} |')


def print_border():
    """Prints a border line for the board."""
    print('·---·---·---·')


def print_board():
    """Prints the current state of the board."""
    print_border()
    for row in BOARD:
        print_row(row)
        print_border()


def check_winner(player_name, player_symbol):
    """Checks if the current player has won."""
    for row in BOARD:
        if row.count(player_symbol) == 3:
            print(f'\n{player_name} wins!')
            sys.exit()
    # TODO Add checks for columns and diagonals for completeness


def make_move(player_name, player_symbol):
    """Prompts the player for a move and updates the board."""
    while True:
        move = input(f'\n{player_name}: ')
        if move not in AVAILABLE_MOVES:
            print('Incorrect move!')
            print(f'Available moves: {AVAILABLE_MOVES}')
        else:
            AVAILABLE_MOVES.remove(move)
            BOARD[int(move[0]) - 1][int(move[1]) - 1] = player_symbol
            print_board()
            check_winner(player_name, player_symbol)
            if not AVAILABLE_MOVES:
                print('\nDraw!')
                sys.exit()
            break

# Main game loop
welcome()
while True:
    make_move(P1_NAME, P1_SYMBOL)
    make_move(P2_NAME, P2_SYMBOL)
