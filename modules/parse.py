import codecs

def parse(name, text, template):
	"""
	This is a JSON parser, which substitutes some variables into a template file.
		:param name: The name of the page.
		:param text: The body text for the page.
		:param template: The template to use for subsitution.
	"""
	json = { "title": name, "body": text }
	text = ''
	with codecs.open(template, encoding='utf-8') as f:
		text = f.read()
	q = ""
	recording = False
	replac = {}
	starts = []
	finish = []
	sfkeys = []
	length = 0
	for i in range(len(text)):
		if recording:
			if text[i]=='}' and not text[i-1]=="\\":
				recording = False
				replac[q] = json[q] if q in json else ""
				finish.append(i)
				sfkeys.append(q)
				length+=1
				q = ""
			else:
				q += text[i]
		elif text[i]=='{' and text[i-1]=="$":
			recording = True
			starts.append(i-1)
	newtxt = ""
	modifier = 0
	for i in range(length):
		newtxt += text[:starts[i]-modifier] + replac[sfkeys[i]]
		text    = text[(finish[i]-modifier)+1:]
		modifier = finish[i]+1
	newtxt += text
	return newtxt