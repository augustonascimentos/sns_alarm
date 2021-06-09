import logging
from datetime import datetime
from pytz import timezone, utc


def init():
    def brazilian_time(*args):
        utc_dt = utc.localize(datetime.utcnow())
        my_tz = timezone("America/Sao_Paulo")
        converted = utc_dt.astimezone(my_tz)
        return converted.timetuple()

    logging.Formatter.converter = brazilian_time

    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] [%(levelname)s] - %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S'
    )


def exception(message):
    logging.exception(message)


def error(message):
    logging.error(message)


def warn(message):
    logging.warning(message)


def info(message):
    logging.info(message)
