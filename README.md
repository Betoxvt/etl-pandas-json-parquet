# ETL com Pandas, JSON e Parquet

1. Escolher a ferramenta de processamento: pandas

2. Escolher a ferramenta de qualidade: pandera é adequado para trabalhar com pandas

3. Salvar logs com loguru

etl.py

    Extract: ler os arquivos (.json) e concatenar
    Transform: criar uma nova coluna 'Total' = 'Quantidade' X 'Venda'
    Load: salvar o novo Data Frame (decidir por 2 caminhos, csv ou parquet)
    Obs.: para salvar em parquet com o pandas há que instalar o fastparquet

pipeline.py > vai chamar a pipeline

schema.py > validação do dataframe com panderas usando decorator

log.py > configurações e decorator para os logs

timer.py > decorador para medir o tempo de execução das funções