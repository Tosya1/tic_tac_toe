from Player_vs_bot import*

class Player_vs_smart_bot(Player_vs_bot):
    def __init__(self, board, players, view):
        super().__init__(board, players, view)

    def bot_select_cell(self):
        m1 = []
        m2 = []
        m3 = []
        m4 = []
        m5 = []
        for i in range(len(self.board.board)):
            if self.board.board[i].count(self.player.mark) == 2 and self.board.board[i].count(self.marks[self.marks.index(self.player.mark) -1]) == 0:
                m1.append(list(filter(lambda x: x not in self.marks, self.board.board[i]))[0])
            if self.board.board[i].count(self.marks[self.marks.index(self.player.mark) -1]) == 2 and self.board.board[i].count(self.player.mark) == 0:
                m2.append(list(filter(lambda x: x not in self.marks, self.board.board[i]))[0])
            if self.board.board[i].count(self.player.mark) > 0 and self.board.board[i].count(self.marks[self.marks.index(self.player.mark) -1]) == 0:
                m3.append(choice(list(filter(lambda x: x not in self.marks, self.board.board[i]))))
            if self.board.board[i].count(self.player.mark) == 0 and self.board.board[i].count(self.marks[self.marks.index(self.player.mark) -1]) == 0:
                m4.append(choice(list(filter(lambda x: int(x) % 2 != 0, self.board.board[i]))))
            if self.board.board[i].count(self.player.mark) == 0 and self.board.board[i].count(self.marks[self.marks.index(self.player.mark) -1]) == 1:
                m5.append(choice(list(filter(lambda x: x not in self.marks, self.board.board[i]))))
        if len(m1) > 0:
            return choice(m1)
        if len(m2) > 0:
            return choice(m2)
        if len(m3) > 0:
            return choice(m3)
        if len(m4) > 0:
            return choice(m4)
        if len(m5) > 0:
            return choice(m5)