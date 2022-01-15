import plotly.figure_factory as pf
import plotly.graph_objects as pg
import csv
import statistics
import pandas as pd
import random

df = pd.read_csv('medium_data.csv')
data = df("reading_time").tolist()
#fig = ff.create_distplot([data], ["reading_time"] , show_hist=False)
#fig.show()

mean = statistics.mean(data)
std_dev = statistics.stdev(data)
print("population mean:-",mean)
print("--"*100)
print("population standard deviation :-",std_dev)
print("--"*100)

def randomSetOfMean(counter):
    dataSet = []
    for i in range(0,counter):
        index = random.randint(0, len(data)-1)
        value = data[index]
        dataSet.append(value) 

    mean = statistics.mean(dataSet)
    return mean

mean_list=[]

for i in range(0,100) :
    set_of_mean = randomSetOfMean(30)
    mean_list.append(set_of_mean)
    
mean_list_std_dev = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print("the std_dev of sampling distributions is ",mean_list_std_dev)
print("------------------------------------------------------------")

print("the mean of sampling distributions is",mean)

fig = pf.create_distplot([mean_list], ["Population"] , show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN"))
fig.show()

