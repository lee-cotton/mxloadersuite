# MXLoader Suite
A tool to automate the execution of multiple MXLoader spreadsheets.

## Getting Started


###Prerequisites
The MXLoader Suite tool requires Python 3 for it's execution.
Visit https://www.python.org/ and install the relevant distribution for your operating system

Note: For Windows distributions ensure that the option 'Add Python to PATH' is selected.

###Installation Instructions.
1. Open a command/terminal window and change directory to 'mxloadersuite'.

2. Execute the following command to install dependancies:
   python setup.py develop

3. Modify the mxloadersuite.ini to specify the connection details to the Maximo application server.

4 Place MXLoader spreadsheets (.xlsm) in the 'content' directory.

5. Execute the following command to test the connection to the Maximo application server:
   python MXLoaderSuite.py -c TestConnection

###Usage
The following command is used to load the MXLoader spreadsheets in the 'content' directory:

python MXLoaderSuite.py -c Load

The tool will load worksheets contained within an MXLoader spreadsheet in the order they appear (skipping the 'About' and 'Config' worksheets)
If a worksheet with the name 'Stop' is reached then it will skip all subsequent worksheets in that MXLoader spreadsheet file.

###Logging
By default information on the current activity will be logged to both the console and a log file.
This is determined by the mxloadersuite_logging.ini file


Refer to the following link for more information:
https://docs.python.org/3/howto/logging-cookbook.html