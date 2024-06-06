import pandas as pd
# data = [1,2,3,4,5]
# series = pd.Series(data)
# print(series)
# data = {
#     'Name':['Alice', 'Bob', 'Roma','Anna'],
#     'Age':[23, 45, 17, 24],
#     'City':['New York', 'LA', 'Chicago', 'Moscow']
# }
#
# df = pd.DataFrame(data)
# print(df)

# df = pd.read_csv('World-happiness-report-2024.csv')
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df['Country name'])
# print(df.loc[56,'Healthy life expectancy'])
# df = pd.read_csv('hh.csv')
# df["Test"] = [new for new in range(29)]
# print(df)
# df.drop('Test', axis=1, inplace=True)
# print(df)
# df.drop(28, axis=0, inplace=True)

df = pd.read_csv('animal.csv')
# print(df)
# df.fillna(value=0, inplace=True)
# print(df)
group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)
