from utils import configs, logger
from business import alarm
from databases import rds


def main():
    configs.init()
    logger.init()
    logger.info('Initializing Alarm')
    rds.init()
    logger.info('Connection pool created')
    alarm.process()


def handler(event, context):
    main()
