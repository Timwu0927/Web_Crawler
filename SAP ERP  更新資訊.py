#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from bs4 import BeautifulSoup
import time


# In[2]:


browser = webdriver.Chrome()


# In[3]:


browser.get("https://www.sap.com/taiwan/products/s4hana-erp/technical-information.html")


# In[4]:


time.sleep(3)


# In[5]:


browser.maximize_window()


# In[6]:


TotalData=[]


# In[17]:


browser.find_element_by_link_text('閱讀白皮書').click() 


# In[8]:


c_url = browser.current_url
browser.get(c_url)
html = browser.page_source
soup=BeautifulSoup(html,'html.parser')


# In[19]:


#link=soup.find('a')
#print(link)


# In[ ]:





# In[ ]:




