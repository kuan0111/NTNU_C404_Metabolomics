# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:10:14 2024

@author: KLM
"""
import pandas as pd
import matplotlib.pyplot as plt

print('lib loaded successfully')

# read the excel file
df = pd.read_excel('Met Cat NEG.xlsx')
print (df)

# color setting
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

tableau20 = [(r / 255., g / 255., b / 255.) for r, g, b in tableau20]

# font setting
plt.rcParams.update({'font.size': 8, 'font.family': 'Arial'})

# producing stacked bar diagram
ax = df.plot( 
  
  x = 'Chromatographic Conditions', 
  ylabel = 'Chromatographic conditions',
  xlabel = 'Numbers of the identified metabolites',
  kind = 'barh',  
  stacked = True, 
  legend = True,
  title = 'Liver metabolites indentified in ESI(-)',
  color = tableau20
  )

# legend parameters
ax.legend(loc='lower center', bbox_to_anchor=(0.45, -0.4), ncol=3)

for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy() 
    ax.text(x + width / 2, y + height / 2, f'{width:.0f}', 
            horizontalalignment='center', verticalalignment='center')

plt.xticks(fontname='Arial', fontsize=8)
plt.yticks(fontname='Arial',fontsize=8)