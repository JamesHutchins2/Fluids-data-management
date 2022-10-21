#Imports
import os 
import pandas as pd
#define directory
dir = 'data'
#initialize array to hold data frames
dataFrames = []
stdFrames = []
#loop through all files in the directory
for filename in os.listdir(dir):
    #get the file name
    f = os.path.join(dir, filename)
    #mutate file name
    fname = "H" + f
    
    #read the csv file and store in a data frame with given column headers
    fname =pd.read_csv(f, usecols=[0,1,2,3,4], names=['x','y','z','a','b','trial name'])
    #assign file name to column 
    fname['trial name'] = f
    #append the array with this data frame 
    dataFrames.append(fname)
#same operation for standard deviation
for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    fname_stdDev = 'std' + f
    fname_stdDev =pd.read_csv(f, usecols=[0,1,2,3,4], names=['x','y','z','a','b','trial name'])
    #get the standard deviation in each column
    fname_stdDev = fname_stdDev.std()
    fname_stdDev['trial name'] = f
    stdFrames.append(fname_stdDev)
    

    

   
    
#concatinate frame_stdDev with stdFrames row by row so
frame_stdDev = pd.concat(stdFrames, axis=1, ignore_index=False)
#print to csv



frame_stdDev.to_csv('stdDev.csv')
#concatinate all the data frames
frame = pd.concat(dataFrames, axis=0)
#group by trial name and take the mean values
frame = frame.groupby('trial name').mean()
#print to csv file
frame.to_csv('mean.csv')
