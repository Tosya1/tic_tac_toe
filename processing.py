from random import choice

def get_board ():
    board = [[3*i + 1, 3*i + 2, 3*i + 3] for i in range(3)]
    board.extend([[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]])
    return board
    
def toss_player (players):
        player = choice(players)
        return player

def toss_mark (marks):
        mark = choice(marks)
        return mark

def check_win (board):
    for i in board:
        if i[0] == i[1] == i[2]:
            return True

def check_draw(board, marks):
    list1 = [marks[0] in i and marks[1] in i for i in board]
    return False in list1