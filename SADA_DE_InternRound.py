#!/usr/bin/env python
# coding: utf-8

# In[539]:


#importing libraries
import pandas as pd
import json
import requests
import io
import os


url = "https://github.com/Guptashreya2304/SADA_DE/raw/master/raw.txt" 
download_url = requests.get(url).content

raw_csvfile = pd.read_csv(io.StringIO(download_url.decode('utf-8')))

#gives the first 5 rows from the table
raw_csvfile.head()

#total number of rows 
#Answer 1

len(raw_csvfile)


# In[540]:


raw_csvfile.info ()


# In[541]:


raw_csvfile.columns = [ 'Year','Rank','Company','Revenue_inMillions','Profit_inMillions']


# In[542]:


raw_csvfile.head()
raw_csvfile.info ()


# In[543]:


raw_csvfile = raw_csvfile[raw_csvfile['Profit_inMillions'] != 'N.A.']





# In[544]:


#Answer 2 after the removal of non-numeric values from the dataframe 
len(raw_csvfile)
#len(df_new)
#print(pd.to_numeric(raw_csvfile['Profit_inMillions'], errors = 'coerce'))

#raw_csvfile.apply(lambda s: pd.to_numeric(s, errors = 'coerce').notnull().all())

#print (pd.to_numeric(raw_csvfile['Profit_inMillions'], errors = 'coerce').notnull().all())



# In[545]:


#command to check the working library
print (os.getcwd()) 

#converting the content to json file with only valid profit values
raw_csvfile.to_json('data2.json')



# In[547]:


# Read the JSON file 
df = pd.read_json('data2.json', orient='columns')

#Descending order of the data based on profit value
df = df.sort_values(by=['Profit_inMillions'], ascending=False)

#Print the top 20 rows with the highest profit values
#Answer 3
print("Print the top 20 rows with the highest profit values")

df.head(20)



# -----

# In[548]:


#Extra Credit
import json

with open ('data2.json') as f:
    data_dict = json.load(f)

#This prints the dictonary of the data
print(data_dict)



# In[549]:


df = pd.read_json('data2.json', orient='columns')
company_unique=df.Company.unique()


# In[552]:


#dataframe
df
#Answer 4
len(company_unique)



# In[553]:


groupby_company=df.groupby('Company')


# In[554]:


groupby_company.groups


# In[559]:


df_company_info = pd. DataFrame({'count': groupby_company.size()}).reset_index()
df_company_info

df_sorted=df_company_info.sort_values(by='count', ascending=False, na_position='first')
df_sorted
#Answer 5
toptenreported = df_sorted.head(10)

#dataframe for answer 5
toptenreported

print(toptenreported['Company'].to_list())


# In[334]:


#List the number of companies that have only reported data once
#answer 6


# In[560]:



df


# In[562]:


reportedonce=df[df.groupby('Company')['Company'].transform('count') == 1]
#reported once
reportedonce


# In[570]:


list_answer6 = reportedonce['Company'].tolist()
print("answer 6")
list_answer6


# ------
# 
