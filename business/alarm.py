from databases.rds import Rds
from utils import logger
from utils.sns import Sns


def process():
    logger.info('Initializing process!')
    alarm_1()
    alarm_2()
    alarm_3()


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

    if result:
        sns = Sns().sns_client_connection()
        sns.publish(PhoneNumber='+5521900000000', Message='Error Alarm 1')


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

    if result:
        sns = Sns().sns_client_connection()
        sns.publish(PhoneNumber='+5521900000000', Message='Error Alarm 2')


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
        sns = Sns().sns_client_connection()
        sns.publish(PhoneNumber='+5521900000000', Message='Error Alarm 3')
