from loguru import logger
from azure.data.tables import TableServiceClient
import vars
import uuid


class CustomLogger:
    def __init__(self, level='INFO'):
        self.level = level.upper()
        self.setup_logger()

    def setup_logger(self):
        log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>"
        logger.remove()
        logger.add("bit-agua-logs.log", level="INFO", format=log_format, rotation="5 MB", compression="zip")

    def log_message(self, message, level='INFO'):
        if level.upper() not in ['DEBUG', 'INFO', 'SUCCESS', 'WARNING', 'ERROR', 'CRITICAL']:
            raise ValueError("Invalid log level. Supported levels are DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL.")
        logger.log(level.upper(), message)
        self.save_log_table(message, level)

  # envia para o azure table service
    def save_log_table(self, log_data, level):
        table_name = 'table_name'

        # Cria uma instância do serviço de tabela
        client = TableServiceClient.from_connection_string(conn_str=vars.storage_account_key)

        # Cria uma tabela se ela não existir
        table_client = client.get_table_client(table_name)

        # Adiciona uma entidade à tabela
        entity = {'PartitionKey': 'logs-api-flask', 'RowKey': str(uuid.uuid4()), 'Level': level, 'LogData': log_data}
        table_client.create_entity(entity)
