# Path Of Exile CWDT Helper
## Motivation
- PoE 3.15 版本中針對觸發類型提出許多改動，受傷時施放輔助從原本的 0% 改動至 250%。這項改動對受傷時施放相關的流派影響慎巨，從原先不需要考慮耗魔，到現在需要考慮魔量平衡的問題。慶幸的是受傷時施放流派可以透過補償來解決魔力問題，但這項解決方式是需要**有效啟動的魔力量**；不幸的是 PoB 沒有提供相關的功能，因此寫了這個模擬程式來幫助計算。

- There are many problems you need to handle if you wanna play a CWDT build in PoE. It is more difficult to design a CWDT build in PoE 3.15 than the previous leagues. Due to the overwhelming mana cost, it is a must to find a method striking a balance between mana cost & mana recovery. 

## Features
1. CWDT Basic Information (Basic/Fight)
2. Calculate the life pool (Basic/Fight)
3. Calculate the mana pool (Basic/Fight)

## Tab Details
- Basic Configurations
  1. Physical Damage Reduction
  2. Increase Damage Taken
  3. Cooldown Recover Rate 
  4. Minion Numbers (basic)
  5. Minion Numbers (fight)
  6. High Level CWDT Damage Taken  (value)
- Mana Tab
  1. Mana (value)
  2. Mana Regeration Value (per sec)
  3. Mana Regeneration Rate (%)
  4. Mana Recoup Rate (%)
  5. Mana Recover Rate (%)
  6. Low Level CWDT mana cost (per time)
  7. High Level CWDT mana cost (per time)
- Life Tab
  1. Life (value) 
  2. Life Regeneration Value (per sec)
  3. Life Regeneration Rate (%)
  4. Life Recoup Rate (%)
  5. Life Recover Rate (%)
- Button Options
  1. Analysis
  2. Output Dialog **[Undo]**
  3. Save Configuration
  4. Load Configuration
  5. Exit

## Undo
- The Agonist
- Blood Rage
- Rightous Fire
- Lavianga's Spirit
- Leech Recovery System
- Indigon CWDT Simulation

## Packing executable file
```bash
$ pyinstaller --onefile -w ./cwdt-calculator.py
```