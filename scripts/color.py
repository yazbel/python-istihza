import os
from functools import wraps

# Enable colors on Windows systems
if os.name == "nt":
    os.system("")

# ANSI escape codes for colors and styles
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
    """
    Context manager to apply a color and style temporarily.
    """
    def __init__(self, color='', style=''):
        self.color = color
        self.style = style

    def __enter__(self):
        print(self.color + self.style, end="")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(END, end="")
        return False

def guard(f):
    """
    Decorator to ensure that ANSI reset (END) is applied
    even if an exception occurs.
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except BaseException as e:
            raise e
        finally:
            print(END, end="")
    return wrapper

def with_modifiers(*modifiers):
    """
    Decorator to apply colors/styles to the output of a function.
    """
    def decorator(f):
        @wraps(f)
        @guard
        def wrapper(*args, **kwargs):
            print(*modifiers, sep="", end="")
            return f(*args, **kwargs)
        return wrapper
    return decorator

@guard
def guarded_print(*args, **kwargs):
    """
    A safe print function that ensures ANSI reset.
    """
    print(*args, **kwargs)

@with_modifiers(Colors.RED)
def error(*args, **kwargs):
    """
    Print an error message in red.
    """
    print(*args, **kwargs)

@with_modifiers(Colors.GREEN)
def success(*args, **kwargs):
    """
    Print a success message in green.
    """
    print(*args, **kwargs)

@with_modifiers(Colors.YELLOW)
def warning(*args, **kwargs):
    """
    Print a warning message in yellow.
    """
    print(*args, **kwargs)

@with_modifiers(Styles.BOLD)
def bold(*args, **kwargs):
    """
    Print a message in bold.
    """
    print(*args, **kwargs)

@with_modifiers(Colors.MAGENTA)
def header(*args, **kwargs):
    """
    Print a header in magenta.
    """
    print(*args, **kwargs)

def _split_without_removing(text, delimiter):
    """
    Split text by a delimiter without removing the delimiter.
    """
    iterator = iter(text.split(delimiter))
    result = []
    try:
        result.append(next(iterator))
        while True:
            result.append(delimiter)
            result.append(next(iterator))
    except StopIteration:
        return result

def _split_multiple_without_removing(text, delimiters):
    """
    Split text by multiple delimiters without removing them.
    """
    fragments = [text]
    for delimiter in delimiters:
        temp = []
        for fragment in fragments:
            temp.extend(_split_without_removing(fragment, delimiter))
        fragments = temp
    return fragments

def modify_text(text, words, color='', replacement_rule=lambda x: x):
    """
    Modify parts of the text by applying colors and a replacement rule.
    """
    result = ""
    for fragment in _split_multiple_without_removing(text, words):
        if fragment in words:
            result += color + replacement_rule(fragment) + END
        else:
            result += fragment
    return result

def modified_print(text, color_mapping, replacement_rule=lambda x: x):
    """
    Print text with multiple words highlighted in specified colors.
    """
    for words, color in color_mapping.items():
        text = modify_text(text, words, color, replacement_rule=replacement_rule)
    guarded_print(text)

if __name__ == "__main__":
    # Example usage
    guarded_print(modify_text(
        modify_text("Hello world!", ["world"], Colors.GREEN + Styles.UNDERLINE),
        ["Hello"], Colors.BLUE + Styles.ITALIC
    ))
    modified_print("Colors here!", {
        ("lors", "he"): Colors.YELLOW,
        ("Co", "re!"): Colors.RED,
    })

