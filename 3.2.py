import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('prices_cleaned.csv')

df['Price'] = df['Price'].str.replace(' ', '').astype(int)

mean_price = df['Price'].mean()
print(f'Средняя цена: {mean_price:.2f}')


plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=15)

plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.grid()
plt.show()