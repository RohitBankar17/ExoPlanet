#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


import astropy 


# In[3]:


from astropy.io import fits


# In[4]:


hdul=astropy.io.fits.open(r'C:\Users\dell\Desktop\Exoplanets\0kepler.fits')


# In[5]:


hdul.info()


# In[6]:


data=hdul[1].data


# In[7]:


Data=astropy.table.Table(data)
Data


# In[8]:


hdul[2].data


# In[9]:


Flux=Data['FLUX']


# In[10]:


Flux


# In[11]:


Flux[1]


# In[12]:


lstf=[]


# In[13]:


Flux[4756]


# In[14]:


for i in range(0,len(Flux)):
    lstf.append(Flux[i][3][4]+Flux[i][4][4])


# In[15]:


Time=Data['TIME']


# In[16]:


lstt=[]


# In[17]:


for i in Time:
    lstt.append(i)


# In[18]:


len(lstt)


# In[19]:


len(lstf)


# In[20]:


type(lstt)


# In[21]:


plt.plot(lstt,lstf,label=['Time','Intensity'],marker='.')
plt.legend()


# In[ ]:




