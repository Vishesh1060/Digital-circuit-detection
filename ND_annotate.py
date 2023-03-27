# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:46:28 2023

@author: vishesh
"""
'''
Generated Annotation file format:
    (txt)
    address of file/filename xmin xmax ymin ymax gate-name
'''

import pandas as pd
import numpy as np
import xml.etree.ElementTree as ElemTree
from os import listdir
expf='/content/drive/MyDrive/Group 1 Mini project 2022-23: New Dataset /Exports/Sarthak-Dataset2.csv'
imgf='/content/drive/MyDrive/Group 1 Mini project 2022-23: New Dataset /Sarthak'

l1=listdir(imgf)
Files=[]
for l in l1:
    if(l.endswith("jpg")):
        Files.append(str(str(imgf)+"/"+str(l)))
df1 = pd.read_csv(expf)
df2=df1
df2['image'] = str(imgf)+"/"+df1['image']
print(df1.head(10))
print(df2.head(10))
print(Files[::10])

for i in range(len(df2['image'])):
            df2.to_csv('annotate.txt',mode='a',header=None, index=None, sep=',')