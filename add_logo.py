import os


def change_div(file):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    old = """<div class='header'><a href='https://yazbel.com'>yazbel.com</a></div>"""
    new = "<div class='header'><a href='https://yazbel.com'><img src='./_images/logo.png'></a></div>"
    with open(file, "w", encoding="utf-8") as f:
        f.write(content.replace(old, new))


def main():
    for i in os.listdir("."):
        if i.endswith("html"):
            change_div(i)
