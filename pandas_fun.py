#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')


web_stats = {"Day": [1,2,3,4,5,6],
             "Visitors": [43,53,34,64,34,10],
             "Bounce_Rate": [65, 72, 62, 64,  54, 66]
             }

df = pd.DataFrame(web_stats)

# print(df)
# print(df.head)
# print(df.tail())
# print(df.tail(2))

# print(df.set_index('Day'))
# print(df.head())

# df2 = df.set_index('Day')
# print(df.head())

# df.set_index('Day', inplace=True)
# print(df.head())

# print(df['Bounce_Rate'])
# print(df.Visitors)


print(df.Visitors.tolist())
print(np.array(df[['Bounce_Rate', 'Visitors']]))

df2 = pd.DataFrame(np.array(df[['Bounce_Rate', 'Visitors']]))

print(df2)