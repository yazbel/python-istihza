import os
from os.path import join
from functools import wraps
from color import error, warning, success, Styles, Colors, modify_text
from difflib import SequenceMatcher
import sys
import subprocess
from threading import Thread, Event
from time import sleep
import webbrowser

root = os.path.abspath(".")
shared = join(root, "shared")
version_file = join("shared", "project_version.txt")
index_file = join(root, "docs", "index.html")

class App:
    def __init__(self):
        self.procedures = {}
        self.configurations = {
            "default": None,
        }

    def configure(self, **kwargs):
        invalid = set(kwargs) - set(self.configurations)
        if invalid:
            raise ValueError(f"The following are not valid configuration keys: {', '.join(invalid)}.")
        self.configurations.update(kwargs)

    def command(self, *cli_args):
        def util(f):
            @wraps(f)
            def g(*args, **kwargs):
                f(self, *args, **kwargs)
            self.procedures[g.__name__] = (g, cli_args)
            return g
        return util

    def run(self, args):
        if len(args) == 0:
            if self.configurations["default"] is None:
                error(f"No argument is passed.")
                return
            command = self.configurations["default"]
            arg = ()
        elif len(args) > 2:
            error(f"No more than two args are allowed.")
            return
        else:
            command, *arg = args

        try:
            procedure, expected_args = self.get_command(command)
        except ValueError:
            return

        if not arg:
            try:
                procedure()
            except TypeError:
                error(f"{command!r} command requires an argument but none were given.")
            return

        arg = arg[0]
        if arg in expected_args:
            procedure(arg)
        else:
            if not expected_args:
                error(f"{command!r} command takes no arguments.")
                return
            match = self.find_similar(arg, expected_args)
            error(f"{command!r} command does not have an argument named {arg!r}.")
            if match is not None:
                error(f"Did you perhaps mean {match!r}?")

    @classmethod
    def find_similar(cls, name, pool):
        matcher = SequenceMatcher()
        matcher.set_seq1(name.casefold())
        ratios = {}
        for p in pool:
            matcher.set_seq2(p.casefold())
            ratio = matcher.ratio()
            ratios[ratio] = p
        m = max(ratios)
        if m > 0.6:
            return ratios[m]
        else:
            return None

    def get_command(self, name):
        try:
            return self.procedures[name]
        except KeyError:
            match = self.find_similar(name, self.procedures)
            error(f"No command named {name!r}.")
            if match is not None:
                error(f"Did you perhaps mean {match!r}?")
            raise ValueError()

    @classmethod
    def create_status_animation(cls, style, msg):
        def status_animation():
            style(msg, end="", flush=True)
            dot = 1
            while True:
                if dot > 3:
                    style("\r" + msg + " " * dot + "\b" * dot, end="", flush=True)
                    dot = 1
                style(".", end="", flush=True)
                dot += 1
                if event.is_set():
                    style("\r" + " " * (len(msg) + dot - 1) + "\r", end="")
                    break
                sleep(0.5)

        event = Event()
        t = Thread(daemon=True, target=status_animation)
        t.start()

        def finish():
            event.set()
            t.join()

        return finish

    @classmethod
    def call(cls, cmd, jobname):
        stop_animation = cls.create_status_animation(print, f"Building {jobname}")

        p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stop_animation()

        stderr = p.stderr.decode()
        if stderr:
            error(stderr, end="")
            warning(f"There were errors while building {jobname}.")
            return False
        else:
            success(f"Built {jobname}.")
            return True

app = App()
app.configure(default="help")

@app.command("release", "dev", "all")
def build(app, job="debug"):
    """Builds the docs. Builds them in all available formats if [release] or [all] argument is given.
       * Increases the project version if [release] argument is given.
       * Opens the docs/index.html in browser if [dev] argument is given.
       * Moves them to where they are needed if [release] or [dev] argument is given."""
    
    # Perform version upgrade if needed
    if job == "release":
        version('patch')

    print("Starting the build process.")
    if not app.call("make html", "HTML"):
        return

    if job in ("release", "all"):
        if not app.call("make singlehtml", "HTML (single file)"):
            return
        if not app.call("make latexpdf", "PDF"):
            return
        if not app.call("make epub", "EPUB"):
            return

    if job in ("debug", "all"):
        return

    import move_documents
    if job == "dev":
        view()

@app.command()
def view(app):
    "Opens the docs/index.html in browser."
    webbrowser.open(index_file, new=0, autoraise=True)
    success("Opened the docs/index.html in browser.")
    
@app.command()
def checklinks(app):
    "Check the links and fix them manually."
    print("Checking the links.")
    if app.call("make linkcheck", "linkcheck"):
        import linkfix

@app.command("major", "minor", "patch", "downgrade")
def version(app, field="display"):
    """Upgrades or downgrades the project version with respect to the specified argument ([major], [minor], [patch] or [downgrade]).
       * Displays the current version if no argument is passed."""
    with open(version_file, "r") as f:
        versions = list(map(lambda x: x.strip(), f))

    if field == "display":
        return print("Project version:", versions[-1])

    if field == "downgrade":
        if len(versions) == 1:
            error("Can't downgrade when there is a single recorded version.")
            return
        versions.pop()
        success(f"Downgraded the version to {versions[-1]}.")
    else:
        version = list(map(int, versions[-1].split(".")))
        index = ("major", "minor", "patch").index(field)

        version[index] += 1
        for i in range(index + 1, 3):
            version[i] = 0
        version = ".".join(map(str, version))
        versions.append(version)
        success(f"Upgraded the version to {version}.")

    with open(version_file, "w") as f:
        f.write("\n".join(versions))

def highlight_arguments(procedure):
    doc = procedure[0].__doc__
    words = tuple(map(lambda x: f"[{x}]", procedure[1]))
    return modify_text(doc, words=words, color=Styles.UNDERLINE + Colors.CYAN, replacement_rule=lambda x: x[1:-1])

@app.command(*app.procedures, "help")
def help(app, method=None):
    """Displays a help message for the given argument."""
    if method is None:
        print("Valid arguments for the application:\n")
        for i in app.procedures:
            print(f"- {i:<20}" + highlight_arguments(app.procedures[i]))
            print()
    else:
        print(f"{method}:", highlight_arguments(app.procedures[method]))

if __name__ == "__main__":
    args = sys.argv[1:]
    try:
        app.run(args)
    except KeyboardInterrupt:
        print()
        warning("Received CTRL+C, shutting down.")
else:
    raise ImportError("This file is not supposed to be imported.")
