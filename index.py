#!/usr/bin/python3
"""
Name: Chocolate Py 2
Description: An upgrade to the worst wiki ever.
Version: 2.0.0
Author: Patrick Emery
Website: https://ssblur.com
Required:
	Common Gateway Interface Module (cgi) - Included with Python 3 by default.
		Used to cleanly fetch GET and POST data for use in fetching the page, mode, and any additional information necessary.
	Chocolate Py Config Module (config) - Included with default build of Chocolate Py
		Used to access custom user-defined configuration tidbits.
"""

from modules import *
from modules import modes, init, data_provider
import sqlite3, cgi, codecs

def chocolate():
	"""
		The titular function.
		This is what runs all initialization functions, grabs the page name and mode, and saves the config and data provider.
	"""
	form = cgi.FieldStorage()
	
	print("Content-Type: text/html\n\n")
	
	for i in init:
		i()
	
	page = form["page"].value if "page" in form else config.get_option("default_page", "Main") # The Page Variable, in case one is not defined.
	mode = form["mode"].value if "mode" in form else config.get_option("default_mode", "view") # The Mode Variable, determines how the page is treated.
	
	for k, v in modes.items():
		if mode==k:
			print(v( page, form ))
	
	data_provider.get().save()
	config.write()

chocolate()

