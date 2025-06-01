import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def getAppUrl():
        urlValue=config.get("login credential","URL")
        return urlValue

    @staticmethod
    def getAppUsername():
        UNValue = config.get("login credential", "username")
        return UNValue

    @staticmethod
    def getAppPassword():
        PWDValue = config.get("login credential", "password")
        return PWDValue

