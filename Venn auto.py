# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 09:12:47 2023

@author: KLM
"""

import pandas as pd
from matplotlib_venn import venn3 
from matplotlib import pyplot as plt

ap1 = [] #amide(+)
an1 = [] #amide(-)
pn1 = [] #pfp(-)

file = pd.read_csv('amide(+).csv')
file1 = pd.read_csv('amide(-).csv')
file2 = pd.read_csv('pfp(-).csv')
ap = file.values.tolist()
an = file1.values.tolist()
pn = file2.values.tolist()

for i in ap:
    x =str(i).replace('[','')
    x = x.replace(']','')
    ap1.append(x)
for i in an:
    x =str(i).replace('[','')
    x = x.replace(']','')
    an1.append(x)
for i in pn:
    x =str(i).replace('[','')
    x = x.replace(']','')
    pn1.append(x)

abc = [i for i in an1 if i in ap1 if i in pn1] #all
ab = [j for j in ap1 if j in an1 if j not in abc] #amide(+) and (-)
ac = [k for k in ap1 if k in pn1 if k not in abc] #amide(+) and pfp
bc = [l for l in an1 if l in pn1 if l not in abc]#amide(-) and pfp
a = [m for m in ap1 if m not in ab if m not in ac if m not in abc ] #amide(+) only
b = [m for m in an1 if m not in ab if m not in bc if m not in abc ] #amide(-) only
c = [m for m in pn1 if m not in bc if m not in ac if m not in abc] 

venn3(subsets = (len(a),len(b),len(ab),len(c),len(ac),len(bc),len(abc)), set_labels = ('Amide, ESI(+)', 'Amide, ESI(-)', 'PFP, ESI(-)'),set_colors = ('mediumblue','darkorange','green'))

plt.savefig('swathcon.tif', dpi=1200)
plt.show()

print(len(a)+len(b)+len(c)+len(ab)+len(ac)+len(bc)+len(abc))

