
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('gasolina.csv')

sns.lineplot(data=df, x='dia', y='venda')
plt.xlabel('Dia')
plt.ylabel('Preço da Gasolina')
plt.title('Preço da Gasolina por Dia')

plt.savefig('gasolina.png')
    