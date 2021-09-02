# -*- coding: utf-8 -*-
import os
import sys
import json
import tkinter
from tkinter import ttk
from tab_mana import *
from tab_conf import *
from tab_life import *

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('3.15 CWDT Helper')
        self.geometry('720x480')
        self.notebook = ttk.Notebook(self)   
        # Config Tab
        self._tab_conf = TabConf(self.notebook)
        self.notebook.add(self._tab_conf, text='Config')
        # Mana Tab
        self._tab_mana = TabMana(self.notebook, self._tab_conf)
        self.notebook.add(self._tab_mana, text='Mana')
        # Life Tab
        self._tab_life = TabLife(self.notebook, self._tab_conf)
        self.notebook.add(self._tab_life, text='Life')

        self.notebook.pack(expand=1, fill='both')

    def run(self):
        self.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()
