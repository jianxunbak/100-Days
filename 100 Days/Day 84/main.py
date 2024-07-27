import os
from player import Player
from board import Board


def clear_screen():
    os.system('clear')


game_board = Board()
game_board.welcome(clear=clear_screen)
clear_screen()
game = True
clear_screen()

player_1 = Player(player="Player 1", clear=clear_screen)
player_2 = Player(player="Player 2", clear=clear_screen)

current_player = player_1

while True:
    clear_screen()
    current_player.game(board=game_board.board,
                        print_board=game_board.print_board,
                        pattern='X' if current_player == player_1 else 'O',
                        clear=clear_screen)

    results = game_board.check_win()
    if results == 'X':
        game_board.print_board()
        print(f"{player_1.name} wins!")
        break
    if results == 'O':
        game_board.print_board()
        print(f"{player_2.name} wins!")
        break
    if results == 'draw':
        game_board.print_board()
        print('Draw')
        break

    current_player = player_2 if current_player == player_1 else player_1
