# to read the ini file we have a special class called config master

import configparser


config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():

    @staticmethod
    def getApplicationURL():
        url=config.get("common info","baseUrl")
        return url

    @staticmethod
    def getUName():
        uname = config.get("common info", "username")
        return uname

    @staticmethod
    def getPassword():
        passw = config.get("common info", "password")
        return passw

# common info is a section