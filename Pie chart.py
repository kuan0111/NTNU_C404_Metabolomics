# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:31:12 2024

@author: KLM
"""
import matplotlib.pyplot as plt
import numpy as np


met = ['Alcohols', 'Amines', 'Amino acids', 'Carbohydrates', 
'Faty acids', 'Imidazole', 'Indoles', 'Nucleic acids',
'Organic acids', 'Peptides', 'Purines', 'Pyrimidines',
'Quaternary ammonium salts', 'Steroids', 'Others']
# labels for negative mode

values = np.array([12,12,12,12,12,12,12,12,12,12,12,12,12,12,12])
# values for negative mode


plt.rcParams.update({'font.size': 8, 'font.family': 'Arial'})

# Tableau 20 colors
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the range [0, 1] to be compatible with matplotlib
tableau20 = [(r / 255., g / 255., b / 255.) for r, g, b in tableau20]

plt.pie(values,
        labels=met,
        radius = 3,
        textprops={'color':'black', 'weight':'bold', 'size':20},
        colors=tableau20
        )