# Задача 40
# Определить среднюю стоимость дома (median_house_value), 
# где кол-во людей от 0 до 500 (population).

import pandas as pd
df = pd.read_csv('california_housing_train.csv')
pop_fiv_hundred = df.loc[(0 < df.population) & (df.population < 500)]
print(pop_fiv_hundred.median_house_value.mean())
