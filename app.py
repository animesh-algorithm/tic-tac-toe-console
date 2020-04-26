from random import randint
from numpy import array

class TicTacToe:
    def __init__(self, XO_choice):
        self.hu_player = XO_choice.capitalize()
        self.comp_player = 'O' if self.hu_player == 'X' else 'X'
        self.board = [['-', '|', '-', '|', '-']] * 3
        self.board = array(self.board)
        self.win_combos = [
            [(0, 0), (0, 2), (0, 4)],
            [(1, 0), (1, 2), (1, 4)],
            [(2, 0), (2, 2), (2, 4)],
            [(0, 0), (1, 2), (2, 4)],
            [(2, 0), (1, 2), (0, 4)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 4), (1, 4), (2, 4)]
        ]
        self.curr_player = self.hu_player

    def display_board(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                print(self.board[row][col], end="")
            i = [0, 2, 4][row]
            print(f'  {row+i+1}|{row+i+2}|{row+i+3}')
        print('--------------')
    
    def update_board(self, inp):
        if inp in [1, 2, 3]:
            row = 0
        elif inp in [4, 5, 6]:
            row = 1
        elif inp in [7, 8, 9]:
            row = 2
        else:
            print('Chutiya hai kya?')
            raise InterruptedError

        if inp in [1, 4, 7]:
            col = 0
        elif inp in [2, 5, 8]:
            col = 2
        elif inp in [3, 6, 9]:
            col = 4
        else:
            print('Chutiya hai kya?')
            raise InterruptedError

        self.board[row][col] = self.curr_player
        self.display_board()
    
    def change_player(self):
        self.curr_player = self.comp_player if self.curr_player == self.hu_player else self.hu_player
    
    def check_win(self):
        for win_combo in self.win_combos:
            to_check = list()
            for combo in win_combo:
                row = combo[0]
                col = combo[1]
                to_check.append(self.board[row][col])
            if len(set(to_check)) == 1:
                if '-' not in set(to_check):
                    return (True, win_combo)
            else:
                continue
        return False

if __name__ == "__main__":
    game = TicTacToe(input('What do you prefer "X" or "O"\n'))
    game.display_board()
    hu_player_inputs = list()
    while True:
        if game.curr_player == game.hu_player:
            inp = int(input('Enter no. between 1 and 9\n'))
            hu_player_inputs.append(inp)
            game.update_board(inp)
        else:
            while True:
                inp = randint(1, 9)
                if inp not in hu_player_inputs:
                    game.update_board(inp)
                    break
        if game.check_win() == False:
            game.change_player()
        else:
            print(game.curr_player, ' Win')
            exit_inp = input('Do you wanna continue to play?\nPress "y" for yes and "n" for no\n')
            if exit_inp.capitalize() == 'Y':
                game = TicTacToe(input('What do you prefer "X" or "O"\n'))
                game.display_board()
                hu_player_inputs = list()
            else:
                break