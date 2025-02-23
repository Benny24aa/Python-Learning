import pandas as pd


Diagnostics = pd.read_csv('diagnostics_by_board_september_2024.csv') #### Reading Data
Diagnostics = Diagnostics[Diagnostics['HBT'] == "S08000015"] ### Filtering

Diagnostics = Diagnostics[['MonthEnding', 'HBT','NumberOnList']]
### Selecting columns required, just like select in R


Diagnostics = Diagnostics.groupby(['HBT', 'MonthEnding'], as_index = False)['NumberOnList'].sum()
### Grouping By and Summing up Number on List Column Based on This

#### Creating Dataframe for join

HB_Look_Up = pd.DataFrame({'HBT':['S08000015'],
'HBName':['A&G']})

Diagnostics = pd.merge(Diagnostics, HB_Look_Up, how='left', on ='HBT') #### Using Pandas to join HBT to HB Name for test
