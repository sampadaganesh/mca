import pymongo
from pymongo import MongoClient
# con = MongoClient() 

# other method are
conn = pymongo.MongoClient("mongodb://localhost")
# conn = MongoClient("IPaddress",27017)
# db = con.testdb

# second method is 
# db = client['testdb']

# my_coll = db.coll_name  here coll_name is collection name 
database = conn.pes
coll = database.mca

for i in range(10):
	coll.insert_one({"name":"ABC"})

docs = coll.find()

for i in docs:
	print(i)