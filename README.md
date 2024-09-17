# ETL com Pandas, JSON e Parquet

Escolher a ferramenta de processamento (pandas)

Escolher a ferramenta de qualidade (pandera)

etl.py

    Extract: ler os arquivos (.json) e concatenar
    Transform: criar uma nova coluna 'Total' = 'Quantidade' X 'Venda'
    Load: salvar o novo Data Frame (decidir por 2 caminhos, csv ou parquet)

pipeline.py > vai chamar a pipeline

schema.py > validação do dataframe