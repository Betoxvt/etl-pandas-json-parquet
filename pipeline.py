from etl import pipeline
from pathlib import Path

if __name__ == '__main__':
    # Define a pasta de entrada dentro da pasta raiz
    pasta_raiz = Path(__file__).parent
    pasta_entrada = pasta_raiz/'data'
    
    formato_saida = ['csv', 'parquet']  # Conforme decisão

    pipeline(pasta_entrada, formato_saida)
