#!/usr/bin/env python
# coding: utf-8

# In[3]:


import json
import csv
import pandas as pd
from datetime import date, timedelta


# In[4]:


dt={}
datelst=[]
def fun_list():
    
    sdt = date(2020, 3, 15)
    edt = date(2021, 8, 14)
    def cdate(date1, date2):
        for n in range(int ((date2 - date1).days)+1):
            yield date1 + timedelta(n)
    for i in cdate(sdt, edt):
        datelst.append(i.strftime("%Y-%m-%d"))

    for i in datelst:
        dt[i]=0
    return dt

dist=json.load(open("neighbor-districts-modified.json","r"))
dist1=[]

for key in dist:
    if('_' in key):
        count=0
        for i in range(len(key)):
            count+=1
            if(key[i]=='_'):
                break
        key=key[count:]
    dist1.append(key)

dist_csv=pd.read_csv("districts.csv")
district=dist_csv['District'].tolist()
dist_date=dist_csv['Date'].tolist()
confirmed=dist_csv['Confirmed'].tolist()

week=[]
c_dist=[]
cases=[]
fin_lst=[]


for i in dist1:
    ind=[j for j in range(len(district)) if district[j]==i]
    dt1=fun_list()
    for n in ind:
        m=dist_date[n]
        if m in dt1:
            dt1[m]=confirmed[n]
    wid=1
    w=0
    prev=0
    
    for x in dt1:
        lst=[]
        if (w==6):
            lst.append(i)
            lst.append(wid)
            wcases=dt1[x]-prev
            prev=dt1[x]
            lst.append(wcases)
            w=0
            wid+=1
        else:
            w+=1
        if (w==0):
            fin_lst.append(lst)


# In[5]:


with open('cases-week.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(['districtid', 'weekid', 'cases'])
    writer.writerows(fin_lst)
        


# In[6]:


week=[]
c_dist=[]
cases=[]
fin_lst=[]
date_list=[]
for i in range(len(datelst)):
    k=datelst[i]
    date_list.append(k[8:])

for i in dist1:
    ind=[j for j in range(len(district)) if district[j]==i]
    dt1=fun_list()
    for n in ind:
        if dist_date[n] in dt1:
            dt1[dist_date[n]]=confirmed[n] 

    prev=0
    mid=1
    y=-1
    for x in dt1:
        y+=1
        lst=[]
        if (int(date_list[y])==14):
            lst.append(i)
            lst.append(mid)
            mcases=dt1[x]-prev
            prev=dt1[x]
            lst.append(mcases)
            mid+=1
    
        if (int(date_list[y])==14):
            fin_lst.append(lst)
    


# In[7]:


with open('cases-month.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(['districtid', 'monthid', 'cases'])
    writer.writerows(fin_lst)


# In[8]:


week=[]
c_dist=[]
cases=[]
fin_lst=[]
z=date(2021,8,14)
z=z.strftime("%Y-%m-%d")

for i in dist1:
    ind=[j for j in range(len(district)) if district[j]==i]
    dt1=fun_list()
    for n in ind:
        m=dist_date[n]
        if m in dt1:
            dt1[m]=confirmed[n]
    for x in dt1:
        lst=[]
        if (x==z and dt1[x]!=0):
            lst.append(i)
            lst.append("overall")
            lst.append(dt1[x])
      
        if (x==z and dt1[x]!=0):
            fin_lst.append(lst)


# In[9]:


with open('cases-overall.csv', 'w', newline='') as fin_csv:
    writer = csv.writer(fin_csv)
    writer.writerow(['districtid', 'overall','cases'])
    writer.writerows(fin_lst)


# In[ ]:





# In[ ]:




