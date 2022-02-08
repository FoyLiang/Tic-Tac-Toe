from ast import literal_eval

def findWinner(board):
    not_complete = False
    for row in board :
        if 0 in row:
            not_complete = True
        if row[0]==row[1]==row[2] and 0 not in row:
            return row[0]
    for colum in range(3) :
        if board[0][colum]==board[1][colum]==board[2][colum] and board[0][colum]!=0 :
            return board[0][colum]
    if board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0] and board[1][1]!=0:
        return board[1][1]
    if not_complete:
        return None

    return "Draw"

def main():
    board = input()
    result = findWinner(literal_eval(board))
    if result == 1:
        print("X Win")
    elif result == 2:
        print("Y Win")
    else:
        print(result)

main()