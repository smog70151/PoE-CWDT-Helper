import json
import math
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

class TabConf(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__()
        self.tickRate = 30
        self.dmgTaken = 350
        self.basicInfo = {}
        self.row = 0

        # Labels
        ## Titles
        self._label_configs = ttk.Label(self, text='Configurations')
        self._label_values = ttk.Label(self, text='Values')
        self._label_options = ttk.Label(self, text='Options')
        self._label_splash1 = ttk.Label(self, text=('-'*48))
        self._label_splash2 = ttk.Label(self, text=('-'*48))
        self._label_splash3 = ttk.Label(self, text=('-'*48))
        self._label_splash4 = ttk.Label(self, text=('-'*48))
        self._label_splash5 = ttk.Label(self, text=('-'*48))
        self._label_splash6 = ttk.Label(self, text=('-'*48))

        self.row = self.row + 1
        self._label_configs.grid(row=self.row, column=0)
        self._label_values.grid(row=self.row, column=1)
        self._label_options.grid(row=self.row, column=2, columnspan=3)

        self.row = self.row + 1
        self._label_splash1.grid(row=self.row, column=0)
        self._label_splash2.grid(row=self.row, column=1)
        self._label_splash3.grid(row=self.row, column=2)

        ## Configurations
        self._label_phy_dmg_reduction = ttk.Label(self, text='phy DMG Reduction')
        self._label_inc_dmg_taken = ttk.Label(self, text='inc DMG Taken')
        self._label_cdr = ttk.Label(self, text='Cooldown Recover Rate')
        self._label_minion_num1 = ttk.Label(self, text='Minion Numbers (Basic)')
        self._label_minion_num2 = ttk.Label(self, text='Minion Numbers (Fight)')
        self._label_cwdt_damage_taken = ttk.Label(self, text='CWDT DMG Taken(High Level)')
        
        # Entries
        self._txt_phy_dmg_reduction = ttk.Entry(self, width=10)
        self._txt_inc_dmg_taken = ttk.Entry(self, width=10)
        self._txt_cdr = ttk.Entry(self, width=10)
        self._txt_minion_num1 = ttk.Entry(self, width=10)
        self._txt_minion_num2 = ttk.Entry(self, width=10)
        self._txt_cwdt_damage_taken = ttk.Entry(self, width=10)

        # Buttons
        self._btn_analysis = ttk.Button(self, text='analysis', command=self.analysis)
        self._btn_loadConf = ttk.Button(self, text='load', command=self.loadConf)
        self._btn_saveConf = ttk.Button(self, text='save', command=self.saveConf)
        self._btn_exitWindow = ttk.Button(self, text='exit', command=self.exitWindow)
        
        # Grids
        self.row = self.row + 1
        self._label_phy_dmg_reduction.grid(row=self.row, column=0, sticky='w')
        self._txt_phy_dmg_reduction.grid(row=self.row, column=1)
        self._btn_analysis.grid(row=self.row, column=2)

        self.row = self.row + 1
        self._label_inc_dmg_taken.grid(row=self.row, column=0, sticky='w')
        self._txt_inc_dmg_taken.grid(row=self.row, column=1)
        

        self.row = self.row + 1
        self._label_cdr.grid(row=self.row, column=0, sticky='w')
        self._txt_cdr.grid(row=self.row, column=1)
        self._btn_saveConf.grid(row=self.row, column=2)

        self.row = self.row + 1
        self._label_minion_num1.grid(row=self.row, column=0, sticky='w')
        self._txt_minion_num1.grid(row=self.row, column=1)
        self._btn_loadConf.grid(row=self.row, column=2)
        
        self.row = self.row + 1
        self._label_minion_num2.grid(row=self.row, column=0, sticky='w')
        self._txt_minion_num2.grid(row=self.row, column=1)
        self._btn_exitWindow.grid(row=self.row, column=2)
        
        self.row = self.row + 1
        self._label_cwdt_damage_taken.grid(row=self.row, column=0, sticky='w')
        self._txt_cwdt_damage_taken.grid(row=self.row, column=1)

        self.row = self.row + 1
        self._label_splash4.grid(row=self.row, column=0)
        self._label_splash5.grid(row=self.row, column=1)
        self._label_splash6.grid(row=self.row, column=2)

        # Default
        self.loadDefaultValue()

    def loadDefaultValue(self):
        self._txt_phy_dmg_reduction.insert(0, '37')
        self._txt_cdr.insert(0, '11')
        self._txt_inc_dmg_taken.insert(0, '0')
        self._txt_minion_num1.insert(0, '3')
        self._txt_minion_num2.insert(0, '4')
        self._txt_cwdt_damage_taken.insert(0, '2864')

    def analysis(self):
        '''
            1. dmg_taken_per_sec = dmgTaken(350) * reduction * (1+inc) * num / frequency
        '''
        phy_dmg_reduction = float(self._txt_phy_dmg_reduction.get())/100
        inc_dmg_taken = float(self._txt_inc_dmg_taken.get())/100
        cdr_rate = float(100+int(self._txt_cdr.get())) / 100
        _value_cwdt_freq = math.ceil(0.25 / cdr_rate / float(1/30))
        minion_num1 = int(self._txt_minion_num1.get())
        minion_num2 = int(self._txt_minion_num2.get())
        cwdt_damage_taken = float(self._txt_cwdt_damage_taken.get())
        self.dmg_taken_basic_time = self.dmgTaken * (1-phy_dmg_reduction) * (1+inc_dmg_taken) * minion_num1
        self.dmg_taken_fight_time = self.dmgTaken * (1-phy_dmg_reduction) * (1+inc_dmg_taken) * minion_num2
        self.dmg_taken_basic_sec = self.dmg_taken_basic_time * self.tickRate / _value_cwdt_freq
        self.dmg_taken_fight_sec = self.dmg_taken_fight_time * self.tickRate / _value_cwdt_freq
        _value_dmg_taken_basic_time = str(int(self.dmg_taken_basic_time)) + '/' + str(int(cwdt_damage_taken/self.dmg_taken_basic_time))
        _value_dmg_taken_fight_time = str(int(self.dmg_taken_fight_time)) + '/' + str(int(cwdt_damage_taken/self.dmg_taken_fight_time))

        # Basic Info
        self.basicInfo['freq'] = _value_cwdt_freq
        self.basicInfo['basic'] = _value_dmg_taken_basic_time
        self.basicInfo['fight'] = _value_dmg_taken_fight_time

        # Show Outcomes on Frame
        self._label_cwdt_freq = ttk.Label(self, text='CWDT Frequency')
        self._label_dmg_taken_basic_time = ttk.Label(self, text='B-DMG Taken/time')
        self._label_dmg_taken_fight_time = ttk.Label(self, text='F-DMG Taken/time')
        self._label_dmg_taken_basic_sec = ttk.Label(self, text='B-DMG Taken/sec')
        self._label_dmg_taken_fight_sec = ttk.Label(self, text='F-DMG Taken/sec')

        self._label_cwdt_freq.grid(row=10, column=0, sticky='w')
        self._label_dmg_taken_basic_time.grid(row=11, column=0, sticky='w')
        self._label_dmg_taken_fight_time.grid(row=12, column=0, sticky='w')
        self._label_dmg_taken_basic_sec.grid(row=13, column=0, sticky='w')
        self._label_dmg_taken_fight_sec.grid(row=14, column=0, sticky='w')

        self._value_cwdt_freq = ttk.Label(self, text=_value_cwdt_freq)
        self._value_dmg_taken_basic_time = ttk.Label(self, text=_value_dmg_taken_basic_time)
        self._value_dmg_taken_fight_time = ttk.Label(self, text=_value_dmg_taken_fight_time)
        self._value_dmg_taken_basic_sec = ttk.Label(self, text=str(int(self.dmg_taken_basic_sec)))
        self._value_dmg_taken_fight_sec = ttk.Label(self, text=str(int(self.dmg_taken_fight_sec)))

        self._value_cwdt_freq.grid(row=10, column=1)
        self._value_dmg_taken_basic_time.grid(row=11, column=1)
        self._value_dmg_taken_fight_time.grid(row=12, column=1)
        self._value_dmg_taken_basic_sec.grid(row=13, column=1)
        self._value_dmg_taken_fight_sec.grid(row=14, column=1)

    def setEntryInput(self, entry, text):
        entry.delete(0, 'end')
        entry.insert(0, text)
    
    def loadConf(self):
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))

        file = fd.askopenfile(parent=self, mode='r', title='JSON Config')
        if file:
            try:
                config = json.load(file)
                self.setEntryInput(self._txt_phy_dmg_reduction, config['phy_dmg_reduction'])
                self.setEntryInput(self._txt_inc_dmg_taken, config['inc_dmg_taken'])
                self.setEntryInput(self.cdr, config['cdr'])
                self.setEntryInput(self._txt_minion_num1, config['minion_num1'])
                self.setEntryInput(self._txt_minion_num2, config['minion_num2'])
                self.setEntryInput(self._txt_cwdt_damage_taken, config['cwdt_damage_taken'])
            except:
                print ('[Error] - Load Configuration File Error.')

    def saveConf(self):
        config = {}
        config['phy_dmg_reduction'] = self._txt_phy_dmg_reduction.get()
        config['inc_dmg_taken'] = self._txt_inc_dmg_taken.get()
        config['cdr'] = self._txt_cdr.get()
        config['minion_num1'] = self._txt_minion_num1.get()
        config['minion_num2'] = self._txt_minion_num2.get()
        config['cwdt_damage_taken'] = self._txt_cwdt_damage_taken.get()

        with open('./datas/configuration.txt', 'w') as output_file:
            json.dump(config, output_file)

    def exitWindow(self):
        exit(1)

    def getValues(self):
        self.analysis()
        return self.basicInfo
