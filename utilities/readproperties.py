
import os
import configparser

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"//configurations//"+"config.ini")

class Readconfig:
    @staticmethod
    def getapplicationurl():
        url=config.get("commoninfo","baseurl")
        return url
    @staticmethod
    def getemail():
        emails=config.get("commoninfo","email")
        return emails
    @staticmethod
    def getpassword():
        pas=config.get("commoninfo","password")
        return pas


