"""
Name: Chocolate Py SQLite3 Data Module
Description: The default data provision module in Chocolate 2.
Author: Patrick Emery
Website: https://ssblur.com
Required:
	glob (glob) - Included with Python 3 by default.
		Used for easily fetching all files in this directory.
	SQLite3 Module (sqlite3) - Included with Python 3 by default.
		Used for data management. 
	Configuration Module (config) - Included in main release of Chocolate 2.
		Used for configuring your install.
"""

import sqlite3
from . import config
from . import data_provider

class sqlite3_data():
	"""
	This is the default data class included in Chocolate 2.
	This is based on SQLite3.
	"""
	data_types = {}
	def reserve( self, data_type, data_structure ):
		"""
		This reserves space for a specific data type. This simplifies data i/o using sqlite, allowing the module to ensure
			:param data_type: The name of the data type, a string.
			:param data_structure: A dictionary including all the variables the data type will need to store. 	
				Each key:value pair should include the name of the variable (as the key) and the type of the variable (as the value). This is for typed data storage, such as sql.
		"""
		cur.execute("""
				CREATE TABLE IF NOT EXISTS """+data_type+""" (
				sqlite3datakey text not null,
				"""+'\n,'.join([k+" "+self.sql_safe_type(v) for k, v in data_structure.items()])+""",
				PRIMARY KEY (sqlite3datakey)
				);""", {})
		self.data_types[data_type] = data_structure
	
	def set( self, type, name, data ):
		"""
		This adds or sets a new data entry of type type to the storage.
			:param type: The name of the data type (which should be reserved via the above command) of data you expect, a string.
			:param name: The name of the entry you are trying to set, a string.
			:param data: The data you wish to set for this entry, a dictionary wherein the keys are the names of variables and the values are the data to be set.
		"""
		data["sqlite3datakey"] = name
		cur.execute("replace into "+type+" ( sqlite3datakey, "+', '.join([k for k, v in self.data_types[type].items()])+") VALUES ( :sqlite3datakey, "+', '.join([":"+k for k, v in self.data_types[type].items()])+");", data)
	
	def get( self, type, name ):
		"""
		This gets the data of type type and entry name.
			:param type: The name of the data type, a string.
			:param name: The name of the entry you are trying to fetch, a string.
			:return: Returns the relevant data, a dictionary adhering to the format outlined when the data type was reserved.
		"""
		cur.execute("select * from "+type+" where sqlite3datakey=:name;", { "name" : name })
		return_data = {}
		fetch_data = cur.fetchone()
		keys = list(self.data_types[type])
		if not fetch_data:
			for i in keys:
				return_data[i] = self.data_types[type][i]()
			return return_data
		for i in range(len(keys)):
			return_data[keys[i]] = fetch_data[i]
		return return_data
	
	def save( self ):
		"""
		This function commits all modifications to the SQLite Database.
		"""
		sql.commit()
	
	def sql_safe_type( self, type ):
		"""
		This is a function used internally in order to turn data types into their SQL equivalents.
		"""
		if type == int:
			return "INTEGER"
		elif type == float:
			return "FLOAT"
		elif type == str:
			return "TEXT"
		elif type == list:
			return "MULTISET"
		elif type == bool:
			return "BIT"
		else:
			raise InvalidTypeException(type)
		
		
class InvalidTypeException(Exception):
	"""
	Exception raised when an incompatible type is fed to the sqlite3_data class' reserve function
	"""
	def __init__(self, type):
		"""
		The initialization call for this class.
			:param type: The invalid data type in question.
		"""
		self.message = "InvalidTypeException: Type '"+str(type)+"' is not supported by sqlite3_data."
		
global sql, cur
sql = sqlite3.connect(config.get_option("database_location", "wiki.db"))
cur = sql.cursor()

data_provider.set(sqlite3_data())