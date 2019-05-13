import pymongo
from pymongo import MongoClient
conn=pymongo.MongoClient("mongodb://localhost")
db=conn.pes
coll=database.emp
def insert:
	employeeId=input('Enter Employee ID:')
	employeeName=input('Enter name:')
	employeeAge=input('Enter Employee Age')
	employeeCountry=input('Enter Employee Country:')
	db.emp.insert_one(
		{
			"id":employeeId,
			"name":employeeName,
			"age":employeeAge,
			"country":employeeCountry
		})

n=input("Entering the number of documents needed")
for i in range(0,int(n)):
	insert()

for x in mycol.find({},{"_id":0,"name":1,"address":1,"age":1}):
	print(x)
	

mydoc=mycol.find({"age":{"gt":50}},{"_id":0,"name":1})
for x in mydoc:
	print(x)

mydoc=mycol.find({"address":"Banashankari"},{"_id":0,"name":1})
for x in mydoc:
	print(x)

# def display():
# 	db.customer.find()