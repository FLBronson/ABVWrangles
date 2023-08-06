import pandas as pd
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
lilaUS = usFile['LILATracts_1And10'].value_counts()[1] #US Low Income and Low Access
lilaFL = flFile['LILATracts_1And10'].value_counts()[1] #FL Low Income and Low Access
lilaGA = gaFile['LILATracts_1And10'].value_counts()[1] #GA Low Income and Low Access
lilaAL = alFile['LILATracts_1And10'].value_counts()[1] #AL Low Income and Low Access
popUS = usFile['Pop2010'].sum() #US total population
popFL = flFile['Pop2010'].sum() #FL total population
popGA = gaFile['Pop2010'].sum() #GA total population
popAL = alFile['Pop2010'].sum() #AL total population

#Create dataframe with for every instance that is low income/low access and add all the population
dataframeUS = pd.DataFrame(usFile.loc[usFile['LILATracts_1And10'] == 1])
lilapopUS = dataframeUS['Pop2010'].sum()
dataframeFL = pd.DataFrame(flFile.loc[flFile['LILATracts_1And10'] == 1])
lilapopFL = dataframeFL['Pop2010'].sum()
dataframeGA = pd.DataFrame(gaFile.loc[gaFile['LILATracts_1And10'] == 1])
lilapopGA = dataframeGA['Pop2010'].sum()
dataframeAL = pd.DataFrame(alFile.loc[alFile['LILATracts_1And10'] == 1])
lilapopAL = dataframeAL['Pop2010'].sum()

#Number of food desert areas out of all data values
print('This data is gathered with the fact that these data values consider low accessibilty, and 1mi Urban/10mi Rural')
print('Number of low access/low income areas in the United States (1mi Urban/10mi Rural):', lilaUS, 'out of', totalUS)
print('That is roughly', '{:.0%}'.format(lilaUS/totalUS), 'of the United States that is low access/low income to supermarkets.\n')
print('Number of low access/low income areas in Florida affected by food deserts:', lilaFL, '/', totalFL)
print('That is roughly', '{:.0%}'.format(lilaFL/totalFL), 'of Florida that is low income / low access to supermarkets.\n')
print('Number of low access/low income areas in Georgia affected by food deserts:', lilaGA, '/', totalGA)
print('That is roughly', '{:.0%}'.format(lilaGA/totalGA), 'of Georgia that is low income / low access to supermarkets.\n')
print('Number of low access/low income areas in Alabama affected by food deserts:', lilaAL, '/', totalAL)
print('That is roughly', '{:.0%}'.format(lilaAL/totalAL), 'of Alabama that is low income / low access to supermarkets.\n')

#Number of food desert population out of all data values
print('\nThis data is gathered with the fact that these data values consider low accessibilty, and 1mi Urban/10mi Rural')
print('Number of low access/low income population in the United States (1mi Urban/10mi Rural):', (f"{lilapopUS:,}"), 'out of', (f"{popUS:,}"))
print('That is roughly', '{:.0%}'.format(lilapopUS/popUS), 'of the United States populations that is low access/low income to supermarkets.\n')
print('Number of low access/low income areas in Florida affected by food deserts:', (f"{lilapopFL:,}"), '/', (f"{popFL:,}"))
print('That is roughly', '{:.0%}'.format(lilapopFL/popFL), 'of Floridians that are low income / low access to supermarkets.\n')
print('Number of low access/low income areas in Georgia affected by food deserts:', (f"{lilapopGA:,}"), '/', (f"{popGA:,}"))
print('That is roughly', '{:.0%}'.format(lilapopGA/popGA), 'of Georgians that are low income / low access to supermarkets.\n')
print('Number of low access/low income areas in Alabama affected by food deserts:', (f"{lilapopAL:,}"), '/', (f"{popAL:,}"))
print('That is roughly', '{:.0%}'.format(lilapopAL/popAL), 'of Alabamaians that are low income / low access to supermarkets.\n')

''' 
Create Graphs for area food desert data

#Create graph Florida
graphx = ['Food Desert', 'No Food Desert']
graphy = [lilaFL, totalFL]
plt.bar(graphx, graphy)
addlabels(graphx, graphy)
plt.title('Florida Food Deserts')
plt.ylabel('Number of areas within state')
plt.xlabel('Is the area a food desert or not?')
plt.show()

#Create graph Georgia
graphx = ['Food Desert', 'No Food Desert']
graphy = [lilaGA, totalGA]
plt.bar(graphx, graphy)
addlabels(graphx, graphy)
plt.title('Georgia Food Deserts')
plt.ylabel('Number of areas within state')
plt.xlabel('Is the area a food desert or not?')
plt.show()

#Create graph Alabama
graphx = ['Food Desert', 'No Food Desert']
graphy = [lilaAL, totalAL]
plt.bar(graphx, graphy)
addlabels(graphx, graphy)
plt.title('Alabama Food Deserts')
plt.ylabel('Number of areas within state')
plt.xlabel('Is the area a food desert or not?')
plt.show()

#Create graph United States (population)
graphx = ['Food Desert', 'No Food Desert']
graphy = [lilapopUS, popUS]
plt.bar(graphx, graphy)
addlabels(graphx, graphy)
plt.title('United States Food Deserts by population')
plt.ylabel('Population affected by food deserts (hundred millions)')
plt.xlabel('Is the area a food desert or not?')
plt.show()

#Create graph Florida (population)
graphx = ['Food Desert', 'No Food Desert']
graphy = [lilapopAL, popAL]
plt.bar(graphx, graphy)
addlabels(graphx, graphy)
plt.title('Alabama Food Deserts by population')
plt.ylabel('Population affected by food deserts (millions)')
plt.xlabel('Is the area a food desert or not?')
plt.savefig('ALpopchart1.png')

#Create graph Georgia (population)
graphx = ['Food Desert', 'No Food Desert']
graphy = [lilapopGA, popGA]
plt.bar(graphx, graphy)
addlabels(graphx, graphy)
plt.title('Georgia Food Deserts by population')
plt.ylabel('Population affected by food deserts (ten millions)')
plt.xlabel('Is the area a food desert or not?')
plt.show()

#Create graph Alabama (population)
graphx = ['Food Desert', 'No Food Desert']
graphy = [lilapopAL, popAL]
plt.bar(graphx, graphy)
addlabels(graphx, graphy)
plt.title('Alabama Food Deserts by population')
plt.ylabel('Population affected by food deserts (millions)')
plt.xlabel('Is the area a food desert or not?')
plt.show()
'''