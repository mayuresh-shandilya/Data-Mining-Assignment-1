#!/usr/bin/env python
# coding: utf-8

# In[12]:


import csv
import pandas as pd
from datetime import date, timedelta
import numpy as np
import datetime


# In[13]:


vacc=pd.read_csv("state-vaccinated-count-week.csv")

vstate=vacc['stateid'].tolist()
vweekid=vacc['weekid'].tolist()
vdose1=vacc['dose1'].tolist()
vose2=vacc['dose2'].tolist()


# In[14]:


rate={}
for i in range(len(vstate)):
    if(vweekid[i]==74):
        rate[vstate[i]]=vdose1[i]/7


# In[15]:


totvacc=pd.read_csv("state-vaccinated-count-overall.csv")
totstate=totvacc["stateid"].tolist()
totdose1=totvacc["dose1"].tolist()


# In[16]:


tvac={}
for i in range(len(totstate)):
    tvac[totstate[i]]=totdose1[i]


# In[17]:


popl=pd.read_excel("DDW_PCA0000_2011_Indiastatedist.xlsx")


# In[18]:


level=popl["Level"].tolist()
lname=popl["Name"].tolist()
tot_pop=popl["TOT_P"].tolist()
typ=popl["TRU"].tolist()


# In[19]:


tpop={}
for i in range(len(level)):
    if(level[i]=="STATE" and typ[i]=="Total"):
        tpop[lname[i]]=tot_pop[i]


# In[20]:


rpop={}
for i in tvac:
    for j in tpop:
        if(i.lower()==j.lower()):
            rpop[i]=tpop[j]-tvac[i]         


# In[21]:


fin_lst=[]
for m in rate:
    for n in rpop:
        if(m.lower()==n.lower()):
            lst=[]
            x=int(rpop[n]/rate[m])
            dt = datetime.date(2021, 8, 14)
            for i in range(x): 
                dt+= datetime.timedelta(days=1)
            lst.append(m)
            lst.append(rpop[n])
            lst.append(rate[m])
            lst.append(dt.strftime("%d-%m-%Y"))
            fin_lst.append(lst)   


# In[22]:


with open('complete-vaccination.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(['stateid', 'populationleft', 'rateofvaccination', 'date'])
    writer.writerows(fin_lst)


# In[ ]:




