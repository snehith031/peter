import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client["flask"]
collection=db["flak0"]

dic = [
    {"name":"raj","add":"highway to 1hell"},

]
x = collection.insert_many(dic)

#for x in collection.find({},{'_id': 0, 'name': 'name1', 'add': 'highway to hell'}):
#    print(x)

#for x in collection.find():
#    print(x)
#collection.delete_one({"name":"name1"})

collection.update_one({"name":"name1"},{"$set":{"name":"satay"}})

