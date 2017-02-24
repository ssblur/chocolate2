"""
Name: Chocolate Py Modules
Description: This file assists in importing all modules.
Author: Patrick Emery
Website: https://ssblur.com
Required:
	glob (glob) - Included with Python 3 by default.
		Used for easily fetching all files in this directory.
	Operating System Access Path Module (os.path) - Included with Python 3 by default.
		Used to fetch this folder's absolute path name, check if each potential include in the directory is a file, and gets the base name of the provided path for imports.
"""
############### Imports ###############
from os.path import dirname, basename, isfile
import glob
################# END #################


m = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in m if isfile(f)]
del m

modes = {} # The modes dictionary, which allows modules to run only when a certain mode is active.

init = [] # The database initialization list, which gives modules a chance to hook into the data provider and ensure all their data is properly initialized.

class data:
	"""
	Below is the variable for storing the data provider. This data provider should have the following functions, at least:
		reserve( type, data )
			This should reserve space for a specific data type. This may not be necessary for all data types, but is included for types such as sql.
			:param type: The name of the data type, a string.
			:param data: A dictionary including all the variables the data type will need to store. 	
				Each key:value pair should include the name of the variable (as the key) and the type of the variable (as the value). This is for typed data storage, such as sql.
		set( type, name, data )
			This should add or set a new data entry of type type to the storage.
			:param type: The name of the data type (which should be reserved via the above command) of data you expect, a string.
			:param name: The name of the entry you are trying to set, a string.
			:param data: The data you wish to set for this entry, a dictionary wherein the keys are the names of variables and the values are the data to be set.
		get( type, name )
			This should get the data of type type and entry name.
			:param type: The name of the data type, a string.
			:param name: The name of the entry you are trying to fetch, a string.
			:return: Returns the relevant data, a dictionary adhering to the format outlined when the data type was reserved.
		save()
			This should save the data accumulated. Usually only called by the core module.
	"""
	data_provider = None
	def set( self, d ):
		"""
		Sets the data provider.
			:param d: The new data provider.
		"""
		self.data_provider = d
	def get( self ):
		"""
		Gets the data provider.
		"""
		return self.data_provider
data_provider = data()