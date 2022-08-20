#!/usr/bin/env python
# coding: utf-8

# In[30]:


import json
import csv
import pandas as pd
from datetime import date, timedelta


# In[31]:


dt={}
datelst=[]
sdt = date(2020, 3, 15)
edt = date(2021, 8, 14)
def cdate(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)
for i in cdate(sdt, edt):
    datelst.append(i.strftime("%Y-%m-%d"))

def fun_list():
    for i in datelst:
        dt[i]=0
    return dt


# In[32]:


dist=json.load(open("neighbor-districts-modified.json","r"))
dist1=[]


# In[33]:


for key in dist:
    if('_' in key):
        count=0
        for i in range(len(key)):
            count+=1
            if(key[i]=='_'):
                break
        key=key[count:]
    dist1.append(key)
 


# In[34]:


dist_csv=pd.read_csv("districts.csv")
state=dist_csv['State'].tolist()
district=dist_csv['District'].tolist()
dist_date=dist_csv['Date'].tolist()
confirmed=dist_csv['Confirmed'].tolist()
recovered=dist_csv['Recovered'].tolist()
deceased=dist_csv['Deceased'].tolist()


# In[35]:


date_list=[]
for i in range(len(datelst)):
    k=datelst[i]
    date_list.append(k[8:])


# In[36]:


fin_lst=[]
for i in dist1:
    ind=[j for j in range(len(district)) if district[j]==i]
    act=fun_list()
    for n in ind:
        m=dist_date[n]
        if m in act:
            act[m]=confirmed[n]
    wid=1
    w=0
    wwave1=0
    wwave2=0
    wid1=0
    wid2=0
    mwave1=0
    mwave2=0
    mid1=0
    mid2=0
    mid=1
    y=-1
    pw1=0
    pw2=0
    pm1=0
    pm2=0
    
    for x in act:
        if(wid<91):
            if (w%7==6):
                wcases1=act[x]-pw1
                pw1=act[x]
                if(wwave1<wcases1):
                    wwave1=wcases1
                    wid1=wid
                wid+=1 
            if ((w-4)%7==6 and (w-4)>0):
                wcases2=act[x]-pw2
                pw2=act[x]
                if(wwave1<wcases2):
                    wwave1=wcases2
                    wid1=wid
                wid+=1
        if(wid>90):
            if (w%7==6):
                wcases1=act[x]-pw1
                pw1=act[x] 
                if(wwave2<wcases1):
                    wwave2=wcases1
                    wid2=wid
                wid+=1
            if ((w-4)%7==6 ):
                wcases2=act[x]-pw2
                pw2=act[x]
                if(wwave2<wcases2):
                    wwave2=wcases2
                    wid2=wid
                wid+=1 
        w+=1
        
        y+=1
        if (int(date_list[y])==14):
            
            mcases1=act[x]-pm1
            pm1=act[x]
            if(mwave1<mcases1):
                mwave1=mcases1
                if(mid<10):
                    mid1=mid
                if(mid>9):
                    mid2=mid
            mid+=1
    lst=[]
    if(wid1!=0 and wid2!=0):
        lst.append(i)
        lst.append(wid1)
        lst.append(wid2-1)
        lst.append(mid1)
        lst.append(mid2)
        fin_lst.append(lst)           


# In[37]:


