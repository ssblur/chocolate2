"""
Name: Chocolate Py Page Edit Module
Description: The default page editing module included with Chocolate 2.
Author: Patrick Emery
Website: https://ssblur.com
Required:
	The type 'pages' must be reserved with one value, String 'content'. This action is performed by default in the 'view' module.
	Markdown (markdown) - https://pypi.python.org/pypi/Markdown
		Used for formatting in the "save" mode.
	JSON Page Parser (parse) - Included in default version of Chocolate 2
		Used for formatting page output.
"""

from . import modes, init, data_provider, parse
import markdown

global provider

def setup():
	"""
	The setup function, used to establish global variables and such which will be used by this module.
	This function just grabs the active data provider.
	"""
	global provider
	provider = data_provider.get()

init.append(setup) # Registers setup() as an initialization function.
	
def edit( title, form ):
	"""
	This function provides the editor to the client.
	This function does not otherwise manipulate data.
		:param title: The title of the page.
		:param form: The GET and POST data fed to the page.
		:return: Returns the body of the page.
	"""
	return parse.parse(title, provider.get( "pages", title )["content"], "templates/edit.template")

modes["edit"] = edit # Registers edit as the callback function for "edit" mode

def save( title, form ):
	"""
	This function saves data fed to it by the edit page on the client.
	This function pushes data based on the default page scheme, placing "content" into "pages"
		:param title: The title of the page.
		:param form: The GET and POST data fed to the page.
		:return: Returns the body of the page.
	"""
	if "data" in form:
		data = form["data"].value.replace("<","&lt;").replace(">","&gt;")
		provider.set( "pages", title, {"content" : data} )
		return parse.parse(title, markdown.markdown(data, output_format="html5"), "templates/wiki.template") 
	else:
		text = provider.get( "pages", title )["content"]
		return parse.parse(title, markdown.markdown(text, output_format="html5"), "templates/wiki.template") 

modes["save"] = save # Registers save as the callback function for "save" mode
