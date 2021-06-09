import os


class Config:
    instance = None

    def __init__(self):
        if not Config.instance:
            self.RDS_HOST = os.getenv('RDS_HOST')
            self.RDS_USERNAME = os.getenv('RDS_USERNAME')
            self.RDS_PASSWORD = os.getenv('RDS_PASSWORD')
            self.RDS_DB_NAME = os.getenv('RDS_DB_NAME')
            self.RDS_DB_NAME = os.getenv('RDS_PORT', default='3306')

            Config.instance = self


def init():
    Config()
