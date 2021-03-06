"""
Created on Sun Oct 31 12:09:22 2021

@author: Jojo
"""
#purpose of this is to create a list to help with the sorting of the data into states after this

import numpy as np
import pandas as pd
import glob

#Change the path to wherever you have the files located
#path = "C:\\Users\Jojo\Documents\Test"
#path = "C:/Users/eddya/Desktop/21-22 First Semester/Data Mining/State-Of-The-Energy/csv/NOAA"
path = "./Data/csv/NOAA"
#This will generate the list of files so you don't have to manually enter the names
files = glob.glob(path + "/*.csv")
content = []
#idk about this part, I couldn't get the code to work properly without this after the line above

#ignore this, it was to help me test my code
#df = pd.read_csv('C:/Users/Jojo/Documents/Test/SumUS1AKAB0001.csv', index_col=None)

#State Abb is a cvs file that will help sort the data by states, I should have it on github
#States = pd.read_csv('C:/Users/eddya/Desktop/21-22 First Semester/Data Mining/State-Of-The-Energy/Data/csv/State Abb.csv',index_col=None)
States = pd.read_csv('./Data/csv/State Abb.csv',index_col=None)
Abbr = np.array(States.Abbr)

# empty DF for combining later
order = pd.DataFrame()
#This next DataFrame is to catch the data with Stations that have their names entered wrong, they will have to be coded in to the correct state case by case
misc = pd.DataFrame()

#file for annoying files
file1 = open("problemFiles.txt", "a")

for filename in files:
    #this will read the file and exact the Name of the station which should have the state name abbrivated in the name.
    df = pd.read_csv(filename, index_col=None)
    # This next part cuts out all letters before the Abbrivation in the name in theory
    try:
        name = list(df.NAME[0])
    except:
        file1.write(filename + " \n")
    if (name is not None):
        #-3 is blank space, -2 is U, -1 is S " US"
        ST = str(name[len(name)-5]+name[len(name)-4])
        try:
            y = pd.DataFrame([df.STATION[0],ST])
        except:
            file1.write(filename + " \n")
        if y is not None:
            if sum(ST==States.Abbr) ==1:
                order = pd.concat([order,y],axis=1)
            else:
            #Some entrys may have a comma which will screw this up so misc will catch them and any other errors in the naming
                misc = pd.concat([misc,y],axis=1)
        
order = order.transpose()
print(order)
order.columns = ['Station','Abbr']
order = order.set_index('Abbr')
order.to_csv('Order' + '.csv')

misc = misc.transpose()
misc.columns = ['Station','Abbr']
misc = misc.set_index('Abbr')
misc.to_csv('Misc' + '.csv')
