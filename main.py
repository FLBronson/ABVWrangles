import pandas as pd

#Read in the file
filein = pd.read_csv('data.csv')

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
usLA = filein['LA1and10'].value_counts()[1] #US Low Access
usLILA = filein['LILATracts_1And10'].value_counts()[1] #US Low Income and Low Access
usFL = filein['State'].value_counts()['Florida']  #Number of instances in FL
usFLLA = filein['State'].value_counts()['Florida'] & filein['LILATracts_1And10'].value_counts()[1] #Number of instances in FL that are low income/low access

usDUVAL = filein['County'].value_counts()['Duval County'] #Number of isntances of Duval County in the data
usDUVALFD = filein['County'].value_counts()['Duval County'] #

#Number of food deserts out of all data values
print('Number of low access food deserts in the United States (1mi Urban/10mi Rural):', usLA, 'out of', usTC)
print('That is roughly', '{:.0%}'.format(usLA/usTC), 'of the United States that is low access to supermarkets.\n')
print('Number of low access/low income areas in the United States (1mi Urban/10mi Rural):', usLILA, 'out of', usTC)
print('That is roughly', '{:.0%}'.format(usLILA/usTC), 'of the United States that is low access/low income to supermarkets.\n')
print('Number of low access/low income areas in Florida affected by food deserts:', usFLLA, '/', usFL)
print('That is roughly', '{:.0%}'.format(usFLLA/usFL), 'of Florida that is low access to supermarkets.\n')
print('Total Duval County areas:', usDUVAL, ' out of', usFL, 'Florida areas.')