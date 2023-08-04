import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read in the file
filein = pd.read_csv('https://raw.githubusercontent.com/FLBronson/ABVWrangles/main/data.csv')

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
print('LA1and10 = Low access tract at 1 mile for urban areas and 10 miles for rural areas\n')


#Print Values
print('Food Deserts in the United States Data')
print('===================================================================')
print(filein[['State', 'County', 'Pop2010', 'LILATracts_1And10', 'LA1and10']])
print()

#Variables
usTC = 72531 #US Total Count
usLILA = filein['LILATracts_1And10'].value_counts()[1] #US Low Income and Low Access
usFL = filein['State'].value_counts()['Florida']  #Number of instances in FL
usGA = filein['State'].value_counts()['Georgia']  #Number of instances in GA
usAL = filein['State'].value_counts()['Alabama']  #Number of instances in AL
usFLLALI = filein['State'].value_counts()['Florida'] & filein['LILATracts_1And10'].value_counts()[1] #Number of instances in FL that are low income/low access
usGALALI = filein['State'].value_counts()['Georgia'] & filein['LILATracts_1And10'].value_counts()[1] #Number of instances in GA that are low income/low access
usALLALI = filein['State'].value_counts()['Alabama'] & filein['LILATracts_1And10'].value_counts()[1] #Number of instances in AL that are low income/low access

#Number of food deserts out of all data values
print('Number of low access/low income areas in the United States (1mi Urban/10mi Rural):', usLILA, 'out of', usTC)
print('That is roughly', '{:.0%}'.format(usLILA/usTC), 'of the United States that is low access/low income to supermarkets.\n')
print('Number of low access/low income areas in Florida affected by food deserts:', usFLLALI, '/', usFL)
print('That is roughly', '{:.0%}'.format(usFLLALI/usFL), 'of Florida that is low income / low access to supermarkets.\n')
print('Number of low access/low income areas in Georgia affected by food deserts:', usGALALI, '/', usGA)
print('That is roughly', '{:.0%}'.format(usGALALI/usGA), 'of Georgia that is low income / low access to supermarkets.\n')
print('Number of low access/low income areas in Alabama affected by food deserts:', usALLALI, '/', usAL)
print('That is roughly', '{:.0%}'.format(usALLALI/usAL), 'of Alabama that is low income / low access to supermarkets.\n')

#Calculations for graphs for FL
flFoodDesert = usFLLALI
flNoFoodDesert = usFL

#Calculations for graphs for GA
gaFoodDesert = usGALALI
gaNoFoodDesert = usGA

#Calculations for graphs for AL
alFoodDesert = usALLALI
alNoFoodDesert = usAL

#Create graph
graphx = ['Food Desert', 'No Food Desert']
graphy = [flFoodDesert, flNoFoodDesert]
plt.bar(graphx, graphy)
addlabels(graphx, graphy)
plt.title('Florida Food Deserts')
plt.ylabel('Number of areas within state')
plt.xlabel('Is the area a food desert or not?')
plt.show()