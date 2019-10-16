import pymongo

DATABASE_NAME = "db_ifpe"
COLLECTION_NAME = "customers"

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient[DATABASE_NAME]
mycol = mydb[COLLECTION_NAME]

mydict1 = { "name": "Valter", "address": "Recife" }
mydict2 = { "name": "Jorge", "address": "Olinda" }
mydict3 = { "name": "Matheus", "address": "Paulista" }

# Inserindo documentos um a um na collection de customers
x = mycol.insert_one(mydict1)
x = mycol.insert_one(mydict2)
x = mycol.insert_one(mydict3)