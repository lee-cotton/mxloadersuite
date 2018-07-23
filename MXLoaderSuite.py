import getopt
import sys

from mxls.logging.MXLogger import MXLogger
from mxls import MXLoaderCommands
def main(argv):

      logger = MXLogger.getLogger()

      command = ''

      try:
            opts, args = getopt.getopt(argv,"hc:",["command="])
      except getopt.GetoptError:
            print ('MXLoaderSuite.py -c command')
            sys.exit(2)
      for opt, arg in opts:
            if opt == '-h':
                  print ('MXLoaderSuite.py -c <command>')
                  print ('commands:')
                  print ('TestConnection')
                  sys.exit()
            elif opt in ("-c", "--command"):
                  command = arg

      logger.info('Executing command: ' + command)

      try:
            if command == 'TestConnection':
                  MXLoaderCommands.testConnection()
            elif command == 'Load' :
                  MXLoaderCommands.loadPackage('mxloadersuite.ini')
      except Exception as err:
            logger.error(err)
            
if __name__ == "__main__":
      main(sys.argv[1:])