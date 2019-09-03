#!/usr/bin/env python
# coding: utf-8

#This code is to extract infomation from test report of test Bench.

import os
import re
import pandas as pd
import datetime

d1=os.listdir('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\Final')
d2=os.listdir('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\Pre')
d3=os.listdir('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\X')

############################Find the row of UUT NAME###################################################
def nm(list):
    count=0
    for i in list:
        count+=1
        ii='UUT NAME' in i
        if ii==True:
            cc=count
    return cc-1


###########################Find the row of UUT PART NUMBER###########################################
def pn(list):
    count=0
    for i in list:
        count+=1
        ii='UUT PART-NUMBER' in i
        if ii==True:
            cc=count
    return cc-1

#########################Find the row of UUT SERIAL NUMBER##########################################
def sn(list):
    count=0
    for i in list:
        count+=1
        ii='UUT SERIAL-NUMBER' in i
        if ii==True:
            cc=count
    return cc-1

########################Find the row of TESTBENCH SERIAL NUMBER####################################
def tsn(list):
    count=0
    for i in list:
        count+=1
        ii='TESTBENCH SERIAL_NUMBER' in i
        if ii==True:
            cc=count
    return cc-1

######################Find the row of DATE##########################################################
def dt(list):
    count=0
    for i in list:
        count+=1
        ii='DATE:' in i
        if ii==True:
            cc=count
    return cc-1

######################Find the row of TIME##########################################################
def time(list):
    count=0
    for i in list:
        count+=1
        ii='TIME:                         ' in i
        if ii==True:
            cc=count
    return cc-1

#####################Find the row of EXECUTION TIME################################################
def ET(list):
    count=0
    for i in list:
        count+=1
        ii='EXECUTION TIME:' in i
        if ii==True:
            cc=count
    return cc-1

#####################Find the row of TEST RESULT################################################
def tr(list):
    count=0
    for i in list:
        count+=1
        ii='TEST RESULT:  ' in i
        if ii==True:
            cc=count
    return cc-1

month={' janvier ':'/01/',' février ':'/02/',' mars ':'/03/',' avril ':'/04/',' mai ':'/05/',' juin ':'/06/',' juillet ':'/07/',' août ':'/08/',' septembre ':'/09/',' octobre ':'/10/',' novembre ':'/11/',' décembre ':'/12/'}
month
def m(t1,month):
    mon=re.findall('[ ]+\w+[ ]',t1)
    for i in month:
        if mon[0]==i:
            mon1=month[i]
    t1=t1.replace(mon[0],mon1)
    return t1

ww={}
ww['UUT_NAME']=[]
ww['UUT_PART_NUMBER']=[]
ww['UUT_SERIAL_NUMBER']=[]
ww['TESTBENCH_SERIAL_NUMBER']=[]
ww['DATE']=[]
ww['TIME']=[]
ww['EXECUTION_TIME']=[]
ww['TEST_RESULT']=[]
ww['TEST']=[]


for name in d1 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\Final\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        nmm=nm(lines)
        name=re.search('(  )\w+',lines[nmm]).group(0)
        ww['UUT_NAME'].append(name)
        tmm=time(lines)
        tm=re.search('\d+:\d+:\d+',lines[tmm]).group(0)
        ww['TIME'].append(tm)

for name in d1 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\Final\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        tsnn=tsn(lines)
        tsn1=re.search('(\w+)?\d+(\w+)?',lines[tsnn]).group(0)
        ww['TESTBENCH_SERIAL_NUMBER'].append(tsn1)

for name in d1 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\Final\\' + name,encoding='cp1252',errors ='replace')
        ww['TEST'].append("FIN")

for name in d1 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\Final\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        pnn=pn(lines)
        pn1=re.search('(\w+)?\d+\w+',lines[pnn]).group(0)
        ww['UUT_PART_NUMBER'].append(pn1)
        snn=sn(lines)
        sn1=re.search('\w+?\d+\w+',lines[snn]).group(0)
        ww['UUT_SERIAL_NUMBER'].append(sn1)

for name in d1 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\Final\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        dtt=dt(lines)
        dt1=re.search('\d+( )(\w+)( )\d+',lines[dtt]).group(0)
        dtt1=m(dt1,month)
        ww['DATE'].append(dtt1)

for name in d1 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\Final\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        tr1=tr(lines)
        ww['TEST_RESULT'].append(lines[tr1])

for name in d1 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\Final\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        ett=ET(lines)
        et=re.findall('\d+',lines[ett])
        if len(et)==1:
            et1=et[0]
        else:
            et1=0
        ww['EXECUTION_TIME'].append(et1)


for name in d2 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\Pre\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        nmm=nm(lines)
        name=re.search('(  )\w+',lines[nmm]).group(0)
        ww['UUT_NAME'].append(name)
        tmm=time(lines)
        tm=re.search('\d+:\d+:\d+',lines[tmm]).group(0)
        ww['TIME'].append(tm)


