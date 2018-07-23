import logging
import logging.config

from configparser import ConfigParser
from pathlib import Path

from mxls.MXHttpRequest import ConnectionDetails
from mxls.MXHttpRequest import MXHttpRequest
from mxls.MXLoader import MXLoader 
from mxls.logging.MXLogger import MXLogger
 
def testConnection():

    logger = MXLogger.getLogger()

    config = ConfigParser()

    config.read('mxloadersuite.ini')

    serveraddress = config.get('Connection', 'serveraddress')
    userName = config.get('Connection', 'user')
    password = config.get('Connection', 'password')
    
    logger.info('Server Address: ' + serveraddress)

    data = '<QueryMXASSET xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.ibm.com/maximo" baseLanguage="EN" transLanguage="EN" maxItems="1"><MXASSETQuery><WHERE>1=0</WHERE></MXASSETQuery></QueryMXASSET>'
    objectStructure = 'MXASSET'

    connectionDetails = ConnectionDetails()
    connectionDetails.setUrl(serveraddress)
    connectionDetails.setUserName(userName)
    connectionDetails.setPassword(password)
      
    httpRequest = MXHttpRequest(connectionDetails)

    httpRequest.sendRequest(objectStructure, data) 

    logger.info('Connection successful.')

def loadPackage(configFileName):
    
    logger = MXLogger.getLogger()

    config = ConfigParser()
    config.read(configFileName)

    serveraddress = config.get('Connection', 'serveraddress')
    userName = config.get('Connection', 'user')
    password = config.get('Connection', 'password')

    contentDirectory = config.get('Package','directory')

    logger.info('Loading files from: ' + contentDirectory)

    path = Path(contentDirectory)

    files = list(path.glob('**/*.xlsm'))

    connectionDetails = ConnectionDetails()
    connectionDetails.setUrl(serveraddress)
    connectionDetails.setUserName(userName)
    connectionDetails.setPassword(password)
      
    mxLoader = MXLoader(connectionDetails)
    
    for file in files:
        mxLoader.loadWorkBook(file)
