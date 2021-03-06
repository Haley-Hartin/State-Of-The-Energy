"""
Created on Wed Nov  3 16:31:28 2021

@author: Jojo
"""
import pandas as pd

#Cleaning 3
#This code actually sorts the stations together for a state

States = pd.read_csv('./Data/csv/State Abb.csv',index_col=None)
# Order is from Cleaning 2.5
order = pd.read_csv('./Order.csv',index_col='Abbr')
# Path is wherever files are located, only important part is the "Sum" part of the line as the files start with "Sum"
path = './Data/csv/NOAA/Sum'

# Doing this state by state
for ab in States.Abbr:
    #empty DF for combining and also resets for the next iteration
    cube = pd.DataFrame()
    #Next line drops the irrelevant states and keeps the normal ones
    #There is an error with .loc(ab), if their isn't a match it will throw an error, this if statement should take care of it
    if sum(ab==order.index)!=0:
        ListStations = order.loc[ab]
        # this next part is to read the relevant stations to the state and combine the dataset
        for StationName in ListStations.Station:
            # this next part is to automate the file reading based on the list created above
            df = pd.read_csv(path+StationName+'.csv',index_col = None)
            cube = pd.concat([cube,df],axis=0)
            #for debugging: There is this weird error where if there is only one item in ListStations it will spell out the station name, instead of listing it 
            #print(StationName)
        #prints the final csv for the state
        #also the column containing the year is unnamed, we will have to rename it later or now.
        cube.to_csv(ab + '.csv')
        
        
