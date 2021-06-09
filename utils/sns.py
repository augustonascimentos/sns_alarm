import boto3
from utils import logger


class Sns:

    def __init__(self):
        self.sns_client = None

    def sns_client_connection(self):
        logger.info('Initializing Sns client')
        self.sns_client = boto3.client('sns')
        return self.sns_client
