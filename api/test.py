import pandas as pd

data_frame = pd.read_excel('D:/js-project/project-j/api/temp.xlsx')

temperatures = data_frame['Temperatures']

print(temperatures)