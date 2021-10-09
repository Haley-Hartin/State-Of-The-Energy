import pandas as pd
import os

#Setting path for orignial data set
directory = os.path.join("C:\\Users\Jojo\Documents\Test")

#cleaning part
for root,dirs,files in os.walk(directory):
    for file in files:
       if file.endswith(".csv"):
           ss = open(file, 'r')
           x = pd.read_cvs(ss)

           #grabbing station ID for csv naming
           station_name = x.STATION[1]
             
           #Dropping anything before 1960-01, will return empty matrix if data doens't go past 1960-01
           d = x.index[x['DATE'] <= '1959-12'].tolist()
           x = x.drop(x.index[d])
             
             #writing new csv
           x.to_csv(x.STATION[1]+ '.csv')
           ss.close()
           
           """
           Line 18
           FileNotFoundError: [Errno 2] No such file or directory: 'ACW00011604.csv'
           There is a file at this location but Python doesnt see it
           """
