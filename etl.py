import pandas as pd
import os
import glob
from log import log_decorator
from timer import timer_decorator

# Função de extract que lê e consolida
@timer_decorator
@log_decorator
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


# Função que transforma o df adicionando o total de cada venda
@timer_decorator
@log_decorator
def transformar_dados(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']
    return df


# Função que salva em csv ou parquet
@timer_decorator
@log_decorator
def carregar_dados(df: pd.DataFrame, formatos: list[str]):
    for formato in formatos:
        if formato == 'csv':
            df.to_csv('vendas.csv', index=False)
        if formato == 'parquet':
            df.to_parquet('vendas.parquet', index=False)


# Função da pipeline que chama a ETL
@timer_decorator
@log_decorator
def pipeline(pasta_entrada: str, formato_saida: list[str]):
    dados = extrair_dados(pasta_entrada)
    dados_transformados = transformar_dados(dados)
    carregar_dados(dados_transformados, formato_saida)
