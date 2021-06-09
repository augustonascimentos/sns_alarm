from databases.rds import Rds
from utils import logger


def process():
    logger.info('Initializing process!')
    alarm_1()


def alarm_1():
    query = """
        SELECT
            FORECASTED_DATE,
            PAYMENT_DATE
        FROM
            TABELA
        WHERE
            FORECASTED_DATE = CURDATE() 
            AND PAYMENT_DATE = ''
    """

    result = Rds.instance.execute(query=query)
    Rds.instance.commit()
    Rds.instance.close()
    if result:
        return


def alarm_2():
    query = """
        SELECT
            QUERY_EXAMPLE,
            QUERY_EXAMPLE
        FROM
            QUERY_EXAMPLE
        WHERE
            QUERY_EXAMPLE
    """

    result = Rds.instance.execute(query=query)
    Rds.instance.commit()
    Rds.instance.close()
    if result:
        return


def alarm_3():
    query = """
        SELECT
            QUERY_EXAMPLE,
            QUERY_EXAMPLE
        FROM
            QUERY_EXAMPLE
        WHERE
            QUERY_EXAMPLE
    """

    result = Rds.instance.execute(query=query)
    Rds.instance.commit()
    Rds.instance.close()
    if result:
        return