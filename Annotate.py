# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 16:07:29 2022

@author: vishesh
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ElemTree
from matplotlib import patches
from os import listdir

df1=[]
metadata1={}

# file directory
d="../../classified/"
l1=listdir(d)
Files=[]
for l in l1:
    if(l.endswith("xml")):
        Files.append(d+l)


#filename size.width size.height 
#object.name object.bndbox.xmin object.bndbox.xmax object.bndbox.ymin object.bndbox.ymax
columns=['name','xmin','xmax','ymin','ymax']
metadata=['filename','height','width']
gates=[["and","nand","or","nor","not","xor","xnor"],["r","b","g","c","m","y","mediumseagreen"]]

def parser(File,Columns,md):
    dt={}
    [dt.setdefault(x, []) for x in tuple(Columns)]
    dt2={}
    [dt2.setdefault(x, []) for x in tuple(md)]
    i=0
    dt3=[]
    tree=ElemTree.parse(File)
    for child in tree.getroot():
        if(child.tag=='filename'):
            dt2['filename'].append(child.text)
        elif(child.tag=='size'):
            for child2 in child:
                if(child2.tag=='width'):
                    dt2['width'].append(float(child2.text))
                elif(child2.tag=='height'):
                    dt2['height'].append(float(child2.text))
    for child in tree.getroot():
            if(child.tag=='object'):
                for child2 in child:
                    if(child2.tag=='name'):
                        dt['name']=child2.text
                    elif(child2.tag=='bndbox'):
                        for child3 in child2:
                            if(child3.tag=='xmin'):
                                dt['xmin']=float(child3.text)
                            elif(child3.tag=='ymin'):
                                dt['ymin']=float(child3.text)
                            elif(child3.tag=='xmax'):
                                dt['xmax']=float(child3.text)
                            elif(child3.tag=='ymax'):
                                dt['ymax']=float(child3.text)
                dt3.append(dt.copy())
                i=i+1
    return dt3,dt2


def process(Files,columns,metadata):
    for file in Files:
        df1,metadata1=parser(file,columns,metadata)
        df=pd.DataFrame(df1)
        metadata=pd.DataFrame(metadata1)
        df5=pd.DataFrame(columns=['filepath','x1','y1','x2','y2','class_name'])
        for i in range(len(df['name'])):
            df5.loc[len(df5.index)+1]=[str('C:\\Users\\vishe.IDEAPADFLEX\\Desktop\\CGHD-1152\\Frcnn\\Keras-frcnn-master\\keras_frcnn\\Train_images\\'+metadata['filename'][0]),str(int(df['xmin'][i])),str(int(df['ymin'][i])),str(int(df['xmax'][i])),str(int(df['ymax'][i])),str(df['name'][i])]

#        df5.to_csv('../out/annotate.txt',mode='a',header=None, index=None, sep=',')
        print('done')
    return df

# image='../C144_D2_P4.jpg'
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# image=plt.imread(image)
# plt.imshow(image)
# edgecolor='w'
df=pd.DataFrame()
df=process(Files,columns,metadata)

# for _,row in df.iterrows():
#     xmin = row.xmin
#     xmax = row.xmax
#     ymin = row.ymin
#     ymax = row.ymax    
#     width = xmax - xmin
#     height = ymax - ymin
#     if row[0] == gates[0][0]:
#         edgecolor = gates[1][0]
#         ax.annotate('AND', xy=(xmax-40,ymin+20))
#     elif row[0] == gates[0][1]:
#         edgecolor = gates[1][1]
#         ax.annotate('NAND', xy=(xmax-40,ymin+20))
#     elif row[0] == gates[0][2]:
#         edgecolor = gates[1][2]
#         ax.annotate('OR', xy=(xmax-40,ymin+20))
#     elif row[0] == gates[0][3]:
#         edgecolor = gates[1][3]
#         ax.annotate('NOR', xy=(xmax-40,ymin+20))
#     elif row[0] == gates[0][4]:
#         edgecolor = gates[1][4]
#         ax.annotate('NOT', xy=(xmax-40,ymin+20))
#     elif row[0] == gates[0][5]:
#         edgecolor = gates[1][5]
#         ax.annotate('XOR', xy=(xmax-40,ymin+20))
#     elif row[0] == gates[0][6]:
#         edgecolor = gates[1][6]
#         ax.annotate('OR', xy=(xmax-40,ymin+20))  
#     elif row[0] == 'terminal':
#         ax.annotate('T', xy=(xmax-40,ymin+20))
#     rect = patches.Rectangle((xmin,ymin), width, height, edgecolor = edgecolor, facecolor = 'none')    
#     ax.add_patch(rect)


