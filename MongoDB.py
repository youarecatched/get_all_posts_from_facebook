#!/usr/bin/python
# -*- coding: utf-8 -*-
#import pymongo
from pymongo import MongoClient
from contextlib2 import contextmanager
import urllib.parse
class MongoDB():
	def __init__(self, database, username, password):
		self.database = urllib.parse.quote_plus(database)
		self.username = urllib.parse.quote_plus(username)
		self.password = urllib.parse.quote_plus(password)
		self.connection_firmware = MongoClient("mongodb://{}:{}@localhost/{}".format(self.username, self.password, self.database))

	def connect(self, collection):
		try:
			self.collection = urllib.parse.quote_plus(collection)
			#password = urllib.parse.quote_plus(self.password)
			#db = urllib.parse.quote_plus(self.database)
			self.dbinfo = self.connection_firmware[self.database][self.collection] # truy cap vao collection
			return self.dbinfo
		except Exception as e:
			print(e)
	def disconnect(self):
		self.connection_firmware.close()

	@contextmanager
	def open(self, collection):
			try:
				self.collection = urllib.parse.quote_plus(collection)
				self.dbinfo = self.connection_firmware[self.database][self.collection] # truy cap vao collection
				yield self.dbinfo
				self.connection_firmware.close()
			except Exception as e:
					print(e)

	
