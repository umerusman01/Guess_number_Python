def winner(a_board):
    # check for diagonals
    if ((a_board[0][0] == 'X' and a_board[1][1] == 'X' and a_board[2][2] == 'X') or
       (a_board[0][0] == 'O' and a_board[1][1] == 'O' and a_board[2][2] == 'O')):
        return True
    # check for right diagonal
    if ((a_board[0][2] == 'X' and a_board[1][1] == 'X' and a_board[2][0] == 'X') or
            (a_board[0][2] == 'O' and a_board[1][1] == 'O' and a_board[2][0] == 'O')):
        return True
    # check for first row
    if ((a_board[0][0] == 'O' and a_board[0][1] == 'O' and a_board[0][2] == 'O') or
            (a_board[0][0] == 'X' and a_board[0][1] == 'X' and a_board[0][2] == 'X')):
        return True
    # check for 2nd row
    if ((a_board[1][0] == 'O' and a_board[1][1] == 'O' and a_board[1][2] == 'O') or
            (a_board[1][0] == 'X' and a_board[1][1] == 'X' and a_board[1][2] == 'X')):
        return True
    # check for 3rd row
    if ((a_board[2][0] == 'O' and a_board[2][1] == 'O' and a_board[2][2] == 'O') or
            (a_board[2][0] == 'X' and a_board[2][1] == 'X' and a_board[2][2] == 'X')):
        return True
    # check for 1st coloumn
    if ((a_board[0][0] == 'O' and a_board[1][0] == 'O' and a_board[2][0] == 'O') or
            (a_board[0][0] == 'X' and a_board[1][0] == 'X' and a_board[2][0] == 'X')):
        return True
    # check for 2nd coloumn
    if ((a_board[0][1] == 'O' and a_board[1][1] == 'O' and a_board[2][1] == 'O') or
            (a_board[0][1] == 'X' and a_board[1][1] == 'X' and a_board[2][1] == 'X')):
        return True
    # check for 3rd coloumn
    if ((a_board[0][2] == 'O' and a_board[1][2] == 'O' and a_board[2][2] == 'O') or
            (a_board[0][2] == 'X' and a_board[1][2] == 'X' and a_board[2][2] == 'X')):
        return True
    return False  # otherwise return False


# function for printing board of game
def print_board(a_board):
    for val in a_board:
        for value in val:
            print(value, end="\t")
        print("\n")


def tictactoe(f_name, s_name):
    i = 0
    # fisrt assign default values to '*'
    board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
    while i < 5:
        print_board(board)  # print board before every input
        print(f"{f_name}'s turn: ")
        r = input("Row number: ")
        r = int(r)
        while r < 1 or r > 3:  # input validation
            r = input("Invalid! \nRow number: ")
        c = input("Coloumn number: ")
        c = int(c)
        while c < 1 or c > 3:  # input validation
            c = input("Invalid! \ncoloumn number: ")
        while (board[r-1][c-1] == 'O' or board[r-1][c-1] == 'X'):  # input validation
            print("Invalid input! ")
            r = input("Row number: ")
            r = int(r)
            while r < 1 or r > 3:  # input validation
                r = input("Invalid! \nRow number: ")
            c = input("Coloumn number: ")
            c = int(c)
            while c < 1 or c > 3:  # input validation
                c = input("Invalid! \ncoloumn number: ")
        board[r-1][c-1] = 'O'  # assigning 'O' to first palyer
        if (winner(board)):  # if found winner then return the function with winner name
            print("\nWe have found the winner!")
            print_board(board)
            return (f_name)
        print_board(board)
        if (i == 4):  # Afetr 9th input if winner is not decided then game is tied
            print("Game is tied!")
            return(None)
        print(f"{f_name}'s turn: ")
        r = input("Row number: ")
        r = int(r)
        while r < 1 or r > 3:  # input validation
            r = input("Invalid! \nRow number: ")
        c = input("Coloumn number: ")
        c = int(c)
        while c < 1 or c > 3:  # input validation
            c = input("Invalid! \ncoloumn number: ")
        while (board[r-1][c-1] == 'O' or board[r-1][c-1] == 'X'):  # input validation
            print("Invalid input! ")
            r = input("Row number: ")
            r = int(r)
            while r < 1 or r > 3:  # input validation
                r = input("Invalid! \nRow number: ")
            c = input("Coloumn number: ")
            c = int(c)
            while c < 1 or c > 3:  # input validation
                c = input("Invalid! \ncoloumn number: ")
        board[r-1][c-1] = 'X'  # assigning 'O' to first palyer
        if (winner(board)):  # if found winner then return the function with winner name
            print("\nWe have found the winner!")
            print_board(board)
            return (s_name)
        i = i + 1


first_name = input("Enter first player name: ")
second_name = input("Enter second player name: ")

print(f"{tictactoe(first_name, second_name)} WINS ")
