#!/usr/bin/env python
# coding: utf-8

# # Steamtown Marathon Anaysis of Change in Pace
# 
# This notebook takes the information made available by the Steamtown Marathon, calculates the change in pace between the first 18 miles and the rest of the marathon, and ranks the field by that change in pace. Columns for "First_18_Pace," "Last_8.2_Pace," and "change_in_pace" were calculated and added to the table. The "change_in_pace" column was used to order the field based on increase in pace, and the ranks are in the "change_in_pace_place." No one ran a negative split. Some runners did not have a recorded time at the 18 mile split timing mat, and paces could not be calculated or compared. 
# 
# To run this Notebook, use Cell- Run All. The output will be a .csv file named steamtown_pace.  
# 

# In[36]:


import pandas as pd


# In[12]:


url = "http://steamtownmarathon.com/wp-content/uploads/2019/10/Steamtown-Final-Report-10-16-19-Update.xls"
df1 = pd.read_excel(url, converters={'18 MILE SPLIT':str,'CHIP TIME':str})


# In[13]:


df1['18 MILE SPLIT'] = pd.to_timedelta(df1['18 MILE SPLIT']) #converts the number value to a timedelta vs. string
df1['CHIP TIME'] = pd.to_timedelta(df1['CHIP TIME']) 


# In[14]:


df1['First_18_Pace'] = pd.Series(df1['18 MILE SPLIT'] / 18) #makes a new column with pace for 18 miles 
df1['Last_8.2_Pace'] = pd.Series((df1['CHIP TIME'] - df1['18 MILE SPLIT'])/8.2) #makes a new column with pace for rest of race
df1['change_in_pace'] = pd.Series(abs(df1['First_18_Pace'] - df1['Last_8.2_Pace'])) #makes a new column for difference in pace


# In[15]:


df2 = df1.sort_values('change_in_pace') #sorts based on change in pace from the split
df2.insert(0, 'change_in_pace_place', range(len(df2)))
df2


# In[16]:


df2.to_csv('steamtown_pace.csv')  # outputs .csv version 

