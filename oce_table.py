# 1. Import libraries

import pandas as pd

# 2. Load data from 2 Excel files

df_1 = pd.read_excel('C:/Users/caberoca/Danone/DACH Data and Digital Powerhouse - Data & Analytics Team/UseCaseFiles/MCE/MCE MMM Fortimel/Project/MMM_Fortimel/input_files/OCE data 2021-04.2023_TA.xlsx')
print(df_1)

df_2 = pd.read_excel('C:/Users/caberoca/Danone/DACH Data and Digital Powerhouse - Data & Analytics Team/UseCaseFiles/MCE/MCE MMM Fortimel/Project/MMM_Fortimel/input_files/OCE data 2021-04.2023_GroupCall.xlsx')
print(df_2)
