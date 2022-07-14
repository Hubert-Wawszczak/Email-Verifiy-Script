
from dataclasses import dataclass
import logging


# ToDo add creating dir checker
class Logger():
    def __init__(self):
        logging.basicConfig(format='%(asctime)s; %(levelname)s: %(message)s',
                            datefmt='%Y-%m-%d; %H:%M:%S',
                            level=logging.DEBUG)
        self.logger = logging.getLogger()
        
    def close_logger(self):
        for hdlr in self.logger.handlers[:]:
            self.logger.removeHandler(hdlr)

    def log_message(self, message, flag = 1):
        """Append message to log file 
        Args:
            message (string): Message to save 
        """   
        message = message + ";"
        if flag == 1:
            self.logger.info(message)
        if flag == 2:
            self.logger.warning(message)
        if flag == 3:
            self.logger.error(message)
        if flag == 4:
            self.logger.critical(message)
        if flag == 5:
            self.logger.exception(message)
    
    
           
