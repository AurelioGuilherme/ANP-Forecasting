import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

sns.set_style("whitegrid")
sns.set_palette("coolwarm")
plt.rcParams.update({'font.size': 12})

def visualiza_serie_temporal(df: pd.DataFrame, x, y, produto=True):
    ax = plt.figure(figsize=(16, 6))
    ax = sns.lineplot(data=df, 
                      x=x, 
                      y=y, 
                      marker='o')
    if produto:
        ax.set_title(f'Preço Médio de Revenda em R$ - {str.capitalize(df['PRODUTO'].iloc[0])}',
                     fontsize=16, 
                     fontweight='bold')
    else:
        ax.set_title(f'Preço Médio de Revenda',
                     fontsize=16, 
                     fontweight='bold')
    ax.set_ylabel('PREÇO MÉDIO REVENDA', 
                  fontsize=14)
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("R$ {x:,.2f}")) 
    ax.set_xlabel('')
    plt.xticks(rotation=45) 

    plt.tight_layout()
    plt.show()

# Função para visualizar estacionaridade
def visualiza_estacionaridade(dados_serie):
    
    # Calcula média e desvio padrão móveis 
    rolling_mean = dados_serie.rolling(12).mean()
    rolling_std = dados_serie.rolling(12).std()
    
    # Plot
    fig = plt.figure(figsize = (12,6))
    time_series = plt.plot(dados_serie, label = 'Itens Vendidos')
    mean = plt.plot(rolling_mean, color = 'yellow', label = "Média Móvel")
    std = plt.plot(rolling_std, color = 'green', label = "Desvio Padrão Móvel")
    
    plt.legend(loc = 'best')
    plt.title("Visualizando a Estacionaridade")
    plt.xticks([]) 
    plt.yticks([]) 
    plt.show()