#!/usr/bin/env python
# coding: utf-8

# In[6]:


n=int(input("enter n"))
arr=[None]*n;
for i in range(n):
    val=int(input("enter the value"))print(sd)
    arr[i]=val
print(arr)


# In[7]:


sum=0
for i in range(n):
    sum+=arr[i]
mean=sum/n
print("mean is ",mean)


# In[ ]:





# In[10]:


if(n%2==0):
    print("median is ",(arr[n//2]+arr[(n//2)-1])/2)
else:
    print("median is ",arr[n//2])
    


# In[13]:


## min-max normalisation
min=arr[0]
max=arr[0]
for i in range(1,n):
    if(min>arr[i]):
        min=arr[i]
    if(max<arr[i]):
        max=arr[i]
##print(min)
##print(max)
for i in range(n):
    val=(arr[i]-min)/(max-min)
    print("normalisation value is ",val)

    


# In[17]:


## standardization
import math
sum=0
for i in range(n):
    sum+=(arr[i]-mean)**2
sd=math.sqrt(sum/n)
for i in range(n):
    val=(arr[i]-mean)/sd
    print("standardization is ",val)


# In[ ]:


mat[][]=[None][None]

