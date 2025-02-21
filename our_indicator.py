import pandas as pd
from pandas_datareader import wb

df = wb.get_indicators()[['id','name']]
df = df[df.name == 'Individuals using the Internet (% of population)']

df2 = wb.get_indicators()[['id','name']]
df2 = df2[df2.name == 'CO2 emissions (kt)']

print(df)
print(df2)

