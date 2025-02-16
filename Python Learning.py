import pandas as pd
Diagnostics = pd.read_csv('diagnostics_by_board_september_2024.csv')
Diagnostics = Diagnostics[Diagnostics['HBT'] == "S08000015"]
