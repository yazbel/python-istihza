import json
import os
from os.path import join, dirname
from color import error, success, warning

file = os.path.realpath(__file__)
base = dirname(dirname(file))
source = join(base, "source")
linkcheck_build = join(base, "build", "linkcheck")
output_file = join(linkcheck_build, "output.json")

try:
	with open(output_file, 'r', encoding = 'utf-8') as f:
		# sphinx produces multiple records instead of a list of records for broken links
		records = [json.loads(i) for i in f.readlines()]
except FileNotFoundError:
	error("ERROR: Run 'make linkcheck' first.")
	exit()


warning("If you do a mistake while replacing the urls you can just terminate the script before it ends (CTRL + C).\n")

cached_replacements = {}
replacements = []
broken = 0
for record in records:
	status = record['status']
	uri = record['uri']

	if status == "working":
		continue
	elif status == "unchecked":
		##print("INFO: Url {!r} is not checked.".format(uri))
		continue
	elif status == "redirected":
		# check whether the redirect is permanent
		if record['code'] != 301:
			##print("INFO: Passing {!r} since the redirection is not permanent.".format(uri))
			continue
		replace_with = record['info']
	elif status == "broken":
		try:
			replace_with = cached_replacements[uri]
		except KeyError:
			broken += 1
			print("File:\t" + record['filename'])
			print("url:\t" + uri)
			replace_with = input("The above url is broken, what do you want to change it with? You can also pass this question if you want to do nothing.\n > ")
			if replace_with and not replace_with.isspace():
				success("Replaced the link.\n\n")
			else:
				warning("Passing.\n\n")
				continue
	elif status == "ignored":
		continue
	else:
		raise ValueError("Unknown status for URL {!r}: {!r}".format(uri, status))

	# used for :target: special casing
	if replace_with == '.':
		continue

	replacements.append((record, replace_with))

if broken == 0:
	success("All links are uptodate, not any broken links.")
elif len(replacements) == 0:
	success(f"Didn't change any links out of {broken} broken ones.")
else:
	warning("Make sure you made no mistake and press Enter to proceed.")
	input()
	success(f"Changed {len(replacements)}/{broken} broken links.")

for record, replacement in replacements:
	rst_file = join(source, record['filename'])
	uri = record['uri']

	with open(rst_file, 'r', encoding = "utf-8") as f:
		data = f.read()

	if uri not in data:
		alternative_uri = uri.split(":", 1)[0]
		if alternative_uri not in data:
			warning("WARNING: Can't find the URL {!r} in file {}:{}. Might be about a :target: directive.".format(uri, rst_file, record['lineno']))
			continue
		uri = alternative_uri

	data = data.replace(uri, replacement)

	# special case :target: directives.
	if uri.startswith("_images") or uri.startswith("/images"):
		data = "\n".join([i for i in data.split("\n") if ":target:" not in i])

	with open(rst_file, 'w', encoding = "utf-8") as f:
		f.write(data)
