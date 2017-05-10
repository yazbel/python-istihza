import os

def walk_up(bottom):
	""" 
	from https://gist.github.com/1098474
	"""

	bottom = os.path.realpath(bottom)

	try:
		names = os.listdir(bottom)
	except Exception as e:
		print(e)
		return

	dirs, nondirs = [], []
	for name in names:
		if os.path.isdir(os.path.join(bottom, name)):
			dirs.append(name)
		else:
			nondirs.append(name)

	yield bottom, dirs, nondirs

	new_path = os.path.realpath(os.path.join(bottom, '..'))
	
	if new_path == bottom:
		return

	for x in walk_up(new_path):
		yield x
