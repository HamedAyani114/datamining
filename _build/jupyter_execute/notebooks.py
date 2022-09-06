#!/usr/bin/env python
# coding: utf-8

# # **Latihan Tugas 1**
# 
# *   Cari *dataset* dari Url
# *   Tentukan *Dissimilarity between binary variable*
# *   Ukur Jarak d(1,2)
# *   Ukur Jarak d(1,3)
# *   Ukur Jarak d(1,4)
# 

# In[1]:


import pandas as pd
import math


# ## *Dataset*

# In[2]:


dataset="https://raw.githubusercontent.com/HamedAyani114/datamining/main/dataset/audi.csv"
getData = pd.read_csv(dataset)


# In[3]:


getData


# In[4]:


getData.columns


# ## Disimilarity
# 
# 
# *   Take all values of 'Transmission' and 'fuelType'
# *   If values is AUTO and Petrol change to 1
# *   If values is MANUAL and *Diesel* change to 0
# 
# 

# In[5]:


getData[["model","year", "transmission", "fuelType"]].head(6)


# In[6]:


# transmission code
code_transm_for_manual = "Manual"
code_transm_for_auto = "Automatic"

code_fuelType_for_Petrol = "Petrol"
code_fuelType_for_Diesel = "Diesel"

# binary value
value_of_one = 1
value_of_zero = 0

def change_code_transmission_to_biner(transmission):
    return value_of_one if transmission == code_transm_for_auto else value_of_zero

def change_code_fuelType_to_biner(fuelType):
    return value_of_one if fuelType == code_fuelType_for_Petrol else value_of_zero


# In[7]:


# Update/changes value from transmission
getData["transmission"] = getData["transmission"].apply(change_code_transmission_to_biner)


# In[8]:


# Update/changes value from fuelType
getData["fuelType"] = getData["fuelType"].apply(change_code_fuelType_to_biner)


# In[9]:


getData[["model","year", "transmission", "fuelType",]].head(8)


# In[10]:


def dissimilarity_biner(i,j):
  p = 2
  m = 0
  for col in ['transmission', 'fuelType']:
    if getData[col][i] == getData[col][j]:
      m+=1
  return (p-m)/p


# In[11]:


print(dissimilarity_biner(1,2))
print(dissimilarity_biner(1,3))
print(dissimilarity_biner(4,6))
print(dissimilarity_biner(1,7))
print(dissimilarity_biner(7,2))
print(dissimilarity_biner(0,2))


# ## Distance

# In[12]:


def distance(i,j,h):
  result = 0
  for col in ["price", "mileage", "tax"]:
    result = math.pow(abs(getData[col][i] - getData[col][j]), h)
  return result**(1/h)


# In[13]:


getData[["model","year", "price", "mileage", "tax"]].head(8)


# In[14]:


print(distance(1,2,1))
print(distance(1,3,1))
print(distance(1,4,1))


# In[15]:


print(distance(1,2,3))
print(distance(1,3,3))
print(distance(1,4,3))

