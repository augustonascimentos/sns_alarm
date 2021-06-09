from utils import logger
from utils.configs import Config
import pymysql
import sys


class Rds:
    instance = None

    def __init__(self):
        logger.info('Connecting with RDS')

        try:
            self.connection = pymysql.connect(
                host=Config.instance.RDS_HOST,
                user=Config.instance.RDS_USERNAME,
                password=Config.instance.RDS_PASSWORD,
                db=Config.instance.RDS_DB_NAME,
                port=Config.instance.RDS_PORT,
                cursorclass=pymysql.cursors.DictCursor,
                connect_timeout=10,
                read_timeout=25
            )
            Rds.instance = self
        except pymysql.MySQLError as err:
            logger.error('Could not connect to RDS instance.')
            logger.error(err)
            sys.exit()

    def execute(self, query, values=None):
        try:
            with self.connection.cursor() as cur:
                cur.execute(query, values)
                return cur

        except Exception as ex:
            logger.exception(ex)
            raise

    def commit(self):
        try:
            self.connection.commit()

        except Exception as ex:
            logger.exception(ex)
            raise

    def connection_close(self):
        try:
            self.connection.close()

        except Exception as ex:
            logger.exception(ex)
            raise


def init():
    Rds()
