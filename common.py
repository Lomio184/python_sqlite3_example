import os
import uuid 

ERROR_CODE = -1
NORMAL_CODE = 0

def version_info_make():
    os.system("pip freeze > version_info.txt")

    return

def version_set():
    os.system("pip install -r > version_info.txt")
    return 

