#!/usr/bin/env python
# coding: utf-8

#This code is to check the columns "part number" in two lists according to the columns "Link" to see if the file "Avionics_CMM" have all the part-numbers for each Link.

# In[1]:

import numpy as np
import pandas as pd

# In[2]:

CMM=pd.read_csv('D:\\Users\\T0230720\\Desktop\\Sarah\\Avionics_CMM.csv',header=0)
Capo=pd.read_csv('D:\\Users\\T0230720\\Desktop\\Sarah\\Capo_List.csv',header=0)

# In[3]:

print(CMM.head())
print(Capo.head())

# In[4]:

link=list(CMM['Link'])
kk=list(range(len(CMM['Link'])))
checklist=[None]*len(CMM['Link'])
check={'kk':kk,'Link':link,'checklist':checklist}
checkk=pd.DataFrame(check)
check

# In[5]:

link1=list(Capo['Maintenance_Data_Reference'])
pn1=list(Capo['Part_Number'])
check1={'link1':link1,'pn':pn1}
check1=pd.DataFrame(check1)
check1

# In[6]:

checl1dict=np.array(check1)
checl1dict=checl1dict.tolist()
checl1dict

# In[7]:

checkdict={}
for item in checl1dict:
    if item[0] in checkdict.keys():
        checkdict[item[0]].append(item[1:])
    else:
        checkdict[item[0]]=[item[1:]]

# In[8]:

checkdict

# In[9]:

#for i in range(len(CMM['Link'])):
for j in checkdict:
    for i in range(len(CMM['Link'])):
        if j==check["Link"][i]:
            check["checklist"][i]=checkdict[j]

# In[10]:

check

# In[52]:

checklist=pd.DataFrame(check)
checklist

# In[53]:

cc=pd.merge(CMM,checklist)

# In[55]:

cc.to_csv('D:\\Users\\T0230720\\Desktop\\cc.csv',index=False)
