# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:38:12 2020

@author: samn_
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#get data from api about coronavirus cases
response = requests.get("https://corona.lmao.ninja/countries")
data = np.array(response.json())
#print(data)
df1 = pd.DataFrame.from_records(data)
df2 = pd.DataFrame.from_records(df1['countryInfo'])
del df1['countryInfo']

df1.describe()

df1_plot = df1[["country","cases", "critical", "deaths", "recovered"]]

#take only 10 data and all columns after sorting with column in asc/desc order
df1_plot1 = df1_plot.sort_values(['critical'], ascending = [False]).iloc[0:10,:]
df1_plot1['key'] = range(0,len(df1_plot1))

#start plotting
plt.xticks(df1_plot1["key"],df1_plot1["country"], rotation = "vertical")
plt.xlabel("Countries")
plt.ylabel("Total Cases upto Today for countries with most deaths")
plt.bar(df1_plot1["key"],df1_plot1["recovered"], color = "green", align = "center" )
plt.bar(df1_plot1["key"],df1_plot1["critical"], color = "red", align = "center" )
#plt.bar(df1_plot1["key"],df1_plot1["cases"])
plt.show()