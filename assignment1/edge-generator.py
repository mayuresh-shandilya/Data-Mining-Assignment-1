#!/usr/bin/env python
# coding: utf-8

# In[4]:


import json
import csv
import numpy as np
import pandas as pd


# In[5]:


dist=json.load(open("neighbor-districts-modified.json","r"))


# In[6]:


list1=[]
list2=[]
for i,j in dist.items():
    for k in j:
        list1.append((i,k))
for i in list1:
    list2.append(tuple(sorted(i)))
list3=[]
for i in list2:
    if i not in list3:
        list3.append(i)
fields=["district1","district2"]
with open(" edge-graph.csv", 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for i in list3:
        csvwriter.writerow(i)      


# In[ ]:





# In[ ]:




