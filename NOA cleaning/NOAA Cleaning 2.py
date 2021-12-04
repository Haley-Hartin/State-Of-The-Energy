"""
Created on Sat Oct 16 17:02:12 2021

@author: Jojo
"""

import numpy as np
import pandas as pd
import glob
#location of the data sets
path = "C:\\Users\Jojo\Documents\gsom-latest"

#creating list of all csv in the folder which only holds the dataset we are working with
files = glob.glob(path + "/*.csv")
content = []

#Code below is for debugging
#df = pd.read_csv('C:/Users/Jojo/Documents/Test/AE000041196.csv', index_col=None)

#This part cleans out the non US data

#Sorting range for summary
RangeYear = np.arange(1960,2022)
    
for filename in files:
    df = pd.read_csv(filename, index_col=None)
    #this if statment will skip any empty dataframes from the first cleaning
    if df.empty == False:
        station_name = df.STATION[0]
        state = df.NAME[0]

        #this is for filtering out the locations not in the USA
        if 'US' in station_name:
            sum = pd.DataFrame()
            #summarizing the data by years, this step drops strings and doesn't drop any year without data
            for i in RangeYear:
                x = df.drop(df.index[df['DATE'] <= (str(i)+'-01')].tolist())
                x = x.drop(df.index[df['DATE'] > (str(i)+'-12')].tolist())
                xsum = np.mean(x)
                #pd.describe for 5 num sum, not used here but maybe useful later
                #combining year and the previous year into one matrix
                sum = pd.concat([sum,xsum],axis=1)

            #Naming the columns as columns aren't named    
            sum.columns = RangeYear
            
            #removing ATTRIBUTE columns as they provide no use analytically
            for attr in sum.index:
                if "ATTRIBUTES" in attr:
                    sum = sum.drop(attr)
            
            #dropping date(MM/DD/YYYY) as the year is an index/column
            #'Unnamed :0' is the entry number of the data from the source
            sum = sum.drop('Unnamed: 0')
            if 'DATE' in sum.index:
                sum = sum.drop('DATE')

            #filling in missing data lost  from np.mean
            sum = sum.transpose()
            sum.STATION = station_name
            sum.NAME = state# for data cubing construction
            
            #Prints DF into .csv into base directory, not in the path from above
            sum.to_csv('Sum' + station_name + '.csv')
            
        else:
            print('Not in US')
                

print('Done')    
#Blank data means there was no recordings for that year. If there is partial recording then the mean will be calc
