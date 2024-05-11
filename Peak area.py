# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 12:30:49 2024

@author: KLM
"""

import pandas as pd # data analysis tool
print('loaded successfully')

df = pd.read_excel('C1801FA_TRY.xlsx') #Read the raw data file

df2 = df.groupby("Name")[['Control 1', 'Control 2', 'Control 3', 'Control 4', 'Control 5', 'Low 1', 'Low 2', 'Low 3', 'Low 4', 'Low 5', 'High 1', 'High 2', 'High 3', 'High 4', 'High 5', 'QC 1', 'QC 2', 'QC 3'
]].sum() #integrate the peak area of metabolites in different groups

df2.to_excel('Result.xlsx') #fill the result into a new Excel table
