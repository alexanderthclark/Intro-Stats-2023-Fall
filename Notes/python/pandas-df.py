import pandas as pd

atus_df = pd.read_csv("ATUS_activity_2019.csv")
other_df = pd.read_excel("helper.xlsx")

data = {'day' : ['Monday', 'Tuesday'], 
        'frosty_expenditure' : [0,2],
        'mcflurry_expenditure': [3,0]}
df = pd.DataFrame(data)