#!/usr/bin/env python
# coding: utf-8

# In[3]:


#WEEK 7 - Python Workbook Assignment 4-2
import pandas as pd
df = pd.read_csv(r"C:\MUNJA_DATA\Courses\Data Visualization\Week-7\learn-data-analysis-w-python-master\datasets\gradedata.csv")
df.head()


# In[4]:


import numpy as np
df['timemgmt']=np.where((df['exercise']>3)&(df['hours']>17),'busy','idle')


# In[5]:


df.tail()


# In[ ]:




