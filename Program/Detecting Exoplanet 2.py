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


hdul=astropy.io.fits.open(r'C:\Users\dell\Desktop\Exoplanets\01kepler.fits')


# In[5]:


hdul.info()
data=hdul[1].data
Data=astropy.table.Table(data)
Data


# In[6]:


hdul[2].data


# In[7]:


Flux=Data['SAP_FLUX']
Flux


# In[8]:


Flux[1]


# In[9]:


lstf=[]


# In[10]:


for i in Flux:
    lstf.append(i)
len(lstf)


# In[11]:


Time=Data['TIME']


# In[12]:


lstt=[]


# In[13]:


for i in Time:
    lstt.append(i)
len(lstt)


# In[15]:


plt.plot(lstt,lstf,label=['Time','Intensity'],marker='.')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Flux')


# In[ ]:




