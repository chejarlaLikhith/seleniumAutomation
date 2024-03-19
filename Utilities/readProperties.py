import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\lokes\\PycharmProjects\\seleniumAutomation\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('login information', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('login information', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('login information', 'password')
        return password

