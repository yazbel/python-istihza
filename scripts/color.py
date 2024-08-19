# see https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
# and https://stackoverflow.com/questions/2048509/how-to-echo-with-different-colors-in-the-windows-command-line
import os
from functools import wraps

# System call to enable colors
if os.name == "nt":
    os.system("")

class Colors:
    WHITE = '\033[97m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLACK = '\033[90m'

class Styles:
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'

END = '\033[0m'

class Modify:
    def __init__(self, color = '', style = ''):
        self.color = color
        self.style = style

    def __enter__(self):
        print(self.color + self.style, end = "")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(END, end = "")
        return False

def guard(f):
    @wraps(f)
    def g(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except BaseException as e:
            raise e
        finally:
            print(END, end = "")
    return g

def with_modifiers(*modifiers):
    def util(f):
        @wraps(f)
        @guard
        def g(*args, **kwargs):
            print(*modifiers, sep = "", end = "")
            f(*args, **kwargs)
        return g
    return util

@guard
def guarded_print(*args, **kwargs):
    print(*args, **kwargs)

@with_modifiers(Colors.RED)
def error(*args, **kwargs):
    print(*args, **kwargs)

@with_modifiers(Colors.GREEN)
def success(*args, **kwargs):
    print(*args, **kwargs)

@with_modifiers(Colors.YELLOW)
def warning(*args, **kwargs):
    print(*args, **kwargs)

@with_modifiers(Styles.BOLD)
def bold(*args, **kwargs):
    print(*args, **kwargs)

@with_modifiers(Colors.MAGENTA)
def header(*args, **kwargs):
    print(*args, **kwargs)

def _split_without_removing(text, delimeter):
    iterator = iter(text.split(delimeter))
    try:
        l = [next(iterator)]
        while True:
            i = next(iterator)
            l.append(delimeter)
            l.append(i)
    except StopIteration:
        pass
    return l

def _split_multiple_without_removing(text, delimeters):
    text = [text]
    for delimeter in delimeters:
        temp = []
        for t in text:
            temp.extend(_split_without_removing(t, delimeter))
        text = temp
    return text

def modify_text(text, words, color = '', replacement_rule = lambda x: x):
    t = ""
    for word in _split_multiple_without_removing(text, words):
        if word in words:
            t += color + replacement_rule(word) + END
        else:
            t += word
    return t

def modified_print(text, color_mapping, replacement_rule = lambda x: x):
    for words, color in color_mapping.items():
        text = modify_text(text, words, color, replacement_rule = replacement_rule)
    guarded_print(text)

if __name__ == "__main__":
    guarded_print(modify_text(modify_text("Hello world!", ["world"], Colors.GREEN + Styles.UNDERLINE), ["Hello"], Colors.BLUE + Styles.ITALIC))
    modified_print("Colors here!", {
        ("lors", "he"): Colors.YELLOW,
        ("Co", "re!"): Colors.RED,
        })