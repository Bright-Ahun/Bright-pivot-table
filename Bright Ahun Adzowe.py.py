#!/usr/bin/env python
# coding: utf-8

# # Assignment on Pandas Pivot and Pivot Tables

# In[4]:


#importing pandas and numpy


# In[5]:


import numpy as np


# In[6]:


import pandas as pd


# # 1. Downloading the autos data set.

# In[3]:


df = pd.read_csv('autos.csv')
df


# # 2. Printing out the first 8 entries.

# In[7]:


df.head(8)


# # 3. Returning a data frame containing the minimum price of each car; 

# In[8]:


gpd_a = df.groupby('make')
min_price = gpd_a['price'].min()
min_price


# # 4. The smallest standard deviation of the prices

# In[9]:


std_dev = np.std(df).min()
std_dev


# # 5. Returning the last 2 rows of each group of "car make" and "fuel_type"

# In[10]:


col = ['make','fuel_type']
print(df[col].tail(2))


# #  6. Replicating the Split-apply-combine without GroupBy;

# In[22]:


for make in df['make'].unique():
    


# # 7. Creating 2 separate dictionaries and joining them as a new dataset;

# In[12]:


dict_1 = {'make':['Alfa', 'benz', 'audi', 'saab'],'price':[25580, 56444, 36215, 12548]}
dict_2 = {'make':['volvo', 'Toyota', 'vitz', 'nissan'], 'price':[38792, 478915, 897452, 59864]}
df_1 = pd.DataFrame(dict_1)
df_2 = pd.DataFrame(dict_2)
merge_df = pd.concat([df_1, df_2],ignore_index=True)
merge_df


# In[ ]:





# In[23]:


result_df = pd.DataFrame.from_dict(results, orient='index', columns=['sum'])


# In[ ]:




