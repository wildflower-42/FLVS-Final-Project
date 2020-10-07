import matplotlib
import math
import numpy
import csv
import matplotlib.pyplot as plt
employed = []
unemployed = []
labels = []
def openCSV():
    with open('EmploymentOfCollegeMajors.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for lines in csvFile: 
            employed.append(int(lines[4]))
            unemployed.append(int(lines[6]))
            labels.append((lines[0]))
def barGraph():
    openCSV()
    data1 = employed
    data2 = unemployed
    matplotlib.rcParams.update({'font.size': 5})
    plt.bar(range(len(data1)), data1)
    plt.xticks(range(len(data1)), labels, rotation= 90)
    plt.bar(range(len(data2)), data2, bottom=data1)
    plt.show()
barGraph()