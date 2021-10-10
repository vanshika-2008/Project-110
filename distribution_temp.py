import statistics
import random
import pandas as pds
import csv
import plotly.figure_factory as pxfig
import plotly.graph_objects as pxgo

dataframe = pds.read_csv('data.csv')
data = dataframe['temp'].tolist()
Population_Mean = statistics.mean(data)
Standard_Deviation = statistics.stdev(data)
print(Population_Mean,Standard_Deviation)
plot = pxfig.create_distplot([data],['Temperature'],show_hist=False)
plot.add_trace(pxgo.Scatter(x=[Population_Mean,Population_Mean],y=[0,1],mode = 'lines',name = 'Mean'))
#plot.show()

def random_SetOfMean() :
    dataset = []
    for i in range(0,100) :
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)

    mean = statistics.mean(dataset)
    st_dev = statistics.stdev(dataset)
    #print(mean,st_dev)
    return(mean)
    
def Setup () :
    Mean_List = []
    for i in range(0,1000) :
        SetOfMeans = random_SetOfMean()
        Mean_List.append(SetOfMeans)
    Sampling_Mean = statistics.mean(Mean_List)
    Sampling_stdev = statistics.stdev(Mean_List)
    print(Sampling_Mean,Sampling_stdev)
    fig = pxfig.create_distplot([Mean_List],['Sampling Distribution'], show_hist=False)
    fig.show()

Setup()