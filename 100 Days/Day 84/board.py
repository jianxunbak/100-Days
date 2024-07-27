class Board:

  def __init__(self):
    self.board = {
        7: ' ',
        8: ' ',
        9: ' ',
        4: ' ',
        5: ' ',
        6: ' ',
        1: ' ',
        2: ' ',
        3: ' '
    }

  def print_board_sample(self):
    print('7' + '|' + '8' + '|' + '9')
    print('-+-+-')
    print('4' + '|' + '5' + '|' + '6')
    print('-+-+-')
    print('1' + '|' + '2' + '|' + '3')

  def print_board(self):
    print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
    print('-+-+-')
    print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
    print('-+-+-')
    print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])

  def welcome(self, clear):
    print("Welcome to the Tic Taq Toe Game!")
    self.select_next = input('Press enter to continue')
    clear()
    print("INSTRUCTIONS:")
    print(
        'The arrangement of the board is as shown.\nSelect a number from 1 to 9 to place your "X" or "O"'
    )
    self.print_board_sample()
    self.play = input('Press enter to continue')

  def check_win(self):
    win_combinations = [
        (7, 8, 9),  # Top row
        (4, 5, 6),  # Middle row
        (1, 2, 3),  # Bottom row
        (7, 4, 1),  # Left column
        (8, 5, 2),  # Center column
        (9, 6, 3),  # Right column
        (7, 5, 3),  # Diagonal \
        (9, 5, 1)  # Diagonal /
    ]

    for items in win_combinations:
      if self.board[items[0]] == self.board[items[1]] == self.board[
          items[2]] and self.board[items[0]] != '':
        return self.board[items[0]]
    if '' not in self.board.values():
      return 'draw'
    else:
      return 'continue'
