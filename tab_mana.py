import json
import math
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

class TabMana(ttk.Frame):
    def __init__(self, parent, tabConf, *args, **kwargs):
        super().__init__()
        self.tickRate = 30
        self.tabConf = tabConf
        self.EMP = {}
        self.EMP['basic'] = 0
        self.EMP['fight'] = 0
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
        self._label_mana = ttk.Label(self, text='Mana (value)')
        self._label_mana_regen_value = ttk.Label(self, text='Mana Regen Value (per sec)')
        self._label_mana_regen_rate = ttk.Label(self, text='Mana Regen Rate (%)')
        self._label_mana_recoup_rate = ttk.Label(self, text='Mana Recoup Rate (%)')
        self._label_mana_recover_rate = ttk.Label(self, text='Mana Recover Rate (%)')
        self._label_mana_cost1 = ttk.Label(self, text='Low Level Mana Cost (per time)')
        self._label_mana_cost2 = ttk.Label(self, text='High Level Mana Cost (per time)')

        # Entries
        self._txt_mana = ttk.Entry(self, width=10)
        self._txt_mana_regen_value = ttk.Entry(self, width=10)
        self._txt_mana_regen_rate = ttk.Entry(self, width=10)
        self._txt_mana_recoup_rate = ttk.Entry(self, width=10)
        self._txt_mana_recover_rate = ttk.Entry(self, width=10)
        self._txt_mana_cost1 = ttk.Entry(self, width=10)
        self._txt_mana_cost2 = ttk.Entry(self, width=10)

        # Buttons
        self._btn_analysis = ttk.Button(self, text='analysis', command=self.analysis)
        self._btn_loadConf = ttk.Button(self, text='load', command=self.loadConf)
        self._btn_saveConf = ttk.Button(self, text='save', command=self.saveConf)
        self._btn_exitWindow = ttk.Button(self, text='exit', command=self.exitWindow)

        # Grids
        self.row = self.row + 1
        self._label_mana.grid(row=self.row, column=0)
        self._txt_mana.grid(row=self.row, column=1)
        self._btn_analysis.grid(row=self.row, column=2)

        self.row = self.row + 1
        self._label_mana_regen_value.grid(row=self.row, column=0)
        self._txt_mana_regen_value.grid(row=self.row, column=1)

        self.row = self.row + 1
        self._label_mana_regen_rate.grid(row=self.row, column=0)
        self._txt_mana_regen_rate.grid(row=self.row, column=1)
        self._btn_saveConf.grid(row=self.row, column=2)

        self.row = self.row + 1
        self._label_mana_recoup_rate.grid(row=self.row, column=0)
        self._txt_mana_recoup_rate.grid(row=self.row, column=1)
        self._btn_loadConf.grid(row=self.row, column=2)

        self.row = self.row + 1
        self._label_mana_recover_rate.grid(row=self.row, column=0)
        self._txt_mana_recover_rate.grid(row=self.row, column=1)
        self._btn_exitWindow.grid(row=self.row, column=2)

        self.row = self.row + 1
        self._label_mana_cost1.grid(row=self.row, column=0)
        self._txt_mana_cost1.grid(row=self.row, column=1)
        
        self.row = self.row + 1
        self._label_mana_cost2.grid(row=self.row, column=0)
        self._txt_mana_cost2.grid(row=self.row, column=1)

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
        self.setEntryInput(self._txt_mana, '1000')
        self.setEntryInput(self._txt_mana_regen_value, '0')
        self.setEntryInput(self._txt_mana_regen_rate, '1.8')
        self.setEntryInput(self._txt_mana_recoup_rate, '20')
        self.setEntryInput(self._txt_mana_recover_rate, '0')
        self.setEntryInput(self._txt_mana_cost1, '88')
        self.setEntryInput(self._txt_mana_cost2, '122')
    
    def analysis(self):
        # Basic Informaiton
        manaInfo = {}
        manaInfo['mana'] = float(self._txt_mana.get())
        manaInfo['mana_regen_value'] = float(self._txt_mana_regen_value.get())
        manaInfo['mana_regen_rate'] = float(self._txt_mana_regen_rate.get()) / 100
        manaInfo['mana_recoup_rate'] = float(self._txt_mana_recoup_rate.get()) / 100
        manaInfo['mana_recover_rate'] = (100 + float(self._txt_mana_recover_rate.get())) / 100
        manaInfo['mana_regen'] = manaInfo['mana'] * manaInfo['mana_regen_rate'] + manaInfo['mana_regen_value']
        mana_cost1 = float(self._txt_mana_cost1.get())
        mana_cost2 = float(self._txt_mana_cost2.get())
        basicInfo = self.tabConf.getValues()

        # Basic
        rows = self.calcEMP('basic', basicInfo, manaInfo, mana_cost1, mana_cost2)
        # Fight
        rows = self.calcEMP('fight', basicInfo, manaInfo, mana_cost1, mana_cost2)
        self.row = self.row - (rows * 2)

    def calcEMP(self, mode, basicInfo, manaInfo, mana_cost1, mana_cost2):
        EMP = 0
        self.EMP[mode] = 0
        dictIndex = 0
        dictRecoup = {}
        mana_recoup = 0
        _temp = basicInfo[mode].split('/')
        dmg_taken = float(_temp[0])
        tick_rate1 = basicInfo['freq']
        tick_rate2 = tick_rate1 * int(_temp[1])
        
        isValid = False
        isDamageTaken = False
        for round in range(4800):
            # Mana Recoup per tick
            if isDamageTaken is True:
                mana_recoup += dmg_taken * manaInfo['mana_recoup_rate'] * manaInfo['mana_recover_rate'] / 120
                isDamageTaken = False
            if round in dictRecoup:
                mana_recoup -= dmg_taken * manaInfo['mana_recoup_rate'] * manaInfo['mana_recover_rate'] / 120
            # Mana Cost
            mana_cost_round = 0
            if round % tick_rate2 is 0 and isValid is True:
                mana_cost_round = mana_cost_round + mana_cost2
            if round % tick_rate1 is 0:
                mana_cost_round = mana_cost_round + mana_cost1
                # Recoup Dict
                dictIndex = round + 120
                dictRecoup[dictIndex] = True
                isValid = True
                isDamageTaken = True

            # Mana Regen per tick
            mana_regen_round = manaInfo['mana_regen'] * manaInfo['mana_recover_rate'] / self.tickRate

            # Summary
            EMP = EMP + mana_recoup + mana_regen_round - mana_cost_round

            self.EMP[mode] = min(self.EMP[mode], EMP)
        # Show Outcomes on Frame
        counter = 0
        _label_mana_EMP = ttk.Label(self)
        _value_mana_EMP = ttk.Label(self)

        counter += 1
        self.row = self.row + 1
        _label_mana_EMP['text'] = 'Mana Pool ({})'.format(mode)
        _value_mana_EMP['text'] = str(self.EMP[mode])
        
        _label_mana_EMP.grid(row=self.row, column=0, sticky='w')
        _value_mana_EMP.grid(row=self.row, column=1)

        _label_mana_balance = ttk.Label(self)
        _value_mana_balance = ttk.Label(self)

        counter += 1
        self.row = self.row + 1
        _label_mana_balance['text'] = 'Mana will strike a balance ({})'.format(mode)
        _value_mana_balance['text'] = 'True' if EMP >= 0 else 'False'
        _label_mana_balance.grid(row=self.row, column=0, sticky='w')
        _value_mana_balance.grid(row=self.row, column=1)

        return counter

    def loadConf(self):
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))

        file = fd.askopenfile(parent=self, mode='r', title='JSON Config')
        if file:
            try:
                config = json.load(file)
                self.setEntryInput(self._txt_mana, config['mana'])
                self.setEntryInput(self._txt_mana_regen_value, config['mana_regen_value'])
                self.setEntryInput(self._txt_mana_regen_rate, config['mana_regen_rate'])
                self.setEntryInput(self._txt_mana_recoup_rate, config['mana_recoup_rate'])
                self.setEntryInput(self._txt_mana_recover_rate, config['mana_recover_rate'])
                self.setEntryInput(self._txt_mana_cost1, config['mana_cost1'])
                self.setEntryInput(self._txt_mana_cost2, config['mana_cost2'])
            except:
                print ('[Error] - Load Configuration File Error.')

    def saveConf(self):
        config = {}
        config['mana'] = self._txt_mana.get()
        config['mana_regen_value'] = self._txt_mana_regen_value.get()
        config['mana_regen_rate'] = self._txt_mana_regen_rate.get()
        config['mana_recoup_rate'] = self._txt_mana_recoup_rate.get()
        config['mana_recover_rate'] = self._txt_mana_recover_rate.get()
        config['mana_cost1'] = self._txt_mana_cost1.get()
        config['mana_cost2'] = self._txt_mana_cost2.get()

        with open('./datas/manaConf.txt', 'w') as output_file:
            json.dump(config, output_file)

    def exitWindow(self):
        exit(1)
