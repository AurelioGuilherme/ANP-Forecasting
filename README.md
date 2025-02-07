# ANP-Forecasting

![Python](https://img.shields.io/badge/Python-3.13.1%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.2.3-green)
![MLflow](https://img.shields.io/badge/MLflow-2.20.1-orange?logo=mlflow&logoColor=white)



 Este repositório apresenta um projeto de forecasting (previsão) aplicado aos preços médios de combustíveis no Brasil, utilizando técnicas de Machine Learning e modelos estatísticos para análise de séries temporais, também será utilizada ferramentas de MLOps para trackeamento, avaliação e melhoria dos modelos testados, juntamente com o uso de `Conformal Prediction` para validar as previsões estatisticamente. 
 
 Os dados utilizados são fornecidos pela Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP).

O objetivo é criar modelos preditivos que ajudem a entender a variação dos preços ao longo do tempo, fornecendo insights para análises estratégicas.

## Estrutura do Projeto

**Etapa 1: Extração dos Dados (ETL)**

Na primeira etapa, os dados foram extraídos diretamente da API da ANP, coletando informações semanais sobre os preços médios por estado. O código-fonte e mais detalhes desta fase podem ser encontrados no repositório:

🔗 [Primeira Etapa - Extração de Dados da API ANP](https://github.com/AurelioGuilherme/ANP-ETL.git)


**Etapa 2: Modelagem e Previsão (Este Repositório)**

Agora, nesta fase, o foco está em desenvolver modelos de Machine Learning para previsão de preços, permitindo uma análise mais aprofundada das tendências e variações ao longo do tempo.
