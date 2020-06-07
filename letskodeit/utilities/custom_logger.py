import inspect
import logging

def customLogger(logLevel = logging.DEBUG):
    # Get the name of the class / method from where this method is being called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)
    
    #Creating the file handler to save the logs in a file
    fileHandler = logging.FileHandler("C:\\Users\\Manish Rawat\\git\\repository\\letskodeit\\Log\\Automation.log", mode ='a')
    fileHandler.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    
    logger.addHandler(fileHandler)
    return logger
