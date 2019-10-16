import pymongo

DATABASE_NAME = "db_ifpe"
COLLECTION_NAME = "customers"

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient[DATABASE_NAME]

# Exibindo os Databases ja criados
print(myclient.list_database_names())

# Verificando se existe o banco de dados informando (db_ifpe)
dblist = myclient.list_database_names()
if DATABASE_NAME in dblist:
  print("The database exists.")

# Verificando se existe a collection customers
collist = mydb.list_collection_names()
if COLLECTION_NAME in collist:
  print("The collection exists.")