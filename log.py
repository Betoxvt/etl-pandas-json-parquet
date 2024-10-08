from loguru import logger
from sys import stderr
from functools import wraps

# Removendo os handlers existentes para evitar duplicação
logger.remove()

# Configuração do logger para stderr (que mostra tipo print)
logger.add(
    sink=stderr,
    format='{time} <r>{level}</r> <g>{message}</g> {file}',
    level='INFO'
)

# Configuração do logger para arquivo de log
logger.add(
    'meu_arquivo_de_logs.log',
    format='{time} {level} {message} {file}',
    colorize=True,
    level='INFO',
    rotation='2 MB',
    compression='gz',
    diagnose=False  # Evita vazamento de dados
)

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f'Chamando função {func.__name__} com args:\n{args}\nE kwargs:\n{kwargs}')
        try:
            result = func(*args, **kwargs)
            logger.info(f'Função {func.__name__} retornou:\n{result}')
            return result
        except Exception as e:
            logger.exception(f'Exceção capturada em {func.__name__}: {e}')
            raise  # Re-lança a exceção para não alterar o comportamento do decorador
    return wrapper
