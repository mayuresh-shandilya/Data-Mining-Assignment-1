#!/usr/bin/env python
# coding: utf-8

# In[66]:


import csv
import pandas as pd
from datetime import date, timedelta
import numpy as np


# In[67]:


vacc=pd.read_csv("cowin_vaccine_data_districtwise.csv")
vacc=vacc[1:]
dist=vacc['District_Key'].tolist()
state=vacc['State_Code'].tolist()
state_name=vacc['State'].tolist()
state_dict={}
for i in range(len(state)):
    state_dict[state[i]]=state_name[i] 


# In[68]:


dose1={}
dose2={}
for i in range(len(dist)):
    vrow=vacc.iloc[i]
    if(type(vrow["14/08/2021.3"])==np.nan):
        dose1[dist[i]]=0
    else:
        if(type(vrow["14/08/2021.4"])==np.nan):
            dose2[dist[i]]=0
        else:
            dose1[dist[i]]=float(vrow["14/08/2021.3"])
            dose2[dist[i]]=float(vrow["14/08/2021.4"])


# In[69]:


stated1={}
stated2={}
for i in state_dict:
    d1=0
    d2=0
    for j in dose1:
        if(i==j[:2]):
            d1+=dose1[j]
            d2+=dose2[j]
    stated1[state_dict[i]]=d1
    stated2[state_dict[i]]=d2


# In[70]:


d1=0
d2=0
for i in dose1:
    d1+=dose1[i]
    d2+=dose2[i]
ovd1=d1
ovd2=d2


# In[71]:


popl=pd.read_excel("DDW_PCA0000_2011_Indiastatedist.xlsx")


# In[72]:


level=popl["Level"].tolist()
lname=popl["Name"].tolist()
tot_pop=popl["TOT_P"].tolist()
typ=popl["TRU"].tolist()


# In[73]:


distpop={}
statepop={}
for i in range(len(lname)):
    if(level[i]=="DISTRICT" and typ[i]=="Total"):
        distpop[lname[i]]=tot_pop[i]
for i in range(len(level)):
    if(level[i]=="STATE" and typ[i]=="Total"):
        statepop[lname[i]]=tot_pop[i] 
pop_overall=tot_pop[0]


# In[74]:


fin_dist={}
for i in dose1:
    for j in distpop:
        if(i[3:]==j):
            lst=[]
            lst.append(dose1[i]/distpop[j])
            lst.append(dose2[i]/distpop[j])
            fin_dist[i]=lst
fin_state={}
for i in stated1:
    for j in statepop:
        if(i.lower()==j.lower()):
            lst=[]
            lst.append(stated1[i]/statepop[j])
            lst.append(stated2[i]/statepop[j])
            fin_state[i]=lst
fin_overd1=ovd1/pop_overall
fin_overd2=ovd2/pop_overall


# In[75]:


fin_dist1={}
fin_dist2=sorted(fin_dist.items(), key=lambda e: e[1][0])
fin_dist1=dict(fin_dist2)
    
fin_state1={}
fin_state2=sorted(fin_state.items(), key=lambda e: e[1][0])
fin_state1=dict(fin_state2)


# In[76]:


with open('district-vaccinated-dose-ratio.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["districtid", "vaccinateddose1ratio", "vaccinateddose2ratio"])
    for i in fin_dist1:
        writer.writerow([i,fin_dist1[i][0],fin_dist1[i][1]])


# In[77]:


with open('state-vaccinated-dose-ratio.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["stateid", "vaccinateddose1ratio", "vaccinateddose2ratio"])
    for i in fin_state1:
        writer.writerow([i,fin_state1[i][0],fin_state1[i][1]])


# In[78]:


with open('overall-vaccinated-dose-ratio.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["overall", "vaccinateddose1ratio", "vaccinateddose2ratio"])
    writer.writerow(["overall",fin_overd1,fin_overd2])


# In[ ]:




