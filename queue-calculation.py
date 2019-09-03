#This code is to calculate the queuing time for each process.
#The challenge is that I have to deal with the customer blocks, which could happen at any time of the whole processing for each order,could happen multiple times and could be overlapping.
#So my solution is first to tranfer all the time to a second difference from some time and second to create a dictionary; the key is the notification(unique key for each order), and make the value a list of customer block(each customer block is a 2-value list:start time and end time.).
#Use a loop to calcuate the queuing for each order. Then the problem becomes a math problem. For each process of each order, I am actually calculating the length of the uncovered range in a limited range which could be covered by several line segments.


from datetime import datetime
import numpy as np

ori=r'01/01/2018 00:00:00
ori=datetime.strptime(ori,'%m/%d/%Y %H:%M:%S')"

def compute(a,b):
    _min = 1e20
    _max = -1e20
    have = 0
    have_sum = 0
    for b_one in b:

        have += 1
        if b_one[1]<a[1] and b_one[0]>a[0]:
            _max = max(_max,b_one[1])
            _min = min(_min,b_one[0])
        elif a[0]<b_one[1]< a[1] and b_one[0]<a[0]:
            _max = max(_max,b_one[1])
            _min = a[0]
        elif b_one[1]>a[1] and a[1]>b_one[0]>a[0]:
            _max = a[1]
            _min = min(_min,b_one[0])
        else:
            have -= 1
            
        if have == 2:
            have = 0
            if b_per < b_one[0]:
                have_sum += b_one[0] - b_per
        b_per = b_one[1]
        
    if _min == 1e20 and _max == -1e20:
        return 0
    return _max-_min-have_sum

def timecal(a,b):
    ch=compute(a,b)
    #print('ch',ch)
    oritime=a[1]-a[0]
    #print('oritime',oritime)
    timing=oritime-ch
    #print('timing',timing)
    days=timing//86400
    hours=timing//3600-days*24
    minutes = (timing % 3600) // 60
    seconds = (timing % 3600) % 60
    time=str(days)+" days "+str(hours)+" hours "+str(minutes)+" minutes "+str(seconds)+" seconds"
    print(time)
    return(time)

def timecalSEC(a,b):
    ch=compute(a,b)
    #print('ch',ch)
    oritime=a[1]-a[0]
    #print('oritime',oritime)
    timing=oritime-ch
    print(timing)
    return(timing)
    
def time_listSEC(k,SCwithHold2,CSHoldCalDict):
    tl=[]
    count=0
    for item in SCwithHold4:
        st=item[k]
        ed=item[k+1]
        A=[st,ed]
        print(item)
        timelist=CSHoldCalDict[item[0]]
        aa=timecalSEC(A,timelist)
        tl.insert(count,aa)
        count+=1
   return tl
 
CSHold=pd.read_csv('D:\\\\Users\\\\T0230720\\\\Desktop\\\\Timing\\\\CSHold.csv',header=0,encoding='utf-8')\n",
SCwithoutHold=pd.read_csv('D:\\\\Users\\\\T0230720\\\\Desktop\\\\Timing\\\\SCwithoutHold.csv',header=0,encoding='utf-8')\n",
SCwithHold=pd.read_csv('D:\\\\Users\\\\T0230720\\\\Desktop\\\\Timing\\\\SCwithHold.csv',header=0,encoding='utf-8')"

SCwithHold.head()

Notification=CSHold.iloc[:,0]
CSHold1=CSHold.iloc[:,[1,2]]
SCwithHold1=SCwithHold.iloc[0:1366,[1,2,3,4,5,6,7]]
Notif=SCwithHold.iloc[0:1366,0]

Notif=Notif.astype(int)

def timetoint(df):
        df1=df.applymap(lambda x: datetime.strptime(x,'%m/%d/%Y %H:%M:%S')) 
        df2=df1.applymap(lambda x:(x-ori).total_seconds())
        df3=df2.applymap(lambda x:int(x))
        return df3
      
SCwithHold1.head()

CSHoldCal=timetoint(CSHold1)
SCHCal=timetoint(SCwithHold1)

CSHoldCal.head()
SCHCal.head()

Notification=pd.DataFrame(Notification)
print(len(CSHoldCal))
print(len(Notification))
type(CSHoldCal)

CSHoldCal1=pd.concat([Notification,CSHoldCal],axis=1)
SCwithHold2=pd.concat([Notif,SCHCal],axis=1)
CSHoldCal1.columns=['Notification','Start','End']
print(CSHoldCal1.head())
print(SCwithHold2.head())

CSHoldCal2=np.array(CSHoldCal1)
CSHoldCal2=CSHoldCal2.tolist()

CSHoldCalDict={}
for item in CSHoldCal2:
    if item[0] in CSHoldCalDict.keys():
        CSHoldCalDict[item[0]].append(item[1:])
    else:
        CSHoldCalDict[item[0]]=[item[1:]]
 
CSHoldCalDict

print(len(CSHoldCalDict))
print(len(SCwithHold2))

notif=time_listSEC(1,SCwithHold2,CSHoldCalDict)
CR=time_listSEC(2,SCwithHold2,CSHoldCalDict)
PL=time_listSEC(3,SCwithHold2,CSHoldCalDict)
FI=time_listSEC(4,SCwithHold2,CSHoldCalDict)
FC=time_listSEC(5,SCwithHold2,CSHoldCalDict)
CBL=time_listSEC(6,SCwithHold2,CSHoldCalDict)

Q={"notification":Notif,"NotifCre":notif2,"4-CR":CR,"5-PL":PL,"7-FI":FI,"9-FC":FC,"C-BL":CBL}
Queue=pd.DataFrame(Q)
Queue.to_cvs('D:\\Users\\T0230720\\Desktop\\Timing\\SAPqueue2019_06_14.csv',index=False)
