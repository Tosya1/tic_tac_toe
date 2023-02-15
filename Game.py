from View import *
from Player_vs_player import *
from Player_vs_bot import *
from Player_vs_smart_bot import *
from Player import *
from Players_bot import *
from Board import *


class Game:
    def __init__(self, view):
        self.view = view

    def btn_click_2plrs(self):
        self.view.window.destroy()
        Player_vs_player(Board(), Players(View()), View()).init()

    def btn_click_bot(self):
        self.view.window.destroy()
        Player_vs_bot(Board(), Players_bot(View()), View()).init()

    def btn_click_smart_bot(self):
        self.view.window.destroy()
        Player_vs_smart_bot(Board(), Players_bot(View()), View()).init()

    def run(self):
        self.view.create_window()
        self.view.window.geometry(START_WIN_SIZE)
        lbl = self.view.create_label(
            self.view.window,
            MSG_SELECT_GAME,
            BG_BASE,
            FG,
            FONT_SIZE,
            0,
            0,
            MSG_PAD
        )
        lbl.pack(padx=BTNS_PAD, pady=BTNS_PAD)
        btn = self.view.create_button(BTN_GAME_2PLAYERS, self.btn_click_2plrs)
        btn['width'] = BTNS_WIDTH
        btn.pack(padx=BTNS_PAD, pady=BTNS_PAD, ipady=BTNS_PAD)
        btn = self.view.create_button(BTN_GAME_BOT, self.btn_click_bot)
        btn['width'] = BTNS_WIDTH
        btn.pack(padx=BTNS_PAD, pady=BTNS_PAD, ipady=BTNS_PAD)
        btn = self.view.create_button(
            BTN_GAME_SMART_BOT, self.btn_click_smart_bot)
        btn['width'] = BTNS_WIDTH
        btn.pack(padx=BTNS_PAD, pady=BTNS_PAD, ipady=BTNS_PAD)
        self.view.window.mainloop()
