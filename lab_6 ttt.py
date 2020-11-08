# import random
#
# def print_board_and_legend(board):
#     for i in range(3):
#         line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2] # This is the empty board
#         line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) # This is the board with the legend
#         print(line1 + " "*5 + line2)
#         if i < 2:
#             print("---+---+---" + " "*5 + "---+---+---")
#
# #everything abovve is from ttt.py
#
# def make_empty_board():
#     board = []
#     for i in range(3):
#         board.append([" "]*3)
#     return board
#
# def mark_square_num(): #I didn't make it take in anything
#     num = input("Enter your move: ")
#
#     column = (int(num) - 1) % 3
#     row = (int(num) - 1) // 3
#     board[row][column] = 'X'
#     print_board_and_legend(board)

#Part b Same code copied from A

import random

def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2] # This is the empty board
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) # This is the board with the legend
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")

#everything abovve is from ttt.py

def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

def mark_square_num(mark): #I didn't make it take in anything
    num = input("Enter your move: ")

    column = (int(num) - 1) % 3
    row = (int(num) - 1) // 3
    if mark == "X":
        board[row][column] = 'X'
    if mark == "O":
        board[row][column] = 'O'
    print_board_and_legend(board)

    if is_win(board, mark) == True:
        print (mark + " has won!")
        #the next parts are for fun but don't really work
        play_again = input(" Would you like to play again? y/n: ")
        if input(" Would you like to play again? y/n: ") == 'y':
            make_empty_board
            print_board_and_legend(board)
        if play_again == 'n':
            print ("Have a good day!")
        if play_again != 'n' or 'y':
            print ("I'm sorry I don't understand")


def put_in_board(mark, num): # I took away some parameters
    pass
    #I did it in mark_square_num

# Can do part C using a global variable but is that okay? go to programming for fun


#Problem 2

def get_free_squares(board):
    free_squares = []
    row = 0
    while row < 3:
        column = 0
        while column < 3:
            if board[row][column] == " ":
                free_squares.append((row, column)) #do you want this with index 0 or +1?
            column += 1
        row += 1
    return free_squares

def make_random_move(board, mark):
    free_squares = get_free_squares(board) #do we have to do this part?
    length = len(free_squares)
    square_to_mark = int(length * random.random()) #since length auto +1 cuz index 0
    coord = free_squares[square_to_mark]
    row = coord[0]
    column = coord [1]
    board[row][column] = mark
    print_board_and_legend(board)

#can do part 2c so but have to use global count

#Problem 3
def is_row_all_marked(board, row_i, mark):
    column = 0
    while column < 3: #since start at index 0
        if board[row_i][column] == mark:
            column += 1
        else:
            return False
    return True #since didn't return false

def is_col_all_marked(board, col_i, mark):
    row = 0
    while row < 3:
        if board[row][col_i] == mark:
            row += 1
        else:
            return False
    return True #since didn't return false

def is_win(board, mark):
    for row in range (3):
        if is_row_all_marked(board, row, mark) == True:
            return True
    for col in range (3):
        if is_col_all_marked(board, col, mark) == True:
            return True

    # Time for diagonals

    #decreasing diagonal
    if board[0][0] == mark:
        if board[1][1] == mark:
            if board[2][2] == mark:
                return True
    #inccreasing diagonal
    if board[0][2] == mark:
        if board[1][1] == mark:
            if board[2][0] == mark:
                return True

    return False

def smart_comp_move(board, mark): #I would make the user always "X"
    print("Computer: ")
    free_squares = get_free_squares(board) #do we have to do this part?
    length = len(free_squares)
    count = 0
    for coord in free_squares:
        board[coord[0]][coord[1]] = mark
        count += 1

        #to place winning marker
        #want this one to trump blovking the other person
        winning_move = is_win(board, mark)
        if winning_move == True: #can I put this in the is_win function?
            print_board_and_legend(board)
            print (mark + " has won!")
            #the next parts are for fun but don't really work
            play_again = input(" Would you like to play again? y/n: ")
            if play_again == 'y':
                make_empty_board
                print_board_and_legend(board)
            if play_again == 'n':
                print ("Have a good day!")
            if play_again != 'n' and play_again != 'y':
                print ("I'm sorry I don't understand")
            break
        else:
            board[coord[0]][coord[1]] = " "

        #now to block other people winning
    if count >= length and count < 2*length: #>= since need to ensure can't win
        for coord in free_squares:
            if mark == "X":
                op_mark = "O"
            if mark == "O":
                op_mark = "X"

            board[coord[0]][coord[1]] = op_mark
            count += 1
            op_winning_move = is_win(board, op_mark)
            if op_winning_move == True:
                board[coord[0]][coord[1]] = mark
                print_board_and_legend(board)
            else:
                board[coord[0]][coord[1]] = " "

    if count == length:
        make_random_move(board, mark)


if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)
    mark_square_num("X")
    mark_square_num("X")
    smart_comp_move(board, "O")









