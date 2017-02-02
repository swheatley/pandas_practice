#!/usr/bin/python

import quandl
# Quandl import needs to be lowercase according to docs

import pandas as pd
import html5lib

api_key = 'wjsyCxbhA1vgsY6VEvAq'

# df = quandl.get('FMAC/HPI_AK', authtoken=api_key)

# print(df.head())

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

# this is a list:
# print(fiddy_states)

# this is a dataframe
# print(fiddy_states[0])

# this is a column
print(fiddy_states[0][0])

for abbv in fiddy_states[0][0][1:]:
    print("FMAC/HPI_AK"+str(abbv))


