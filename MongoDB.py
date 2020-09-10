#!/usr/bin/python
# -*- coding: utf-8 -*-
#import pymongo
from pymongo import MongoClient
from contextlib2 import contextmanager
import urllib.parse
class MongoDB():
	def __init__(self, database):
		self.database = urllib.parse.quote_plus(database)
		self.connection = MongoClient("mongodb://localhost:27017/{}".format(self.database))
	def connect(self, collection):
		try:
			self.collection = urllib.parse.quote_plus(collection)
			#password = urllib.parse.quote_plus(self.password)
			#db = urllib.parse.quote_plus(self.database)
			self.dbinfo = self.connection[self.database][self.collection] # truy cap vao collection
			return self.dbinfo
		except Exception as e:
			print(e)

	def disconnect(self):
		self.connection.close()

	@contextmanager
	def open(self, collection):
			try:
				self.collection = urllib.parse.quote_plus(collection)
				# print(self.connection[self.database].list_collection_names())
				self.dbinfo = self.connection[self.database][self.collection] # truy cap vao collection
				yield self.dbinfo
				self.connection.close()
			except Exception as e:
					print(e)

	
