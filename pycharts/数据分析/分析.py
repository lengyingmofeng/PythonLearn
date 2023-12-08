import pandas as pd
db = pd.read_csv(r'C:/消息/DXYArea.csv')
countryName = list(set(db['countryName']))
last_day = '2020-11-11'
to_day = '2020-11-12'
