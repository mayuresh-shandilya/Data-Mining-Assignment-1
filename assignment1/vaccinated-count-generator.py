#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv
import pandas as pd
from datetime import date, timedelta
import numpy as np


# In[5]:


vacc=pd.read_csv("cowin_vaccine_data_districtwise.csv")
vacc=vacc[1:]
cols=vacc.columns
dist=vacc['District_Key'].tolist()
state=vacc['State'].tolist()
state_code=vacc['State_Code'].tolist()
state_dict={}
for i in range(len(state)):
    state_dict[state[i]]=state_code[i] 


# In[6]:


dt={}
datelst=[]
vdate=[]
sdt = date(2020, 3, 15)
sdt1= date(2021, 1, 16)
edt = date(2021, 8, 14)
def cdate(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)
for i in cdate(sdt, edt):
    datelst.append(i.strftime("%d/%m/%Y"))
for i in cdate(sdt1, edt):
    vdate.append(i.strftime("%d/%m/%Y"))
def fun_list():
    for i in datelst:
        dt[i]=[0,0]
    return dt


# In[7]:


date_list=[]
for i in range(len(datelst)):
    k=datelst[i]
    date_list.append(k[:2])


# In[8]:


week_lst=[]
month_lst=[]
overall_lst=[]

for i in range(len(dist)):
    vd=fun_list()
    vrow=vacc.iloc[i]
    for j in vdate:
        dlist=[]
        dose1=j+".3"
        dose2=j+".4"
        if(type(vrow[dose1])==np.nan):
            dlist.append(0)
        else:
            dlist.append(float(vrow[dose1]))
        if(type(vrow[dose2])==np.nan):
            dlist.append(0)
        else:
            dlist.append(float(vrow[dose2]))
        vd[j]=dlist
        
    wid=1
    w=0
    prev1=0
    prev2=0
        
    for x in vd:
        lst=[]
        if (w==6):
            lst.append(dist[i])
            lst.append(wid)
            f1=vd[x][0]-prev1
            prev1=vd[x][0]
            f2=vd[x][1]-prev2
            prev2=vd[x][1]
            lst.append(abs(f1))
            lst.append(abs(f2))
            w=0
            wid+=1
        else:
            w+=1
        if (w==0):
            week_lst.append(lst)    
            
    prev1=0
    prev2=0
    mid=1
    y=-1
    for x in vd:
        y+=1
        lst=[]
        if (int(date_list[y])==14):
            lst.append(dist[i])
            lst.append(mid)
            f1=vd[x][0]-prev1
            prev1=vd[x][0]
            f2=vd[x][1]-prev2
            prev2=vd[x][1]
            lst.append(abs(f1))
            lst.append(abs(f2))
            mid+=1
    
        if (int(date_list[y])==14):
            month_lst.append(lst)        
            
    z=date(2021,8,14)
    z=z.strftime("%d/%m/%Y")
    
    for x in vd:
        lst=[]
        if (x==z):
            lst.append(dist[i])
            lst.append(vd[x][0])
            lst.append(vd[x][1])
      
        if (x==z):
            overall_lst.append(lst)
week_lst.sort()
month_lst.sort()
overall_lst.sort()


# In[9]:


with open('district-vaccinated-count-week.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(['districtid', 'weekid', 'dose1', 'dose2'])
    writer.writerows(week_lst)


# In[10]:


with open('district-vaccinated-count-month.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(['districtid', 'monthid', 'dose1', 'dose2'])
    writer.writerows(month_lst)


# In[11]:


with open('district-vaccinated-count-overall.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(['districtid', 'dose1', 'dose2'])
    writer.writerows(overall_lst)


# In[12]:


sweek=[]
smon=[]
soverall=[]

for i in state_dict:  
    for j in range(74):
        lst=[]
        d1=0
        d2=0
        for k in week_lst:
            if(state_dict[i]==k[0][0:2] and k[1]==j+1):
                d1+=k[2]
                d2+=k[3]
        lst.append(i)
        lst.append(j+1)
        lst.append(d1)
        lst.append(d2)
        sweek.append(lst)
    for j in range(17):
        lst=[]
        d1=0
        d2=0
        for k in month_lst:
            if(state_dict[i]==k[0][0:2] and k[1]==j+1):
                d1+=k[2]
                d2+=k[3]
        lst.append(i)
        lst.append(j+1)
        lst.append(d1)
        lst.append(d2)
        smon.append(lst)
    llist=[]
    x1=0
    x2=0
    for k in overall_lst:
        if(state_dict[i]==k[0][0:2]):
            x1+=k[1]
            x2+=k[2]
    llist.append(i)
    llist.append(x1)
    llist.append(x2)
    soverall.append(llist)


# In[13]:


with open('state-vaccinated-count-week.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(['stateid', 'weekid', 'dose1', 'dose2'])
    writer.writerows(sweek)


# In[14]:


with open('state-vaccinated-count-month.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(['stateid', 'monthid', 'dose1', 'dose2'])
    writer.writerows(smon)


# In[15]:


with open('state-vaccinated-count-overall.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(['stateid', 'dose1', 'dose2'])
    writer.writerows(soverall)


# In[ ]:




