import json
import math
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

class TabLife(ttk.Frame):
    def __init__(self, parent, tabConf, *args, **kwargs):
        super().__init__()
        self.tickRate = 30
        self.tabConf = tabConf
        self.EHP = {}
        self.EHP['basic'] = 0
        self.EHP['fight'] = 0
        self.row = 0

        # Labels
        ## Titles
        self._label_configs = ttk.Label(self, text='Configurations')
        self._label_values = ttk.Label(self, text='Values')
        self._label_options = ttk.Label(self, text='Options')
        self._label_splash1 = ttk.Label(self, text=('-'*48))
        self._label_splash2 = ttk.Label(self, text=('-'*48))
        self._label_splash3 = ttk.Label(self, text=('-'*48))

        self.row = self.row + 1
        self._label_configs.grid(row=self.row, column=0)
        self._label_values.grid(row=self.row, column=1)
        self._label_options.grid(row=self.row, column=2, columnspan=3)

        self.row = self.row + 1
        self._label_splash1.grid(row=self.row, column=0)
        self._label_splash2.grid(row=self.row, column=1)
        self._label_splash3.grid(row=self.row, column=2)

        # Configurations
        self._label_life = ttk.Label(self, text='Life (value)')
        self._label_life_regen_value = ttk.Label(self, text='Life Regen Value (per sec)')
        self._label_life_regen_rate = ttk.Label(self, text='Life Regen Rate (%)')
        self._label_life_recoup_rate = ttk.Label(self, text='Life Recoup Rate (%)')
        self._label_life_recover_rate = ttk.Label(self, text='Life Recover Rate (%)')

        # Entries
        self._txt_life = ttk.Entry(self, width=10)
        self._txt_life_regen_value = ttk.Entry(self, width=10)
        self._txt_life_regen_rate = ttk.Entry(self, width=10)
        self._txt_life_recoup_rate = ttk.Entry(self, width=10)
        self._txt_life_recover_rate = ttk.Entry(self, width=10)

        # Buttons
        self._btn_analysis = ttk.Button(self, text='analysis', command=self.analysis)
        self._btn_loadConf = ttk.Button(self, text='load', command=self.loadConf)
        self._btn_saveConf = ttk.Button(self, text='save', command=self.saveConf)
        self._btn_exitWindow = ttk.Button(self, text='exit', command=self.exitWindow)

        # Grids
        self.row = self.row + 1
        self._label_life.grid(row=self.row, column=0)
        self._txt_life.grid(row=self.row, column=1)
        self._btn_analysis.grid(row=self.row, column=2)

        self.row = self.row + 1
        self._label_life_regen_value.grid(row=self.row, column=0)
        self._txt_life_regen_value.grid(row=self.row, column=1)

        self.row = self.row + 1
        self._label_life_regen_rate.grid(row=self.row, column=0)
        self._txt_life_regen_rate.grid(row=self.row, column=1)
        self._btn_saveConf.grid(row=self.row, column=2)

        self.row = self.row + 1
        self._label_life_recoup_rate.grid(row=self.row, column=0)
        self._txt_life_recoup_rate.grid(row=self.row, column=1)
        self._btn_loadConf.grid(row=self.row, column=2)

        self.row = self.row + 1
        self._label_life_recover_rate.grid(row=self.row, column=0)
        self._txt_life_recover_rate.grid(row=self.row, column=1)
        self._btn_exitWindow.grid(row=self.row, column=2)
        
        self.row = self.row + 1
        self._label_splash4 = ttk.Label(self, text=('-'*48))
        self._label_splash5 = ttk.Label(self, text=('-'*48))
        self._label_splash6 = ttk.Label(self, text=('-'*48))
        self._label_splash4.grid(row=self.row, column=0)
        self._label_splash5.grid(row=self.row, column=1)
        self._label_splash6.grid(row=self.row, column=2)

        # Default
        self.loadDefaultValue()

    def setEntryInput(self, entry, text):
        entry.delete(0, 'end')
        entry.insert(0, text)

    def loadDefaultValue(self):
        self.setEntryInput(self._txt_life, '5000')
        self.setEntryInput(self._txt_life_regen_value, '10')
        self.setEntryInput(self._txt_life_regen_rate, '26.4')
        self.setEntryInput(self._txt_life_recoup_rate, '20')
        self.setEntryInput(self._txt_life_recover_rate, '54')
    
    def analysis(self):
        # Basic Informaiton
        lifeInfo = {}
        lifeInfo['life'] = float(self._txt_life.get())
        lifeInfo['life_regen_value'] = float(self._txt_life_regen_value.get())
        lifeInfo['life_regen_rate'] = float(self._txt_life_regen_rate.get()) / 100
        lifeInfo['life_recoup_rate'] = float(self._txt_life_recoup_rate.get()) / 100
        lifeInfo['life_recover_rate'] = (100 + float(self._txt_life_recover_rate.get())) / 100
        lifeInfo['life_regen'] = lifeInfo['life'] * lifeInfo['life_regen_rate'] + lifeInfo['life_regen_value']
        basicInfo = self.tabConf.getValues()

        # Basic
        rows = self.calcEHP('basic', basicInfo, lifeInfo)
        # Fight
        rows = self.calcEHP('fight', basicInfo, lifeInfo)
        self.row = self.row - (rows * 2)

    def calcEHP(self, mode, basicInfo, lifeInfo):
        EHP = 0
        self.EHP[mode] = 0
        dictIndex = 0
        dictRecoup = {}
        life_recoup_round = 0
        _temp = basicInfo[mode].split('/')
        dmg_taken = float(_temp[0])
        tick_rate1 = int(basicInfo['freq'])
        
        isDamageTaken = False
        for round in range(4800):
            # Life Recoup per tick
            if isDamageTaken is True:
                life_recoup_round += dmg_taken * lifeInfo['life_recoup_rate'] * lifeInfo['life_recover_rate'] / 120
                isDamageTaken = False
            if round in dictRecoup:
                life_recoup_round -= dmg_taken * lifeInfo['life_recoup_rate'] * lifeInfo['life_recover_rate'] / 120
            # Life Cost
            life_cost_round = 0
            if round % tick_rate1 is 0:
                life_cost_round = dmg_taken
                # Recoup Dict
                dictIndex = round + 120
                dictRecoup[dictIndex] = True
                isDamageTaken = True

            # Life Regen per tick
            life_regen_round = lifeInfo['life_regen'] * lifeInfo['life_recover_rate'] / self.tickRate

            # Summary
            EHP = EHP + life_recoup_round + life_regen_round - life_cost_round

            self.EHP[mode] = min(self.EHP[mode], EHP)
        # Show Outcomes on Frame
        counter = 0
        _label_life_EHP = ttk.Label(self)
        _value_life_EHP = ttk.Label(self)

        counter += 1
        self.row = self.row + 1
        _label_life_EHP['text'] = 'Life Pool ({})'.format(mode)
        _value_life_EHP['text'] = str(self.EHP[mode])
        
        _label_life_EHP.grid(row=self.row, column=0, sticky='w')
        _value_life_EHP.grid(row=self.row, column=1)

        _label_life_balance = ttk.Label(self)
        _value_life_balance = ttk.Label(self)

        counter += 1
        self.row = self.row + 1
        _label_life_balance['text'] = 'Life will strike a balance ({})'.format(mode)
        _value_life_balance['text'] = 'True' if EHP >= 0 else 'False'
        _label_life_balance.grid(row=self.row, column=0, sticky='w')
        _value_life_balance.grid(row=self.row, column=1)

        return counter

    def loadConf(self):
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))

        file = fd.askopenfile(parent=self, mode='r', title='JSON Config')
        if file:
            try:
                config = json.load(file)
                self.setEntryInput(self._txt_life, config['life'])
                self.setEntryInput(self._txt_life_regen_value, config['life_regen_value'])
                self.setEntryInput(self._txt_life_regen_rate, config['life_regen_rate'])
                self.setEntryInput(self._txt_life_recoup_rate, config['life_recoup_rate'])
                self.setEntryInput(self._txt_life_recover_rate, config['life_recover_rate'])
            except:
                print ('[Error] - Load Configuration File Error.')

    def saveConf(self):
        config = {}
        config['life'] = self._txt_mana.get()
        config['life_regen_value'] = self._txt_mana_regen_value.get()
        config['life_regen_rate'] = self._txt_mana_regen_rate.get()
        config['life_recoup_rate'] = self._txt_mana_recoup_rate.get()
        config['life_recover_rate'] = self._txt_mana_recover_rate.get()

        with open('./datas/lifeConf.txt', 'w') as output_file:
            json.dump(config, output_file)

    def exitWindow(self):
        exit(1)
