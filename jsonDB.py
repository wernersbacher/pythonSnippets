"""
	  This project was made for saving of a few data locally with json with key: value
	  It's in no way meant to be fast, reliable, threadsafe or well tested - it's only easy to use for some special cases.
	  Behaves a little bit like webbrowser's localStorage system
	"""
import json


class LocalData:
	"""
	saves some key: value pairs in a json file. you can pass dicts as values to have a better hierarchy.
	it's not threadsafe and it doesn't really do any exception handling.
	"""

	LOCAL_JSON_PATH = "localdata.json"  # path to json db
	ALLOW_ANY_KEY = True  # if this is True, any key found in the json gets read, if not, only those specified in createDB()
	AUTOSAFING_ENABLED = True  # if False, use LocalData.save() to write to filesystem

	def __init__(self):
		self.db = None
		# load from local or init empty db
		self._load()

	def createDB(self):
		return {}  # here you can specifiy default values for the db

	def set(self, key, value):
		self.db[key] = value
		if self.AUTOSAFING_ENABLED:
			self._save()
		return True

	def get(self, key):
		return self.db[key]

	def getCopy(self):
		"""Only meant for debugging"""
		return self.db.copy()

	def _load(self):
		"""tries to load a local json file as db, if not found or parsing error, create an empty one"""
		try:
			with open(self.LOCAL_JSON_PATH) as json_file:
				loadedDB = json.load(json_file)
				newDB = self.createDB()

				# if keys are found, overwrite existing keys, delete others
				for key, value in loadedDB.items():
					if key in newDB or self.ALLOW_ANY_KEY:
						newDB[key] = value

				self.db = newDB

		except BaseException as e:
			# print("Could not load local json db. Will create an empty one. REASON:")
			# print(e)

			# creating new database in error case
			self.db = self.createDB()


	def _save(self):
		with open(self.LOCAL_JSON_PATH, 'w+') as json_file:
			json.dump(self.db, json_file)


	def save(self):
		self._save()


if __name__ == "__main__":
	# some testing/ docu
	localdb = LocalData()
	localdb.set("my-key", "my-data-values")

	print(localdb.get("my-key"))
	# that's it, nothing more than that
