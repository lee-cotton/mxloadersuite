import logging
import logging.config

class MXLogger(object):

    mxLogger = None

    @staticmethod
    def configureLogger():

        loggerDict = []
        with open('mxloadersuite_logging.ini','r') as inf:
            loggerDict = eval(inf.read())

        logging.config.dictConfig(loggerDict)

        return logging.getLogger('default')

    @staticmethod
    def getLogger():
        if MXLogger.mxLogger == None:
            MXLogger.mxLogger = MXLogger.configureLogger()

        return MXLogger.mxLogger
