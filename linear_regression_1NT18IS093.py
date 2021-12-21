#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv("/home/root1/Downloads/Food-Truck-LineReg (1).csv")


# In[2]:


df.head()


# In[12]:


df.columns=["X","Y"]
df.head()


# In[13]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[14]:


x,y=df["X"],df["Y"]
plt.scatter(x,y,alpha=0.6)
plt.title("scatter plot")
plt.xlabel("X->")
plt.ylabel("Y->")


# In[18]:


heatmap=sns.heatmap(df.corr(),annot=True)
df["Y"].corr(df["X"])





# In[19]:


Xsquare=[]
Ysquare=[]
XY=[]
for i in range(len(df)):
    Xsquare.append(round(df.X[i]**2,4))
    Ysquare.append(round(df.Y[i]**2,4))
    XY.append(round(df.Y[i]*df.X[i],4))
df["Xsquare"]=Xsquare
df["Ysquare"]=Ysquare
df["XY"]=XY
df.head()
    Xsquare.append(round(df.X[i]**2,4))


# In[27]:


sumxy=0
sumxs=0
sumys=0
sumy=0
sumx=0
xmean=0
ymean=0
for i in range(len(df)):
    sumxy=sumxy+df.XY[i]
    sumxs=sumxs+df.Xsquare[i]
    sumys=sumys+df.Ysquare[i]
    sumx=sumx+df.X[i]
    sumy=sumy+df.Y[i]
print(sumxy)
print(sumxs)
print(sumys)
r=sumxy/(sumxs*sumys)
print(r)
xmean=sumx/len(df)
ymean=sumy/len(df)


# In[30]:


import math

sdx=0
sdy=0
sum=0
for i in range(len(df)):
    valx=df.X[i]
    valy=df.Y[i]
    sdx=sdx+((valx-xmean)*(valx-xmean))
    sdy=sdy+((valy-ymean)*(valy-ymean))
sdx=sdx/len(df)
sdy=sdy/len(df)
sdx=math.sqrt(sdx)
sdy=math.sqrt(sdy)
print(sdx)
print(sdy)

    
    


# In[31]:


m=r*sdy/sdx
print(m)


# In[32]:


c=ymean-(m*xmean)
print(c)


# In[ ]:




