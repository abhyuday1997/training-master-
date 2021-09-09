# importing module
from pymongo import MongoClient
  
# creation of MongoClient
client=MongoClient()
  
# Connect with the portnumber and host
client = MongoClient('localhost', 27017)

#Creating a Database
db = client['datacampdb']

article = {"author": "Derrick Mwiti",
            "about": "Introduction to MongoDB and Python",
            "tags":
                ["mongodb", "python", "pymongo"]}
                
# Inserting a Document
print('************* Inserting single document************')
articles = db.articles
result = articles.insert_one(article)
print("First article key is: {}".format(result.inserted_id))
print(db.list_collection_names())

print('************* Inserting multiple document************')
article1 = {"author": "Emmanuel Kens",
            "about": "Knn and Python",
            "tags":
                ["Knn","pymongo"]}
article2 = {"author": "Daniel Kimeli",
            "about": "Web Development and Python",
            "tags":
                ["web", "design", "HTML"]}
new_articles = articles.insert_many([article1, article2])
print("The new article IDs are {}".format(new_articles.inserted_ids))

print('************* Displaying multiple document************')

for article in articles.find():
  print(article)
  
print('*************Return Some Fields Only************')
# 
for article in articles.find({},{ "_id": 0, "author": 1, "about": 1}):
  print(article)

# Sorting
print('*************sorting descending ************')
doc = articles.find().sort("author", -1)

for x in doc:
  print(x)