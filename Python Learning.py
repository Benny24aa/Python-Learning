import pandas as pd

import numpy as np
from datetime import datetime

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


Diagnostics = Diagnostics.rename(columns={'HBName': 'HealthBoard' })

Diagnostics ['NumberOnList'] = pd.to_numeric(Diagnostics['NumberOnList'], errors='coerce')



#### Testing allocation of new column based on pre-set conditions giving out trues and falses based if condition is met
Diagnostics = Diagnostics.assign(
    Zero =Diagnostics['NumberOnList'] == 0,
    Normal =(Diagnostics['NumberOnList'] > 0) & (Diagnostics['NumberOnList'] <= 15000),
    Bad =(Diagnostics['NumberOnList'] > 15000) & (Diagnostics['NumberOnList'] <= 15500),
   Very_Bad =Diagnostics['NumberOnList'] > 15500
)

Diagnostics = Diagnostics.assign(
    Activity_Type=pd.Series(
        ['Zero', 'Normal', 'Bad', 'Very_Bad']
    ).where(
        [Diagnostics['Zero'],
         Diagnostics['Normal'],
         Diagnostics['Bad'],
         Diagnostics['Very_Bad']], 
        inplace=False
    )
)
