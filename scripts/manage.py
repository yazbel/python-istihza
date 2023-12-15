import os
from os.path import join
from functools import wraps
from color import error, warning, success, Colors
from difflib import SequenceMatcher
import sys

shared = join("..", "shared")
version_file = join("shared", "project_version.txt")

class App:
	def __init__(self):
		self.procedures = {}


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
			error(f"No argument is passed.")
			return
		if len(args) > 2:
			error(f"No more than two args is required.")
			return
		command, *arg = args
		try:
			procedure, expected_args = self.get_command(command)
		except ValueError:
			return

		if not arg:
			try:
				procedure()
			except TypeError as e:
				raise e
				error(f"{command!r} command requires an argument but none were given.")
			return

		arg = arg[0]
		if arg in expected_args:
			procedure(arg)
		else:
			if not expected_args:
				error(f"{command!r} command takes no argument.")
				return
			match = self.find_similar(arg, expected_args)
			error(f"{command!r} command have no argument named {arg!r}.")
			if match is not None:
				error(f"Did you perhaps meant {match!r}?")

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
				error(f"Did you perhaps meant {match!r}?")
			raise ValueError()

app = App()

@app.command("release")
def build(app, job = None):
	"Builds the docs, moves them to where they are needed and upgrades the version."
	import subprocess
	from io import StringIO

	def call(cmd, jobname):
		err = subprocess.PIPE
		out = subprocess.PIPE
		p = subprocess.run(cmd, shell=True, stdout=out, stderr=err)
		error(p.stderr.decode(), end = "")
		if not p.stderr:
			success(f"Built {jobname}.")
		else:
			warning(f"There were errors while building {jobname}.")

	print("Starting the build process.")
	p = call("make html", "HTML")
	p = call("make singlehtml", "HTML (single file)")
	p = call("make latexpdf", "PDF")
	p = call("make epub", "EPUB")

	if job is None:
		return

	if job == "release":
		app.procedures['version'](self, 'patch')
		import move_documents



@app.command()
def check_links(app):
	pass

@app.command("major", "minor", "patch", "downgrade")
def version(app, field):
	"Upgrades or downgrades the project version with respect to the specified argument."
	with open(version_file, "r") as f:
		versions = list(map(lambda x: x[:-1] if x.endswith("\n") else x, f))
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
	
@app.command(*app.procedures, "help")
def help(app, method = None):
	"Displays a help message for the given argument."
	if method is None:
		print("Possible arguments for the application:\n")
		for i in app.procedures:
			print(f"- {i:<20}" + app.procedures[i][0].__doc__)
	else:
		print(f"{method}:", app.procedures[method][0].__doc__)

if __name__ == "__main__":
	import sys
	args = sys.argv[1:]
	app.run(args)