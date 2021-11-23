#!/usr/bin/env python
# coding: utf-8

# In[6]:


import math
redx=6.2
redy=3.2
bluex=6.5
bluey=3.0
greenx=6.6
greeny=3.7
redxc=0
redyc=0
countred=0
greenxc=0
greenyc=0
countgreen=0
bluexc=0
blueyc=0
countblue=0

for i in range(10):
    
    x=float(input("x co-ordinate of datapoint"))
    y=float(input("y co-ordinate of datapoint"))
    red=math.sqrt(((redx-x)*(redx-x))+((redy-y)*(redy-y)))
    green=math.sqrt(((greenx-x)*(greenx-x))+((greeny-y)*(greeny-y)))
    blue=math.sqrt((( bluex-x)*( bluex-x))+(( bluey-y)*( bluey-y)))
    if(red<=green and red<=blue):
        print("this datapoint belongs to red cluster")
        redxc=redxc+x
        redyc=redyc+y
        countred=countred+1
    elif(green<=red and green<=blue):
        print("this datapoint belongs to green cluster")
        greenxc=greenxc+x
        greenyc=greenyc+y
        countgreen=countgreen+1
    else:
        print("this datapoint belongs to blue cluster")
        bluexc=bluexc+x
        blueyc=blueyc+y
        countblue=countblue+1

        
    


# ## 

# In[8]:


print("new red centroid is (",redxc/countred,",",redyc/countred,")")
print("new green centroid is (",greenxc/countgreen,",",greenyc/countgreen,")")
print("new blue centroid is (",bluexc/countblue,",",blueyc/countblue,")")


# In[ ]:




