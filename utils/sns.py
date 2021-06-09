import boto3


class Sns:

    def __init__(self):
        self.sns_client = None

    def sns_client_connection(self):
        self.sns_client = boto3.client('sns')
        return self.sns_client
