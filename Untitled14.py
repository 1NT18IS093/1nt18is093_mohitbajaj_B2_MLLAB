#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("enter the value of n"))


# In[3]:


arr=[None]*n
for i in range(n):
    val=int(input("enter the value"))
    arr[i]=val


# In[4]:


print(arr)


# In[8]:


for i in range(n):
    for j in range(i,n-1):
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp

print(arr)


# In[9]:


sum=0
for i in range(n):
    sum+=arr[i]
mean=sum/n
print(mean)


# In[11]:


if(n%2==0):
    print((arr[n//2]+arr[(n//2)-1])//2)
if(n%2!=0):
    print(arr[n//2])


# In[17]:



a=[1,2,3,4]
n=len(a)
if(n%2==0):
    print((a[n//2]+a[(n//2)-1])/2)
else:
    print(a[n//2])


# In[32]:


sum=0
for i in range(n):
    sum+=(arr[i]-mean)**2
sd=math.sqrt(sum/n)
print(sd)


# In[34]:


variance=sd**2


# In[35]:


print(variance)


# In[ ]:




