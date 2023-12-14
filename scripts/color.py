# see https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
import os
from functools import wraps

# System call to enable colors
if os.name == "nt":
    os.system("")

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def guard(f):
    @wraps(f)
    def g(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except Exception as e:
            print(Colors.END, end = "")
            raise e
    return g

@guard
def error(*args, **kwargs):
    print(Colors.FAIL, end = "")
    print(*args, **kwargs)
    print(Colors.END, end = "")

@guard
def success(*args, **kwargs):
    print(Colors.OKGREEN, end = "")
    print(*args, **kwargs)
    print(Colors.END, end = "")

@guard
def warning(*args, **kwargs):
    print(Colors.WARNING, end = "")
    print(*args, **kwargs)
    print(Colors.END, end = "")