import matplotlib
import math
import numpy
import csv
import matplotlib.pyplot as plt
hours = []
labels = []
def openCSV():
    with open('HoursSpentStudyingByMajors.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for lines in csvFile: 
            hours.append(float(lines[1]))
            labels.append(str(lines[0]))
def barGraph():
    openCSV()
    data1 = hours
    #matplotlib.rcParams.update({'font.size': 5})
    plt.barh(range(len(data1)), data1)
    plt.yticks(range(len(data1)), labels, rotation= 0)
    # Labeling the X-axis 
    plt.ylabel('Major') 
    # Labeling the Y-axis 
    plt.xlabel('Hours of Studying per week') 
    plt.show()
barGraph()