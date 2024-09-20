import pandas as pd
import pandera as pa
from loguru import logger
from functools import wraps

schema = pa.DataFrameSchema({
    'Produto': pa.Column(pa.String),
    'Categoria': pa.Column(pa.String),
    'Quantidade': pa.Column(pa.Int64, pa.Check.ge(0)),
    'Venda': pa.Column(pa.Float64, pa.Check.ge(0), coerce=True),
    'Data': pa.Column(pa.DateTime, coerce=True)
})

def validate_schema(func):
    @wraps(func)
    def wrapper(df, *args, **kwargs):
        try:
            df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d')
            schema(df)
            logger.info(f'O DataFrame gerado é válido com schema:\n{df.dtypes}')
            return func(df, *args, **kwargs)
        except pa.errors.SchemaError as err:
            print('O DataFrame não é válido:', err)
            raise
    return wrapper