for name in d2 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\Pre\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        tsnn=tsn(lines)
        tsn1=re.search('(\w+)?\d+(\w+)?',lines[tsnn]).group(0)
        ww['TESTBENCH_SERIAL_NUMBER'].append(tsn1)


for name in d2 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\Pre\\' + name,encoding='cp1252',errors ='replace')
        ww['TEST'].append("PRE")


for name in d2 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\Pre\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        pnn=pn(lines)
        pn1=re.search('(\w+)?\d+\w+',lines[pnn]).group(0)
        ww['UUT_PART_NUMBER'].append(pn1)
        snn=sn(lines)
        sn1=re.search('\w+?\d+\w+',lines[snn]).group(0)
        ww['UUT_SERIAL_NUMBER'].append(sn1)


for name in d2 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\Pre\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        dtt=dt(lines)
        dt1=re.search('\d+( )(\w+)( )\d+',lines[dtt]).group(0)
        dtt1=m(dt1,month)
        ww['DATE'].append(dtt1)


for name in d2 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\Pre\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        tr1=tr(lines)
        ww['TEST_RESULT'].append(lines[tr1])


for name in d2 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\Pre\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        ett=ET(lines)
        et=re.findall('\d+',lines[ett])
        if len(et)==1:
            et1=et[0]
        else:
            et1=0
        ww['EXECUTION_TIME'].append(et1)


for name in d3 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\X\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        nmm=nm(lines)
        name=re.search('(  )\w+',lines[nmm]).group(0)
        ww['UUT_NAME'].append(name)
        tmm=time(lines)
        tm=re.search('\d+:\d+:\d+',lines[tmm]).group(0)
        ww['TIME'].append(tm)


for name in d3 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\X\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        tsnn=tsn(lines)
        tsn1=re.search('(\w+)?\d+(\w+)?',lines[tsnn]).group(0)
        ww['TESTBENCH_SERIAL_NUMBER'].append(tsn1)

for name in d3 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\X\\' + name,encoding='cp1252',errors ='replace')
        ww['TEST'].append("X")


for name in d3 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\X\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        pnn=pn(lines)
        pn1=re.search('(\w+)?\d+\w+',lines[pnn]).group(0)
        ww['UUT_PART_NUMBER'].append(pn1)
        snn=sn(lines)
        sn1=re.search('\w+?\d+\w+',lines[snn]).group(0)
        ww['UUT_SERIAL_NUMBER'].append(sn1)


for name in d3 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\X\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        dtt=dt(lines)
        dt1=re.search('\d+( )(\w+)( )\d+',lines[dtt]).group(0)
        dtt1=m(dt1,month)
        ww['DATE'].append(dtt1)


for name in d3 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\X\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        tr1=tr(lines)
        ww['TEST_RESULT'].append(lines[tr1])


for name in d3 : 
        f=open('D:\\Users\\T0230720\\Desktop\\stevstuff\\E\\X\\' + name,encoding='cp1252',errors ='replace')
        lines=f.readlines()
        ett=ET(lines)
        et=re.findall('\d+',lines[ett])
        if len(et)==1:
            et1=et[0]
        else:
            et1=0
        ww['EXECUTION_TIME'].append(et1)


DATE=list(ww['DATE'])
EXECUTION_TIME=list(ww['EXECUTION_TIME'])
TESTBENCH_SERIAL_NUMBER=list(ww['TESTBENCH_SERIAL_NUMBER'])
TEST_RESULT=list(ww['TEST_RESULT'])
TIME=list(ww['TIME'])
UUT_NAME=list(ww['UUT_NAME'])
UUT_PART_NUMBER=list(ww['UUT_PART_NUMBER'])
UUT_SERIAL_NUMBER=list(ww['UUT_SERIAL_NUMBER'])
TEST=list(ww['TEST'])
print(len(DATE))
print(len(EXECUTION_TIME))
print(len(TESTBENCH_SERIAL_NUMBER))
print(len(TEST_RESULT))
print(len(TIME))
print(len(UUT_NAME))
print(len(UUT_PART_NUMBER))
print(len(UUT_SERIAL_NUMBER))
print(len(TEST))

e_rmd={'UUT_NAME':UUT_NAME,'UUT_PART_NUMBER':UUT_PART_NUMBER,"UUT_SERIAL_NUMBER":UUT_SERIAL_NUMBER,'TESTBENCH_SERIAL_NUMBER':TESTBENCH_SERIAL_NUMBER,'DATE':DATE,"TIME":TIME,"EXECUTION_TIME":EXECUTION_TIME,"TEST_RESULT":TEST_RESULT,"TEST":TEST}
e_rmd1=pd.DataFrame(e_rmd)
e_rmd1


e_rmd1['DateTime']=e_rmd1['DATE']+' '+e_rmd1['TIME']
e_rmd1


e_rmd1.to_csv('D:\\Users\\T0230720\\Desktop\\stevstuff\\E-RMD.csv',index=False)


#!/usr/bin/env python
# coding: utf-8

