import json
import os
from os.path import join, dirname

file = os.path.realpath(__file__)
base = dirname(dirname(file))
source = join(base, "source")
linkcheck_build = join(base, "build", "linkcheck")
output_file = join(linkcheck_build, "output.json")

with open(output_file, 'r', encoding = 'utf-8') as f:
	# sphinx produces multiple records instead of a list of records for broken links 
	records = [json.loads(i) for i in f.readlines()]

line = lambda: print("-" * 30)

cached_replacements = {}
replacements = []
for record in records:
	status = record['status']
	uri = record['uri']
	if status == "working":
		continue
	elif status == "unchecked":
		print("INFO: Url {!r} is not checked.".format(uri))
		continue
	elif status == "redirected":
		# check whether the redirect is permanent
		if record['code'] != 301:
			print("INFO: Passing {!r} since the redirection is not permanent.".format(uri))
			continue
		replace_with = record['info']
	elif status == "broken":
		try:
			replace_with = cached_replacements[uri]
		except KeyError:
			line()
			replace_with = input("The URL {!r} is broken, what do you want to change it with? You can also pass this question if you want to do nothing.\n > ".format(uri))
			line()
			if not replace_with:
				print("INFO: passing the URL")
				continue
	else:
		raise ValueError("ERROR: Unknown status: {!r}".format(status))
	
	# used for :target: special casing
	if replace_with == '.':
		replace_with = uri

	replacements.append((record, replace_with))

if len(replacements) == 0:
	print("All links are uptode, not any broken links.")

line()
for record, replacement in replacements:
	rst_file = join(source, record['filename'])
	uri = record['uri']

	with open(rst_file, 'r', encoding = "utf-8") as f:
		data = f.read()

	if uri not in data:
		alternative_uri = uri.split(":", 1)[0]
		if alternative_uri not in data:
			print("WARNING: Can't find the URL {!r} in file {}:{}. Might be about a :target: directive.".format(uri, rst_file, record['lineno']))
			continue
		uri = alternative_uri

	data = data.replace(uri, replacement)

	# special case :target: directives.
	if uri.startswith("_images") or uri.startswith("/images"):
		data = "\n".join([i for i in data.split("\n") if ":target:" not in i])

	with open(rst_file, 'w', encoding = "utf-8") as f:
		f.write(data)