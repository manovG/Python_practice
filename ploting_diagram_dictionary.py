dic_stocks = {'PyhonDS':{'Open':12.87,'High':13.23,'Low':11.42,'Close':13.10},
        'PythonSoft':{'Open':23.54,'High':25.76,'Low':21.87,'Close':22.33},
        'Pythazon':{'Open':98.99,'High':102.34,'Low':97.21,'Close':100.065},
        'Pybook':{'Open':203.63,'High':207.54,'Low':202.43,'Close':205.24}}
                 




'''
Question 4
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it.
'''
import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame(dic_stocks)
print(df)

df.transpose().plot.bar()