with open('district-peaks.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(['districtid', 'wave1 - weekid','wave2 - weekid','wave1 - monthid','wave2 - monthid'])
    writer.writerows(fin_lst)


# In[38]:


active=[]
u_state=[]


# In[39]:


for k in range(len(confirmed)):
    active.append(confirmed[k]-recovered[k]-deceased[k])


# In[40]:


for k in state:
    if k not in u_state:
        u_state.append(k)

fin_lst=[]
date_list=[]
for i in range(len(datelst)):
    k=datelst[i]
    date_list.append(k[8:])
u_state.sort()


# In[41]:


mfin_lst=[]
for k in u_state:
    ind=[j for j in range(len(state)) if state[j]==k]
    act=fun_list()
    for n in ind:
        m=dist_date[n]
        if m in act:
            act[m]=act[m]+active[n]

    wid=1
    w=0
    wwave1=0
    wwave2=0
    wid1=0
    wid2=0
    mwave1=0
    mwave2=0
    mid1=0
    mid2=0
    mid=1
    y=-1

    for x in act:
        if(wid<91):
            if (w%7==6):
                if(wwave1<act[x]):
                    wwave1=act[x]
                    wid1=wid
                wid+=1 
            if ((w-4)%7==6):
                if(wwave1<act[x]):
                    wwave1=act[x]
                    wid1=wid
                wid+=1
        if(wid>90):
            if (w%7==6):
                if(wwave2<act[x]):
                    wwave2=act[x]
                    wid2=wid
                wid+=1
            if ((w-4)%7==6):
                if(wwave2<act[x]):
                    wwave2=act[x]
                    wid2=wid
                wid+=1 
        w+=1
        
        y+=1
        if (int(date_list[y])==14):
            if(mid<10):
                if(mwave1<act[x]):
                    mwave1=act[x]
                    mid1=mid
            if(mid>9):
                if(mwave2<act[x]):
                    mwave2=act[x]
                    mid2=mid
            mid+=1
            
    lst=[]
    if(wid1!=0 and wid2!=0):
        lst.append(k)
        lst.append(wid1)
        lst.append(wid2)
        lst.append(mid1)
        lst.append(mid2)
        mfin_lst.append(lst)


# In[42]:


with open('state-peaks.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(['stateid', 'wave1 - weekid','wave2 - weekid','wave1 - monthid','wave2 - monthid'])
    writer.writerows(mfin_lst)


# In[43]:


active=[]
u_state=[]


# In[44]:


for k in range(len(confirmed)):
    active.append(confirmed[k]-recovered[k]-deceased[k])


# In[45]:


for k in state:
    if k not in u_state:
        u_state.append(k)

fin_lst=[]
date_list=[]
for i in range(len(datelst)):
    k=datelst[i]
    date_list.append(k[8:])
u_state.sort()


# In[46]:


overall=fun_list()
ofin_lst=[]
for k in u_state:
    ind=[j for j in range(len(state)) if state[j]==k]
    act=fun_list()
    for n in ind:
        m=dist_date[n]
        if m in act:
            act[m]=act[m]+active[n]

    for i in datelst:
        overall[i]=overall[i]+act[i]
overall

wid=1
w=0
wwave1=0
wwave2=0
wid1=0
wid2=0
mwave1=0
mwave2=0
mid1=0
mid2=0
mid=1
y=-1

for x in overall:
    if(wid<91):
        if (w%7==6):
            if(wwave1<overall[x]):
                wwave1=overall[x]
                wid1=wid
            wid+=1 
        if ((w-4)%7==6):
            if(wwave1<overall[x]):
                wwave1=overall[x]
                wid1=wid
            wid+=1
    if(wid>90):
        if (w%7==6):
            if(wwave2<overall[x]):
                wwave2=overall[x]
                wid2=wid
            wid+=1
        if ((w-4)%7==6):
            if(wwave2<overall[x]):
                wwave2=overall[x]
                wid2=wid
            wid+=1 
    w+=1

    y+=1
    if (int(date_list[y])==14):
        if(mid<10):
            if(mwave1<overall[x]):
                mwave1=overall[x]
                mid1=mid
        if(mid>9):
            if(mwave2<overall[x]):
                mwave2=overall[x]
                mid2=mid
        mid+=1

lst=[]
if(wid1!=0 and wid2!=0):
    lst.append("overall")
    lst.append(wid1)
    lst.append(wid2)
    lst.append(mid1)
    lst.append(mid2)
    ofin_lst.append(lst)


# In[47]:


with open('overall-peaks.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(['overall', 'wave1 - weekid','wave2 - weekid','wave1 - monthid','wave2 - monthid'])
    writer.writerows(ofin_lst)


# In[ ]:




