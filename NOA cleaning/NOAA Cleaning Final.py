# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:45:27 2021

@author: Jojo
"""

import pandas as pd
import glob

"""
this scrip will combine all the datasets into one final set and set it up
so we can call out the data easier

Year has to be a string to make it easier to call out.

Use this code to import the csv so you can call out the rows when you grab a column
the index_col part is the most important part here

final= pd.read_csv('final.csv',index_col=[0,1],header=[0,1])

*if lines 63-80 were removed/inactivated, clvl2 and clvl1: 
    DO NOT USE: header=[0,1]

final= pd.read_csv('final.csv',index_col=[0,1],header=[0,1])

Ex: Trying to select the avg temp in a year for all states

[In]:Temp_avg = final.TEMP.TAVG

*if header=[0,1] was not used then use this instead:

[In]:Temp_avg = final.TAVG    

[In]:Temp_avg[:,'2020']
[Out]:AK     1.234001
      AL    18.521110
      ...

From here if you want to single out a state for the regions, you can do something like this
But this will remove the index hierarchy
[In]: x = pd.DataFrame((temp['AL'],temp['AK']),index=['AL','AK'])

Useful codes:
    final.columns
    final.index

"""

path = "Data/NOAA Aggregate"
files = glob.glob(path + "/*.csv")

final = pd.DataFrame()
lvl1 = ['1960', '1961', '1962', '1963', '1964', '1965', '1966',
       '1967', '1968', '1969', '1970', '1971', '1972', '1973',
       '1974', '1975', '1976', '1977', '1978', '1979', '1980',
       '1981', '1982', '1983', '1984', '1985', '1986', '1987',
       '1988', '1989', '1990', '1991', '1992', '1993', '1994',
       '1995', '1996', '1997', '1998', '1999', '2000', '2001',
       '2002', '2003', '2004', '2005', '2006', '2007', '2008',
       '2009', '2010', '2011', '2012', '2013', '2014', '2015',
       '2016', '2017', '2018', '2019', '2020', '2021']
for file in files:
    df = pd.read_csv(file, index_col=None)
    df = df.drop(df.columns[0],axis=1)
    df = df.drop(df.columns[0],axis=1)
    Name = list(file)
    ST = (file[len(Name)-16]+file[len(Name)-15])
    
    df = df.set_index([lvl1])
    df = df.assign(l2=ST).set_index('l2', append=True)
    final = pd.concat([final,df],axis=0)


# If this is causing an error, then delete/comment out from here:
# clvl2 = ['RAIN', 'RAIN', 'RAIN', 'SNOW', 'SNOW', 'SNOW', 'SNOW', 'RAIN', 'RAIN',
#        'SNOW', 'FOG', 'RAIN', 'WIND', 'TEMP', 'TEMP', 'TEMP', 'TEMP', 'TEMP',
#        'TEMP', 'TEMP', 'TEMP', 'TEMP', 'RAIN', 'HDSD', 'TEMP', 'TEMP', 'TEMP',
#        'TEMP', 'TEMP', 'TEMP', 'WIND', 'WIND', 'WIND', 'SOIL', 'SOIL', 'SOIL',
#        'FOG', 'SUN', 'WIND', 'WIND', 'WIND', 'WIND', 'SUN', 'SOIL', 'SOIL',
#        'SOIL', 'SOIL', 'SOIL', 'SOIL', 'SOIL', 'SOIL', 'SOIL', 'SOIL', 'SOIL',
#        'SOIL', 'SOIL', 'SOIL', 'SOIL', 'SOIL', 'SOIL', 'SOIL', 'SOIL', 'SOIL',
#        'SOIL', 'WIND', 'WIND', 'WIND', 'WIND']

# clvl1 = final.columns
# final=final.transpose()
# final = final.assign(l1='GROUP').set_index('l1', append=True)
# final.index=[clvl1,clvl2]
# final.index.names = ['ATTR','GROUP']
# final = final.swaplevel('ATTR','GROUP')
# final=final.transpose()
# To here

final.index.names = ['YEAR','STATE']
final = final.swaplevel('STATE','YEAR')
final.to_csv('Data/NOAA Final/final' + '.csv')
"""
df2 = pd.read_csv('C:/Users/Jojo/Downloads/AL Aggregate.csv')
df2 = df2.drop(df2.columns[0],axis=1)
df2 = df2.drop(df2.columns[0],axis=1)
df2 = df2.set_index([lvl1])

df2 = df2.set_index([df2['YEAR'].astype(str)])

df2 = pd.read_csv('C:/Users/Jojo/Downloads/AL Aggregate.csv',index_col='YEAR')
df2 = df2.drop(df.columns[0],axis=1)

df = df.assign(l2='AK').set_index('l2', append=True)
df2 = df2.assign(l2='AL').set_index('l2', append=True)

final = pd.concat([df,df2],axis=0)

final.index.names = ['YEAR','STATE']
final = final.swaplevel('STATE','YEAR')

final.to_csv('final' + '.csv')
"""
