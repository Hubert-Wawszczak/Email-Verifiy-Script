from src.logger import Logger



class ServicesClass():
    
    __logger_obj = None
       
    @classmethod    
    def get_logger(cls): 
        """Get or create Logger objects

        Returns:
            [Logger]: Return Logger object
        """
        if(not cls.__logger_obj):
            cls.__logger_obj = Logger()
        return cls.__logger_obj
    