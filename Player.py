from random import choice
from constants import X_COLOR, O_COLOR

class Player:
    def __init__(self, name):
        self.__name = name
        self.__color = ''
        self.__mark = ''
        self.__wins = 0
        self.__draws = 0
        self.__losses = 0

    @property
    def name(self):
        return self.__name

    @property
    def color (self):
        return self.__color

    @property
    def mark (self):
        return self.__mark

    @property
    def wins (self):
        return self.__wins

    @property
    def draws (self):
        return self.__draws   

    @property
    def losses (self):
        return self.__losses      

    def set_color(self, marks):
        if self.__mark == marks[0]:
                self.__color = X_COLOR
        else:
                self.__color = O_COLOR

    @mark.setter
    def mark (self, mark):
        self.__mark = mark

    def add_win(self):
        self.__wins = self.__wins + 1

    def add_draw(self):
        self.__draws = self.__draws + 1

    def add_loss(self):
        self.__losses = self.__losses +1

    def toss_mark (marks):
            mark = choice(marks)
            return mark

    def toss_player (players):
            player = choice(players)
            return player

