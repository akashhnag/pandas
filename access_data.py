import pandas as pd

coffee_data=pd.read_csv('coffee.csv')

print(coffee_data.sort_values('Units Sold'))