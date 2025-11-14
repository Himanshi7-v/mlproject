import sys 
def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error.detail.exc.info()
    filename=exc.tb.tb.frame.tb_code.co_filename
    error message ="error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
     filename,exc_tb.tb.lineno,str(error)
    return error_message 
    )
    class customExecption(Exception):
        def __init__(error,error_message,error_detail:sys):
# to inherit the init function or intilaize the init function of parent class Exception
            super.__init__(error_message)
            self.error_message = error_message_detail(error_message,error_detail=error_detail)
        def __str__(error):
            return self.error_message

