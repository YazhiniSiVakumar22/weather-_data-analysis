#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[33]:


data= pd.read_csv(r"C:\Users\lenovo\Downloads\weather dataset\weatherHistory.csv")
data.head()


# In[3]:


data.shape


# In[4]:


data.columns


# In[5]:


data.index


# In[34]:


data.dtypes


# In[35]:


data['Humidity'].unique()


# In[36]:


data.nunique()


# In[37]:


data.count()


# In[38]:


data['Summary'].value_counts()


# In[39]:


data.info()


# In[40]:


#find all the unique 'wind speed' values in thr data


# In[41]:


data.head(2)


# In[42]:


data.nunique()


# In[43]:


data['Wind Speed (km/h)'].nunique()


# In[44]:


data['Wind Speed (km/h)'].unique()


# In[45]:


#find all the unique 'Humidity' values in thr data


# In[46]:


data.Humidity.value_counts()


# In[47]:


# find the number of times when the wind speed was extactly  4km/h
data.head(2)
data[data['Wind Speed (km/h)']==4]


# In[49]:


#null values
data.isnull().sum()


# In[51]:


data.notnull().sum()


# In[54]:


# rename 
data.rename(columns={'Wind Speed (km/h)': 'windspeed'},inplace=True)


# In[55]:


data


# In[63]:


#varience of humidity
data['Humidity'].var()


# In[68]:


data.head(2)


# In[67]:


# findin all instances when 'windspeed is above 24' and visibility is 25

data[(data['windspeed']>24)& (data['Wind Bearing (degrees)']==25)]


# In[ ]:




