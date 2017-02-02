#!/usr/bin/python

import pandas as pd

# df = pd.read_csv('zillow_houses.csv')
# print(df.head())

# df.set_index('Date', inplace=True)
# df.to_csv('newcsv2.csv')

# df = pd.read_csv('newcsv2.csv', index_col=0)
# print(df.head())

# df.columns = ['Midvale_HPI']
# print(df.head())

# df.to_csv('newcsv3.csv')
# df.to_csv('newcsv4.csv', header=False)

# print(df.head())

# df = pd.read_csv('newcsv4.csv', names=['Date', 'Austin_HPI'], index_col=0)
# print(df.head())

# df.to_html('example.html')

df = pd.read_csv('newcsv4.csv', names=['Date', 'Austin_HPI'])
print(df.head())

df.rename(columns={'Austin_HPI': '84047_HPI'}, inplace=True)

print(df.head())