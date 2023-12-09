#!/usr/bin/env python
# coding: utf-8

# In[42]:


# Importer les librairies

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split


from sklearn.linear_model import LinearRegression


# In[22]:


# import Data Set

Data = pd.read_csv('D:\LoyersMaisons.csv' , delimiter = ';')
Data


# In[23]:


plt.scatter (Data['surface'],Data['loyer'],color='red')


# In[30]:


Data = Data[Data['loyer']<=10000]
Data


# In[31]:


plt.scatter (Data['surface'],Data['loyer'],color='red')


# In[32]:


x=Data.iloc[ : , :-1 ].values
y=Data.iloc[ : , -1].values


# In[33]:


y


# In[38]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)


# In[39]:


len(x)


# In[40]:


len(x_train)


# In[41]:


len(x_test)


# In[43]:


#Construction du model

regressor= LinearRegression()
regressor.fit(x_train,y_train)


# In[44]:


y_pred = regressor.predict(x_test)


# In[45]:


y_pred


# In[46]:


regressor.predict([[44]])


# In[49]:


regressor.predict([[70]])


# In[52]:


plt.scatter(x_test,y_test,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title('Evolution des loyers par surface')


# In[ ]:




