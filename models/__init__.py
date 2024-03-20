#!/usr/bin/python3
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

# Determine storage type based on environment variable
if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

# Reload the storage
storage.reload()
