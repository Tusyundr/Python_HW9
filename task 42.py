# Задача 42:
# Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd
df = pd.read_csv('california_housing_train.csv')
min_zone = df.loc[df.population < df.population.quantile(.25)]
print(min_zone.households.max())