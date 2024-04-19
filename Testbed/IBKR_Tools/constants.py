import os
import time

LOCALHOST_IP = "127.0.0.1"
IB_GATEWAY_PORT = 4002
CURRENT_DATETIME = time.strftime("%Y%m%d-%H%M%S")
DEFAULT_CLIENT_ID = 1000  # this was used in examples, and presumably id's this app

# Constants for file path
BASE_DIRECTORY = "C:\\Users\\Gram\\IdeaProjects\\PYTHON\\api_ibkr_01\\"
FILE_NAME_TEMPLATE = "{timestamp}_scanner.xml"

# Constructing file path
scanner_file_name = FILE_NAME_TEMPLATE.format(timestamp=CURRENT_DATETIME)
FILE_PATH = os.path.join(BASE_DIRECTORY, scanner_file_name)
