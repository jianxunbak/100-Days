class Player:

    def __init__(self, player, clear):
        self.name = input(f"{player}, please provide your name: ")
        clear()

    def game(self, board, print_board, pattern, clear):
        while True:
            print_board()
            print(board)
            try:
                print(f"{self.name}'s turn")
                player = int(input("Please choose a number from 1 to 9: "))
                if player in range(1, 10):
                    if board[player] != ' ':
                        clear()
                        print(
                            'please select another number as this is already taken'
                        )
                    else:
                        clear()
                        board[player] = pattern
                        break
                else:
                    print(
                        'Invalid input, please input a number between 1 to 9')
            except ValueError:
                print('Invalid input, please input a number between 1 to 9')
