#!/usr/bin/env python
# coding: utf-8

# In[51]:


import csv
import pandas as pd
from datetime import date, timedelta
import numpy as np


# In[52]:


vacc=pd.read_csv("cowin_vaccine_data_districtwise.csv")
vacc=vacc[1:]
dist=vacc['District_Key'].tolist()
state=vacc['State_Code'].tolist()
state_name=vacc['State'].tolist()
state_dict={}
for i in range(len(state)):
    state_dict[state[i]]=state_name[i]  


# In[53]:


female={}
male={}
dratio={}
for i in range(len(dist)):
    vrow=vacc.iloc[i]
    if(type(vrow["14/08/2021.5"])==np.nan):
        male[dist[i]]=0
    else:
        if(type(vrow["14/08/2021.6"])==np.nan):
            female[dist[i]]=0
        else:
            male[dist[i]]=float(vrow["14/08/2021.5"])
            female[dist[i]]=float(vrow["14/08/2021.6"])
    if(male[dist[i]]!=0):
        dratio[dist[i]]=female[dist[i]]/male[dist[i]]
    else:
        dratio[dist[i]]=0


# In[54]:


sratio={}
for i in state_dict:
    fsum=0
    msum=0
    for j in male:
        if(i==j[:2]):
            fsum+=female[j]
            msum+=male[j]
    sratio[state_dict[i]]=fsum/msum


# In[55]:


fsum=0
msum=0
for i in male:
    fsum+=female[i]
    msum+=male[i]
vacc_overall=fsum/msum


# In[56]:


popl=pd.read_excel("DDW_PCA0000_2011_Indiastatedist.xlsx")


# In[57]:


level=popl["Level"].tolist()
lname=popl["Name"].tolist()
male_pop=popl["TOT_M"].tolist()
female_pop=popl["TOT_F"].tolist()
typ=popl["TRU"].tolist()


# In[58]:


distrpop={}
staterpop={}
for i in range(len(lname)):
    if(level[i]=="DISTRICT" and typ[i]=="Total"):
        distrpop[lname[i]]=female_pop[i]/male_pop[i]
for i in range(len(level)):
    if(level[i]=="STATE" and typ[i]=="Total"):
        staterpop[lname[i]]=female_pop[i]/male_pop[i]  
pop_overall=female_pop[0]/male_pop[0]


# In[59]:


fin_dist={}
for i in dratio:
    for j in distrpop:
        if(i[3:]==j):
            lst=[]
            lst.append(dratio[i])
            lst.append(distrpop[j])
            lst.append(dratio[i]/distrpop[j])
            fin_dist[i]=lst
fin_state={}
for i in sratio:
    for j in staterpop:
        if(i.lower()==j.lower()):
            lst=[]
            lst.append(sratio[i])
            lst.append(staterpop[j])
            lst.append(sratio[i]/staterpop[j])
            fin_state[i]=lst
fin_over=vacc_overall/pop_overall


# In[60]:


fin_dist1={}
fin_dist2=sorted(fin_dist.items(), key=lambda e: e[1][2])
fin_dist1=dict(fin_dist2)
    
fin_state1={}
fin_state2=sorted(fin_state.items(), key=lambda e: e[1][2])
fin_state1=dict(fin_state2)


# In[61]:


with open('district-vaccination-population-ratio.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["districtid", "vaccinationratio", "populationratio", "ratioofratios"])
    for i in fin_dist1:
        writer.writerow([i,fin_dist1[i][0],fin_dist1[i][1],fin_dist1[i][2]])


# In[62]:


with open('state-vaccination-population-ratio.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["stateid", "vaccinationratio", "populationratio", "ratioofratios"])
    for i in fin_state1:
        writer.writerow([i,fin_state1[i][0],fin_state1[i][1],fin_state1[i][2]])


# In[63]:


with open('overall-vaccination-population-ratio.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["overall", "vaccinationratio", "populationratio", "ratioofratios"])
    writer.writerow(["overall",vacc_overall,pop_overall,fin_over])


# In[ ]:




