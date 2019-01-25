
# coding: utf-8

# In[1]:


import os


# In[2]:


print(os.listdir())


# In[3]:


#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


#import dataset
data = pd.read_csv('housingData-Real.csv')


# In[5]:


data.head()


# In[6]:


data.info()


# In[7]:


# select your columns
livingspace = data['sqft_living']
price = data['price']


# In[10]:


#convert livingspace into 2D matrix
#X usually is in CAPS
x = np.array(livingspace).reshape(-1, 1)


# In[12]:


#convert price into 2D matrix
y = np.array(price)


# In[13]:


y


# In[14]:


# convert the data into test and training
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/3)


# In[15]:


x_test


# In[16]:


#pass your data into linear Regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)


# In[17]:


#create a predictor
predictor = regressor.predict(x_test)


# In[18]:


predictor


# In[19]:


#this prediction is more helpful with graphs/plots


# In[23]:


#plot for training dataset
plt.scatter(x_train, y_train)
plt.plot(x_train, regressor.predict(x_train), color='red')
plt.title('Training graph for Housing')
plt.xlabel('Space')
plt.ylabel('Price')


# In[24]:


#plot for test dataset
plt.scatter(x_test, y_test)
plt.plot(x_train, regressor.predict(x_train), color='red')
plt.title('Training graph for Housing')
plt.xlabel('Space')
plt.ylabel('Price')

