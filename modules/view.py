"""
Name: Chocolate Py Page View Module
Description: The default page viewing module included with Chocolate 2.
Author: Patrick Emery
Website: https://ssblur.com
Required:
	Markdown (markdown) - https://pypi.python.org/pypi/Markdown
		Used for formatting the page.
	JSON Page Parser (parse) - Included in default version of Chocolate 2
		Used for formatting page output.
"""
from . import modes, parse, data_provider, init
import markdown

global provider

def view( title, form ):
	"""
	This function displays the page for the client.
	This function does not otherwise manipulate data.
		:param title: The title of the page.
		:param form: The GET and POST data fed to the page.
		:return: Returns the body of the page.
	"""
	text = provider.get( "pages", title )["content"]
	return parse.parse(title, markdown.markdown(text if text else "This page does not exist yet. You can <a href='?page="+title+"&mode=edit'>Create</a> this page now!", output_format="html5"), "templates/wiki.template")

modes["view"] = view # Adds view as the callback for the "view" mode.

	
def setup():
	"""
	The setup function, used to establish global variables and such which will be used by this module.
	This function just grabs the active data provider and reserves the pages data type with one string item, "content".
	"""
	global provider
	provider = data_provider.get()
	provider.reserve( "pages", { "content" : str } )
	
init.append(setup)