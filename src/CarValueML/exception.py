import os 
import sys
from src.CarValueML.logger import logging
import  src.CarValueML.exception as exception
def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in python script [{file_name}] at line no. [{exc_tb.tb_lineno}] with message[{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message,
            error_detail=error_detail
        )
        
    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        print(1/0)
    except Exception as e:
        raise CustomException(e, sys)