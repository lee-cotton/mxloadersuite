import requests
import base64

from mxls.logging.MXLogger import MXLogger

class ConnectionDetails(object):
    def setUrl(self, url):    
        self.url = url
    def getUrl(self):
        return self.url
    def setUserName(self, userName):    
        self.userName = userName
    def getUserName(self):
        return self.userName
    def setPassword(self, password):    
        self.password = password
    def getPassword(self):
        return self.password
        
class MXHttpRequest(object):

    def __init__(self, connectionDetails):
        self.connectionDetails = connectionDetails
        self.logger = MXLogger.getLogger()

    def sendRequest(self, objectStructure, request):

        url = self.connectionDetails.getUrl() + objectStructure

        self.logger.info('sendRequest to: ' + url)

        self.logger.debug('request content:')
        self.logger.debug(request)

        userPass = self.connectionDetails.getUserName() + ':' + self.connectionDetails.getPassword()
        
        credentials = base64.b64encode(userPass.encode())
        
        headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)', 'MAXAUTH' : credentials}
        
        req = requests.post(url, data=request, headers=headers)
        
        self.logger.info('Repsonse Status Code: ' + req.status_code)
        self.logger.debug(req.text)
        
        if req.status_code == 500:
            raise ValueError('Request Failed.')