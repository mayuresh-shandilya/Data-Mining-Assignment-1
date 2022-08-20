#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import numpy as np
import pandas as pd
import collections


# In[3]:


dist=json.load(open("neighbor-districts.json","r"))


# In[4]:


keylst=[]
valslst=[]
for k in dist :
    i=k.index("/")
    key=k[0:i]
    if('_' in key):
        count=0
        for i in range(len(key)):
            if(key[i]=='_'):
                count+=1
        key=key.replace("_"," ",count)
    keylst.append(key)
valslst= list(dist.values())
newval=[]
for v in valslst:
    val2=[]
    for m in v:
        i=m.index("/")
        key=m[0:i]
        if('_' in key):
            count=0
            for i in range(len(key)):
                if(key[i]=='_'):
                    count+=1
            key=key.replace("_"," ",count)
        val2.append(key)
    newval.append(val2)
newdict = dict(zip(keylst,newval))


# In[7]:


comp=pd.read_csv("cowin_vaccine_data_districtwise.csv")
cmplst=comp['District'].tolist()
cmplst=cmplst[1:]
for i in range(len(cmplst)):
    cmplst[i]=cmplst[i].lower()
num=0
for i in range(len(keylst)): 
    count=0
    for j in range(len(cmplst)):
        if(keylst[i]==cmplst[j]):
            count+=1
    if(count==0):
        num+=1


# In[8]:


distcleaned=json.load(open("cleaned_file.json","r"))


# In[11]:


cmpcode=comp['District_Key'].tolist()
cmpcode=cmpcode[1:]
code=dict(zip(cmplst,cmpcode))
clst=[]
llst=[]
for i in distcleaned:
    for k,v in code.items():
        if(k.lower()==i.lower()):
            clst.append(v)
for i,j in distcleaned.items():
    lst2=[]
    for m in j:
        for k,v in code.items():
            if(k.lower()==m.lower()):
                lst2.append(v)
    llst.append(lst2)


# In[12]:


findict = dict(zip(clst,llst))
result = collections.OrderedDict(sorted(findict.items()))
with open("neighbor-districts-modified.json", "w") as outfile:
    json.dump(result, outfile)


# In[ ]:





# In[ ]:




