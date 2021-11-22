"""
Created on Thu Nov 18
File to aggregate data from each states weather stations to data for just that state from the average of each weather station
@author: Edward
"""

import numpy as np
import pandas as pd
import glob
#location of the data sets
#path = "Data/NOAA Cleaned"
path = "Data/NOAA Cleaned"
pathTo = "Data/NOAA Aggregate"

#creating list of all csv in the folder which only holds the dataset we are working with
files = glob.glob(path + "/*.csv")
RangeYear = np.arange(1960,2022)
#content = []

for filename in files:
    df = pd.read_csv(filename, index_col='Unnamed: 0')
    dfState = pd.DataFrame(columns=['YEAR', 'DP01', 'DP10', 'DP1X', 'DSND', 'DSNW', 'EMSD', 'EMSN', 'EMXP', 
    'PRCP', 'SNOW', 'DYFG', 'DYTS', 'AWND', 'CDSD', 'CLDD', 'DT00', 'DT32', 'DX32', 'DX70', 'DX90', 
    'EMNT', 'EMXT', 'EVAP', 'HDSD', 'HTDD', 'MNPN', 'MXPN', 'TAVG', 'TMAX', 'TMIN', 'WDMV', 'WDFG', 
    'WSFG', 'HX01', 'LX01', 'MX01', 'DYHF', 'TSUN', 'WDF2', 'WDF5', 'WSF2', 'WSF5', 'PSUN'])
    #this if statment will skip any empty dataframes from the first cleaning
    if df.empty == False:
        state = filename[len(filename)-6:len(filename)-4]
        for year in RangeYear:
            dfYear = df.loc[df['YEAR'] == year]
            dfYear = dfYear.drop(columns=['STATION', 'LATITUDE', 'LONGITUDE', 'ELEVATION', 'NAME'])
            colNames = []
            colDataList = []
            for (colName, colData) in dfYear.iteritems():
                #print(colName)
                colNames.append(colName)
                #print(colData.mean())
                if colName != 'YEAR':
                    colDataList.append(colData.mean())
                else:
                    colDataList.append(int(colData.mean()))
            
            dfNew = pd.DataFrame(columns=colNames)
            dfNewLength = len(dfNew)
            dfNew.loc[dfNewLength] = colDataList
            dfState = dfState.append(dfNew)
    dfState.to_csv(pathTo + '/' + state + ' Aggregate' + '.csv')        
    

                

print('Done')    

