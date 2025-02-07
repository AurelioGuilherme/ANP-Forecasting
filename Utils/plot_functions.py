import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

sns.set_style("whitegrid")
sns.set_palette("coolwarm")
plt.rcParams.update({'font.size': 12})

def visualiza_serie_temporal(df: pd.DataFrame, x, y):
    ax = plt.figure(figsize=(16, 6))
    ax = sns.lineplot(data=df, 
                      x=x, 
                      y=y, 
                      marker='o')

    ax.set_title(f'Preço Médio de Revenda em R$ - {str.capitalize(df['PRODUTO'].iloc[0])}',
                 fontsize=16, 
                 fontweight='bold')

    ax.set_ylabel('PREÇO MÉDIO REVENDA', 
                  fontsize=14)
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("R$ {x:,.2f}")) 
    ax.set_xlabel('')
    plt.xticks(rotation=45) 

    plt.tight_layout()
    plt.show()
