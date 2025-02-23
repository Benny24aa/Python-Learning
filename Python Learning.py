import pandas as pd
Diagnostics = pd.read_csv('diagnostics_by_board_september_2024.csv') #### Reading Data
Diagnostics = Diagnostics[Diagnostics['HBT'] == "S08000015"] ### Filtering

Diagnostics = Diagnostics[['MonthEnding', 'DiagnosticTestType', 'DiagnosticTestDescription', 'WaitingTime', 'NumberOnList']]
### Selecting columns required, just like select in R
