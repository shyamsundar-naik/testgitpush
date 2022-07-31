import pymongo

von = pymongo.MongoClient("mongodb+srv://shyam:<password>@cluster0.xzmbj.mongodb.net/?retryWrites=true&w=majority")
db = von.test

print(db)