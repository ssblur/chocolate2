import json

data = {}

with open("config.json","r") as f:
	data = json.load(f)
	f.close()
	print(data)

def write():
	with open("config.json","w") as f:
		json.dump(data, f)
		f.close()

def get_option( name, default ):
	if name in data:
		return data[name]
	else:
		data[name] = default
		return default