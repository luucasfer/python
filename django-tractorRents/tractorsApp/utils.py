from setup import settings
from influxdb import InfluxDBClient
import logging

logger = logging.getLogger(__name__)


def influxConnection():
    client = InfluxDBClient(
                settings.INFLUXDB_HOST,
                settings.INFLUXDB_PORT,
                settings.INFLUXDB_USERNAME,
                settings.INFLUXDB_PASSWORD,
                settings.INFLUXDB_DATABASE,
                timeout=getattr(settings, 'INFLUXDB_TIMEOUT', 10),
                ssl=getattr(settings, 'INFLUXDB_SSL', False),
                verify_ssl=getattr(settings, 'INFLUXDB_VERIFY_SSL', True),
            )
    return client


