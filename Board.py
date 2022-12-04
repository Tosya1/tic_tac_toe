class Board:
    def __init__(self):
        self.__board = Board.__create_board()

    def __create_board():
        board = [[3*i + 1, 3*i + 2, 3*i + 3] for i in range(3)]
        board.extend([[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]])
        return board

    @property
    def board(self):
        return self.__board

    def check_win(self):
        for i in self.__board:
            if i[0] == i[1] == i[2]:
                return True

    def check_draw(self, marks):
        list1 = [marks[0] in i and marks[1] in i for i in self.__board]
        return False in list1
