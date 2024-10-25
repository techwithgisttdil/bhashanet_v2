from datetime import datetime
import inspect
import os

# --------INFO LOG FUNCTION -----------##

def logs(message):
    # Get the frame of the caller
    caller_frame = inspect.currentframe().f_back
    # Get the line number from the frame
    line_number = caller_frame.f_lineno
    filepath = caller_frame.f_globals["__file__"]
    file_name = os.path.basename(filepath)
    file_name = str(file_name)
    line_number  = " [ "+str(line_number)+" ] "
    logdata = file_name + line_number +"-->" + message
    with open("message.logs", 'a',encoding='utf-8') as messagefile:
        messagefile.write(logdata)
        messagefile.write("\n")
        messagefile.close()
