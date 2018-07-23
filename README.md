# mxloadersuite
A tool to load multiple MXLoader spreadsheets

Installation Instructions.

1. Install Python3 (https://www.python.org/). 
   Note: For Windows distributions ensure that the option 'Add Python to PATH' is selected.

2. Open a command window terminal and change directory to 'mxloadersuite'.

3. Execute the following command to install dependancies:
   python setup.py develop

4. Modify the mxloadersuite.ini to specify the connection details to the Maximo application server.

5. Place MXLoader spreadsheets (.xlsm) in the 'content' directory.

6. Execute the following command to test the connection to the Maximo application server:
   python MXLoaderSuite.py -c TestConnection
   
7. Execute the following command to load the MXLoader spreadsheets in the 'content' directory
   python MXLoaderSuite.py -c Load