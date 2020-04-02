# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 08:03:28 2020

@author: samn_
"""

import pandas as pd

df = pd.read_csv("S:\\work\\python\\requests\\HR_comma_sep.csv")
#for type
type(df)
#check dimesnsion of data
df.shape
#name of columns
df.columns
#first n rows data
df.head(5)
#bottom n rows
df.tail(5)
#information of dataset(hidhlevel view)
df.info()
#summary of dataset
df.describe()
#check unique values of a column
df['left'].unique()
#extract certain columns to a new dataframe
df2 = df[['satisfaction_level','sales', 'salary']]
#take small portion of data from existing dataframe(row, column)
df_copy = df.iloc[0:5,:5]
#for random columns
df.iloc[0:5,[0,5,6]]
#create a new column
df['col1'] = 1
#create column from existing column
df['col2'] = df['satisfaction_level'] * df['number_project']
#delete a column
del df['col1']
#perform string operation on a column
df['salary'].str.upper()
df['salary_new'] = df['salary'].str.upper() + '-new'

#filtered column
df_filtered = df[df['number_project']>4]
#multiple filters
df_filtered = df[(df['number_project']>4) & (df['salary']=="low")]
#check minimum in a column
df_filtered['number_project'].min()
#sorting by columns
df.sort_values(["last_evaluation", "average_montly_hours"], ascending =[1,0])
#groupby function
df_grouped = df.groupby(["salary"], as_index = False)["satisfaction_level"].sum()
df_grouped = df.groupby(["salary"], as_index = False)["satisfaction_level"].mean()
#multiple groupby
df_grouped_multiple = df.groupby(["salary","sales"], as_index = False)["satisfaction_level"].sum()
#merge- happens on a specfied column, join-happens on a key(index)
left = df
right = df.groupby(['sales'], as_index = False)['satisfaction_level'].mean()
right.columns = ["sales","satisfaction_index"]
df_merged = pd.merge(left, right, how = "inner", on = ["sales"])

#join
left1 = df.iloc[:1500,:4]
right1 = df.iloc[:500,7:]

joined = left1.join(right1, how = "inner")
joined = left1.join(right1, how = "left")
joined = left1.join(right1, how = "right")

#concat
df_grouped1 = df.groupby(['sales'], as_index = False)['satisfaction_level'].mean()
df_grouped2 = df.groupby(['sales'], as_index = False)['satisfaction_level'].sum()
concated = pd.concat([df_grouped1, df_grouped2])#vertical concat, adds two data in one
concated = pd.concat([df_grouped1, df_grouped2], axis = 1)

#pivot
df_pvt =  df.groupby(['sales', 'salary'], as_index = False)['satisfaction_level'].mean()
df_pvt2 = df_pvt.pivot(index = "sales", columns = "salary", values = "satisfaction_level")