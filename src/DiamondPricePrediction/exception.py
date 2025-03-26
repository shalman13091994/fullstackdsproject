import sys
import traceback

class CustomException(Exception):
    def __init__(self, errormessage):
        self.errormessage = errormessage
        self.error_trace = traceback.format_exc()  # Captures traceback as a string

    def __str__(self):
        return f"Error occurred:\n{self.error_trace[41:]}\n Error message: {self.errormessage}"

# script is imported into another module, the code inside if __name__ == "__main__": will not run automatically.
if __name__ == "__main__": 
    try:
        # a = 9 / 0  # This will raise ZeroDivisionError
        pass #add pass for importing to another python file
    except Exception as e:
        raise CustomException(e)

    
#in another python file will use like this 

# from CustomException import CustomException  # Import the class

# try:
#     # Simulating a data length mismatch error
#     data = [1, 2, 3]
#     if len(data) != 5:
#         raise ValueError("Data length mismatch error!")  # Example error
    
# except Exception as e:
#     raise CustomException(e)


