import pymongo
client = pymongo.MongoClient("mongodb+srv://prateek:pt302030@cluster0.gqu4fiu.mongodb.net/?retryWrites=true&w=majority")
db=client.test
print(db)
d={
    "name":"prateek","surname":"tripathi","occupation":"teaching"
}
d={
    "name":"prateek","surname":"tripathi","occupation":"teaching"}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)
