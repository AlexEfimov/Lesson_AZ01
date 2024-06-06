import pandas as pd
# Официальный ранг игроков в гольф по состоянию на апрель 2024
df = pd.read_csv('owgr_apr_2024.csv')
print(df.head())
print(df.info())
print(df.describe())

df_1 = pd.read_csv('dz.csv')
print(df_1.head())

group = df_1.groupby('City')['Salary'].mean()
print(group)
# Проверим изменится ли что нибудь, если предварительно выбросить все строки, где не определен город или зарплата
df_1r = df_1.dropna(subset= ['City', 'Salary'], inplace=False)
group1 = df_1r.groupby('City')['Salary'].mean()
print(group1)
# Поскольку ничего не поменялось, видимо метод mean отбрасывает такие данные автоматически