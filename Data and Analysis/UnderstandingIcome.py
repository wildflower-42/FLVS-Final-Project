import numpy as np 
import matplotlib as mpl 
import csv
import matplotlib.pyplot as plt 
dataToPlotA = []
dataToPlotB = []
dataToPlotC = []
dataToPlotD = []
Titles = []
def openCSV():
    with open('IncomeOfCollegeMajors.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for lines in csvFile: 
            dataQ1XQ2 = [float(lines[5]),float(lines[2]),float(lines[7])]
            title = lines[0]
            dataToPlotA.append(dataQ1XQ2)
            Titles.append(title)
            dataToPlotB.append(float(lines[5]))
            dataToPlotC.append(float(lines[2]))   
            dataToPlotD.append(float(lines[7]))
#This function creates our graph for data anyalsis:            
def boxplot(Data,Title):
    figure = plt.figure()
    ax = figure.add_subplot()
    bp = ax.boxplot(Data)
    #This section adds 3 lines to the graph,
    #which indicate the trends of the Quarter 1 and Quarter 2 (25th and 75th Percentiles respectively),
    #in addition to the median, values throughout the dataset.
    ax.plot(dataToPlotB)
    ax.plot(dataToPlotC)
    ax.plot(dataToPlotD)
    ax.set_xticklabels(Title)
    plt.xticks(rotation= 90)
    plt.show()
#We put our data and title to plot in our call for the function we just wrote:
#boxplot(dataToPlot,title)
def main():
    openCSV()
    boxplot(dataToPlotA,Titles)
main()