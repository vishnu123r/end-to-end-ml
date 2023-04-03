import sys
import logging

def error_message_detail(error_message, error_detail:sys):
    """
    Returns a string with error message and the file and line in which it occurs
    """
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error = f"Error occured in python script name [{file_name}] line number [{line_number}] error message[{str(error_message)}]"
    
    return error
    
class CustomException(Exception):
    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message)
        self.error=  error_message_detail(error_message, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
    
    
if __name__ == '__main__':
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)