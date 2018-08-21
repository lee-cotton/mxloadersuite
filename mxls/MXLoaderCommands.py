import logging
import logging.config
import os

from configparser import ConfigParser
from os import chdir
from subprocess import call
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

def runscriptfile(connectionDetails, fileToLoad):
    logger = MXLogger.getLogger()

    logger.info('Executing runscriptfile command on:' + fileToLoad.name)

    chdir(connectionDetails.getMaximoHome())

    runScriptFie = os.path.join(connectionDetails.getMaximoHome() + 'internal' + 'runscriptfile.sh')
    call([runScriptFie, '-caviation -f' + fileToLoad.name])

def configdb(connectionDetails):
    chdir(connectionDetails)
    call(os.path.join(connectionDetails.getMaximoHome(), 'tools/maximo', 'configdb.sh'))

def loadFile(connectionDetails, fileToLoad):
    fileName = fileToLoad.name
    mxLoader = MXLoader(connectionDetails)

    if fileName.lower().endswith('.xlsm'):
        
        mxLoader.loadWorkBook(fileToLoad)
    elif fileName.lower().endswith('.dbc'):
        runscriptfile(connectionDetails, fileToLoad)  
    elif fileName.lower() == 'configdb':
        configdb(connectionDetails)  

def loadPackage(configFileName):
    
    logger = MXLogger.getLogger()

    config = ConfigParser()
    config.read(configFileName)

    serveraddress = config.get('Connection', 'serveraddress')
    userName = config.get('Connection', 'user')
    password = config.get('Connection', 'password')

    contentDirectory = config.get('Package','directory')

    maximoHome = config.get('Maximo', 'maximo-home')

    logger.info('Loading files from: ' + contentDirectory)

    path = Path(contentDirectory)

    if not path.exists():
        logger.info('Package directory: ' + contentDirectory + ' does not exist.')
        return

    connectionDetails = ConnectionDetails()
    connectionDetails.setUrl(serveraddress)
    connectionDetails.setUserName(userName)
    connectionDetails.setPassword(password)
    connectionDetails.setMaximoHome(maximoHome)

    #If there is a content.dict file then use this to determine the files to be loaded
    contentDictFile = Path(os.path.join(contentDirectory, 'content.dict'))

    if contentDictFile.exists():
        logger.info('Found content.dict file.')

        contentDict = []
        with open(contentDictFile,'r') as inf:
            contentDict = eval(inf.read())

        logger.debug('content.dict:' + str(contentDict))

        for folder in contentDict['content'].items():
            for contentFileName in folder[1]:
                contentFile = open(os.path.join(contentDirectory, folder[0], contentFileName), 'r')
                loadFile(connectionDetails, contentFile)

    else:    
        contentFiles = list(path.glob('**/*.*')) # Guaranteed to be in alphabetical order?

        for contentFile in contentFiles:
            loadFile(connectionDetails, contentFile)         
