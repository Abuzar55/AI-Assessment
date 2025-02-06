import sys

def error_message(error, error_detail: sys):
    _,_, exec_info = error_detail.exc_info()
    filename = exec_info.tb_frame.f_code.co_filename
    error_message_detail = "Error Occurred in script [{0}] line number [{1}] error message[{2}]".format(filename, exec_info.tb_lineno, str(error))
    return error_message_detail

class CustomExcetions(Exception):
    def __init__(self, error_message_detail, error_detail:sys):
        super().__init__(error_message_detail)
        self.error_message = error_message(error=error_message_detail, error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message