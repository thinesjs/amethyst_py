import configparser
import random


class Config:
    def __init__(self, configFile):
        self.configFile = configFile
        self.config = configparser.ConfigParser()

    def readConfig(self):
        self.config.read(self.configFile)

    def getData(self, header, key):
        return self.config[header][key]

    def getApiKey(self):
        return self.config['OPTIONS']['API_KEY']

    def getFormsURL(self):
        return self.config['ENDPOINTS']['FORMS_URL']

    def getMaxAttempt(self):
        return self.config['OPTIONS']['MAX_ATTEMPT']

    def getRetryInterval(self):
        return self.config['OPTIONS']['RETRY_INTERVAL']

    def getRandApiKey(self):
        api_keys = (self.config['OPTIONS']['API_KEY']).split(',')
        return random.choice(api_keys)