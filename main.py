import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read in the files
usFile = pd.read_csv('https://raw.githubusercontent.com/FLBronson/ABVWrangles/main/data.csv')
flFile = pd.read_csv('https://raw.githubusercontent.com/FLBronson/ABVWrangles/main/florida.csv')
gaFile = pd.read_csv('https://raw.githubusercontent.com/FLBronson/ABVWrangles/main/georgia.csv')
alFile = pd.read_csv('https://raw.githubusercontent.com/FLBronson/ABVWrangles/main/alabama.csv')

#Add labels to graph
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')

#Legend
print('The ABV Wranglers Dataset')
print('===================================================================')
print('Column Header information:')
print('State = The State of data')
print('County = The county of the data')
print('Pop2010 = The Population of the data in 2010')
print('LILATracts_1And10 = Low income and low access tract measured at 1 mile for urban areas and 10 miles for rural areas')

#Print Values
print('Food Deserts in the United States Data')
print('===================================================================')
print(usFile[['State', 'County', 'Pop2010', 'LILATracts_1And10']])
print()

#Variables
totalUS = 72531 #US Total Count
totalFL = flFile['State'].value_counts()['Florida']  #Number of instances in FL
totalGA = gaFile['State'].value_counts()['Georgia']  #Number of instances in GA
totalAL = alFile['State'].value_counts()['Alabama']  #Number of instances in AL
usLILA = usFile['LILATracts_1And10'].value_counts()[1] #US Low Income and Low Access
lilaFL = flFile['LILATracts_1And10'].value_counts()[1]
lilaGA = gaFile['LILATracts_1And10'].value_counts()[1]
lilaAL = alFile['LILATracts_1And10'].value_counts()[1]

#Number of food deserts out of all data values
print('This data is gathered with the fact that these data values consider low accessibilty')
print('Number of low access/low income areas in the United States (1mi Urban/10mi Rural):', usLILA, 'out of', totalUS)
print('That is roughly', '{:.0%}'.format(usLILA/totalUS), 'of the United States that is low access/low income to supermarkets.\n')
print('Number of low access/low income areas in Florida affected by food deserts:', lilaFL, '/', totalFL)
print('That is roughly', '{:.0%}'.format(lilaFL/totalFL), 'of Florida that is low income / low access to supermarkets.\n')
print('Number of low access/low income areas in Georgia affected by food deserts:', lilaGA, '/', totalGA)
print('That is roughly', '{:.0%}'.format(lilaGA/totalGA), 'of Georgia that is low income / low access to supermarkets.\n')
print('Number of low access/low income areas in Alabama affected by food deserts:', lilaAL, '/', totalAL)
print('That is roughly', '{:.0%}'.format(lilaAL/totalAL), 'of Alabama that is low income / low access to supermarkets.\n')

#Calculations for graphs for FL
flFoodDesert = lilaFL
flNoFoodDesert = totalFL

#Calculations for graphs for GA
gaFoodDesert = lilaGA
gaNoFoodDesert = totalGA

#Calculations for graphs for AL
alFoodDesert = lilaAL
alNoFoodDesert = totalAL

#Create graph
graphx = ['Food Desert', 'No Food Desert']
graphy = [flFoodDesert, flNoFoodDesert]
plt.bar(graphx, graphy)
addlabels(graphx, graphy)
plt.title('Florida Food Deserts')
plt.ylabel('Number of areas within state')
plt.xlabel('Is the area a food desert or not?')
plt.show()