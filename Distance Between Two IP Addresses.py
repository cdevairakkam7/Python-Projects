
# Note in order for this to work you need to generate a access key from ipstack.com
# coding: utf-8

# In[1]:


# Importing Required Modules
import requests
import csv
import pandas as pd 
from geopy.distance import geodesic


# In[2]:


# Add Try catch
# reading csv using pandas 
data_set = pd.read_csv("https://www.dropbox.com/s/56njnjab3m159wb/D4-ipstack.csv?dl=0")


# In[3]:


# Adding Extra columns Needed
data_set['loan_lat']=''
data_set['loan_lng']=''
data_set['payment_lat']=''
data_set['payment_lng']=''
data_set['distance_miles']=''


# In[4]:


for row in data_set.iterrows():
    # Retrieve lat long for loan Ip
    a=row[0]
    loan_ip = data_set['loan_ipaddress'][a]
    url='http://api.ipstack.com/'+loan_ip+'?access_key=XXX'
    response = requests.get(url)
    response=response.json()
    data_set['loan_lat'][a]=response['latitude']
    data_set['loan_lng'][a]=response['longitude']
        # Retrieve lat long for Payment Ip
    b=row[0]
    pay_ip =data_set['payment_ipaddress'][b]
    pay_url='http://api.ipstack.com/'+pay_ip+'?access_key=XXX'
    pay_response = requests.get(pay_url)
    pay_response=pay_response.json()
    data_set['payment_lat'][b]=pay_response['latitude']
    data_set['payment_lng'][b]=pay_response['longitude']


# In[5]:


# Add Try catch
    #getting the distance 
for row in data_set.iterrows():
    s=row[0]
    i =(data_set['loan_lat'][s],data_set['loan_lng'][s])
    c =(data_set['payment_lat'][s],data_set['payment_lng'][s])
    #print(i,c)
   # data_set['distance_miles'][c]=str(geodesic(i, c).miles)+' miles'
    #print(str(geodesic(i, c).miles)+' miles')
    data_set['distance_miles'][s]=geodesic(i, c).miles
    





print(data_set)







