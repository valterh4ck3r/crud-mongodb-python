import pymongo

DATABASE_NAME = "db_ifpe"
COLLECTION_NAME = "customers"

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient[DATABASE_NAME]
mycol = mydb[COLLECTION_NAME]

mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x)