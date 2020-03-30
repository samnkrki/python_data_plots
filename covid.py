import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#get data from api about coronavirus cases
response = requests.get("https://corona.lmao.ninja/countries")
data = np.array(response.json())
#print(data)
ds = pd.DataFrame.from_records(data)
ds1 = pd.DataFrame.from_records(ds['countryInfo'])
del ds['countryInfo']

ds.to_csv("covid_cases.csv", index=False)
ds1.to_csv("covid_cases_countries.csv", index=False)
#read the csv and load to dataframe
#ds.describe()
#ds1.describe()
#ds1.info()

#merge dataframes
#df_merged = pd.merge(ds, ds1, how = "inner", on = [""])

#add index column to the dataframe
#ds.reset_index(level = "country")

#assign a new dataframe with these columns from old dataframe
df = ds[["cases", "country", "deaths","recovered"]]

#take only 10 data and all columns after sorting with column in asc/desc order
df1 = df.sort_values(['deaths'], ascending = [False]).iloc[0:20,:]
                     
#add a new column called key whose value is in increasing order                     
df1['key'] = range(0, 0+len(df1))

#start plotting
plt.xticks(df1["key"],df1["country"] )
plt.xlabel("Countries")
plt.ylabel("Total Cases upto Today for countries with most deaths")
plt.scatter(df1["key"],df1["cases"], color = "red",)
plt.show()

#scatter plot
plt.xticks(df1["key"],df1["country"] )
plt.bar(df1["key"], df1["recovered"], color = "green")
plt.bar(df1["key"], df1["deaths"], color = "red")
plt.title("Deaths and recovered per countries")
plt.xlabel("Countries")
plt.ylabel("Deaths and Recovered cases")
plt.show()