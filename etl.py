import pandas as pd
import os
import glob

# Função de extract que lê e consolida
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


# Função que transforma o df adicionando o total de cada venda
def transformar_dados(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']
    return df


# Função que salva em csv ou parquet
def carregar_dados(df: pd.DataFrame, formatos: list[str]):
    for formato in formatos:
        if formato == 'csv':
            df.to_csv('vendas.csv', index=False)
        if formato == 'parquet':
            df.to_parquet('vendas.parquet', index=False)


# Função da pipeline que chama a ETL
def pipeline(pasta_entrada: str, formato_saida: list[str]):
    dados = extrair_dados(pasta_entrada)
    dados_transformados = transformar_dados(dados)
    carregar_dados(dados_transformados, formato_saida)
