#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import self_cashier


# In[3]:


from self_cashier import Transaction


# In[4]:


test_1 = Transaction()


# In[5]:


test_1.add_item("Ayam Goreng", 2, 20_000)


# In[9]:


test_1.add_item("Pasta Gigi", 3, 15_000)


# In[10]:


test_1.check_order()


# In[11]:


test_1.delete_item("Pasta Gigi")


# In[12]:


test_1.check_order()


# In[13]:


test_1.reset_transaction()


# In[14]:


test_1.add_item("Mainan Mobil", 2, 200_000)


# In[15]:


test_1.add_item("Mie Instan", 5, 3_000)


# In[16]:


test_1.add_item("Ayam Goreng", 2, 20_000)


# In[21]:


test_1.add_item("Pasta Gigi", 3, 15_000)


# In[22]:


test_1.check_order()


# In[23]:


test_1.total_price()


# In[ ]:




