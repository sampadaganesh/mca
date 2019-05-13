import pymongo
import math
import random

from pymongo import MongoClient

conn = pymongo.MongoClient("mongodb://localhost")

database = conn.pes
coll = database.mca

people = ["sampada","ganesh","raghu","priya","sudeep"]

for i in range(10):
	user_id=i;
	name=people[int(math.floor(random.random()*people))]
	number=math.floor(random.random()*100)
	x={"user_id":user_id,"name":name,"number":number};
	coll.inset(x);

docs=coll.find()
for i in docs:
	print(i)

# 2.
import pymongo
import math
import random

from pymongo import MongoClient

conn = pymongo.mongoclient("mongodb://localhost")

database = conn.pes
coll = database.mca

for i in range(10):
	coll.insert_one({"name":"Sampada"})

docs=coll.find()
for i in range(10):
	print(i)

# 3
import pymongo
import math
import random

from pymongo import MongoClient

conn = pymongo.mongoclient("MongoClient://localhost")

database = conn.pes
coll = database.mca

people = ["sampada","ganesh","raghu","priya","sudeep"]

for i in range(10):
	user_id:i;
	name=people[int(math.floor(random.random()*people))]
	number=math.floor(random.random()*100)
	x={"user_id":user_id,"name":name,"number":number};
	coll.inset(x);

insert()
try:
	docs=coll.find()
	for i in docs:
		print(i)
except Exception as e:
	print("Error trying to read collection:",type(e),e)
num=coll.find().count()
print(num)

# 4.
import pymongo
import math
import random

from pymongo import MongoClient

conn = pymongo.mongoclient("MongoClient://localhost")

database = conn.pes
coll = database.mca

coll.updateMany({},{'$set':{"name":"sampada"}})
docs=coll.find()
for i in range(10):
	print(i)
num=coll.find().count()
print("Total record updated are:")
print(num)

rec=coll.delete_Many({})
print("Total record deleted are:")
print(rec.eleted_count)

# 5.
import pymongo
import math
import random

from pymongo import MongoClient

conn = pymongo.mongoclient("MongoClient://localhost")

database = conn.pes
coll = database.mca

st={'name':"sampada","number":10}

coll.insert_one(st)

p={'name':"sampada"}
q={'_id':0,'name':1}

doc=coll.find(q,p)

for r in doc:
	print(r)
print(doc.count())

doc=coll.find()
for r in doc:
	print(r)
print(doc.count())

# 6.
import pymongo
import math
import random

from pymongo import MongoClient

conn = pymongo.mongoclient("MongoClient://localhost")

try:
	database = conn.pes
	coll = database.mca
	def add():
		people = ["sampada","ganesh","raghu","priya","sudeep"]
		for i in range(10):
			user_id:i;
			name=people[int(math.floor(random.random()*people))]
			number=math.floor(random.random()*100)
			x={"user_id":user_id,"name":name,"number":number};
			coll.inset(x);
	add()
except Exception as e:
	print("Error trying to read collection:",type(e),e)
num=coll.find().count()
print(num)

# 7.
import pymongo
import math
import random

from pymongo import MongoClient

conn = pymongo.mongoclient("MongoClient://localhost")

database=conn.pes
coll=database.emp

def insert():
	try:
		employeeID=input("Enter employee ID")
		employeeName=input("enter employee Name")
		employeeAge=int(input("Enter Age"))
		employeeCountry=input("enter country")
		db.emp.insert_one(
			{
				"id":employeeID,
				"Name":employeeName,
				"Age":employeeAge,
				"country":employeeCountry
			})
	except Exception as e:
		print(str(e))

n=input("Entering the number of documents needed")
for i in range(0,int(n)):
	insert()

# 8
import pymongo
import math
import random

from pymongo import MongoClient

conn = pymongo.mongoclient("MongoClient://localhost")

database=conn.pes
coll=database.customer
def insert():
		custID=input("Enter Customer ID")
		custName=input("Enter Customer Name")
		custAge=int(input("Enter Age"))
		custAddress=input("Enter Address")
		coll.insert_one(
			{
				"id":custID,
				"Name":custName,
				"Age":custAge,
				"country":custAddress
			})
n=input("Entering the number of documents needed")
for i in range(0,int(n)):
	insert()
print("All details of customers")
for x in coll.find({},{"_id":0,"name":1,"address":1,"age":1,}):
	print(x)

mydoc=coll.find({"age":{"$gte":50}},{"_id":0,"name":1})
print("all customers having an age greater than 50")
for x in mydoc:
	print(x)

add=input("Enter the address to be found")
'''print ("all cusomers staying in")&add'''
mydoc=coll.find({"address":add},{"_id":0,"name":1})
for i in mydoc:
	print(i)

c=coll.find({"address":add},{}).count()
print(c)

id=("Enter the id of the record to be deleted")
res=coll..find_one_and_delete({"id":id})
print(res)
mydoc=coll.find({},{"_id":0,"id":1,"name":1,"address":1,"age":1})
for x in mydoc:
	print(x)


import pymongo
import math
import random

from pymongo import MongoClient

conn = pymongo.mongoclient("MongoClient://localhost")

database=conn.pes
coll=database.employee


def insert():
		employeeID=input("Enter employee ID")
		employeeName=input("enter employee Name")
		employeeSalary=int(input("Enter Salary"))
		employeeDept=input("Enter Department")
		db.emp.insert_one(
			{
				"id":employeeID,
				"Name":employeeName,
				"Age":employeeSalary,
				"dept":employeeDept
			})
n=input("Entering the number of documents needed")
for i in range(0,int(n)):
	insert()
print("The documents inserted are")
for x in coll.find({},{"_id":0,"name":1,"salary":1,"dept":1,}):
	print(x)
pipe=[{'$group':{'_id':"$dept",'Salary_num':{'$sum':"$salary"}}}]
print("sum of salary of all employee working in the same depertment")
for x in coll.aggregate(pipeline=pipe):
	print(x)
pipe=[{'$group':{'_id':"null",'Salary_num':{'$sum':"$salary"}}}]
print("sum of salary of all employees")
for x in coll.aggregate(pipeline=pipe):
	print(x)
print("sum of salary of all employee working in the same depertment where salary is > 80000")
pipe=[{"$match":{'salary':{'$gt':80000}}},		+
{'$group':{'_id':"$dept",'Salary_num':{'$sum':"$salary"}}}]
for x in coll.aggregate(pipeline=pipe):
	print(x)

