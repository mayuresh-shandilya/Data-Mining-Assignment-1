#!/usr/bin/env python
# coding: utf-8

# In[21]:


import csv
import pandas as pd
from datetime import date, timedelta
import numpy as np


# In[22]:


vacc=pd.read_csv("cowin_vaccine_data_districtwise.csv")
vacc=vacc[1:]
dist=vacc['District_Key'].tolist()
state=vacc['State_Code'].tolist()
state_name=vacc['State'].tolist()
state_dict={}
for i in range(len(state)):
    state_dict[state[i]]=state_name[i] 


# In[23]:


covishield={}
covaxin={}
dratio={}
for i in range(len(dist)):
    vrow=vacc.iloc[i]
    if(type(vrow["14/08/2021.8"])==np.nan):
        covaxin[dist[i]]=0
    else:
        if(type(vrow["14/08/2021.9"])==np.nan):
            covishield[dist[i]]=0
        else:
            covaxin[dist[i]]=float(vrow["14/08/2021.8"])
            covishield[dist[i]]=float(vrow["14/08/2021.9"])
    if(covaxin[dist[i]]!=0):
        dratio[dist[i]]=covishield[dist[i]]/covaxin[dist[i]]
    else:
        dratio[dist[i]]=0


# In[24]:


sratio={}
for i in state_dict:
    cox=0
    cov=0
    for j in covaxin:
        if(i==j[:2]):
            cov+=covishield[j]
            cox+=covaxin[j]
    if(cox!=0):
        sratio[state_dict[i]]=cov/cox
    else:
        sratio[state_dict[i]]=0


# In[25]:


fin_dist1={}
fin_dist2=sorted(dratio.items(), key=lambda e: e[1])
fin_dist1=dict(fin_dist2)

fin_state1={}
fin_state2=sorted(sratio.items(), key=lambda e: e[1])
fin_state1=dict(fin_state2)


# In[26]:


cox=0
cov=0
for i in covaxin:
    cov+=covishield[i]
    cox+=covaxin[i]
vacc_overall=cov/cox


# In[27]:


with open('district-vaccine-type-ratio.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["districtid", "vaccineratio"])
    for i in fin_dist1:
        writer.writerow([i,fin_dist1[i]])


# In[28]:


with open('state-vaccine-type-ratio.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["stateid", "vaccineratio"])
    for i in fin_state1:
        writer.writerow([i,fin_state1[i]])


# In[29]:


with open('overall-vaccine-type-ratio.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(["overall", "vaccineratio"])
    writer.writerow(["overall",vacc_overall])


# In[ ]:




