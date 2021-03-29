# Example of ImportError
try:
    import sqlite4
except ImportError as error_msg:
    print(error_msg)


# try except with else
try:
    import sqlite3
except ImportError as error_msg:
    print(error_msg)
else:
    print('Import Successful!')


# try except with finally
try:
    import sys
    open('file.csv')
    # operations on file.csv
except (ImportError, OSError) as error_msg:
    print(error_msg)
finally:
    print('File related operations failed/complete.')


# Raising exceptions
try:
    if 'format'.upper() != 'JSON':
        raise Exception('Json file required..!')
except:
    pass

# User Defined exceptions
class SessionException(Exception):
    def __init__(self, message):
        self.message = None

try: 
    print('Calling API without passing session_id')
    raise SessionException('No Session Id')    
except SessionException as error_msg:
    print(error_msg)