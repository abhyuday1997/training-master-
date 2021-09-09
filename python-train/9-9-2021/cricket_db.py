# importing module
from pymongo import MongoClient
  
# creation of MongoClient
client=MongoClient()
  
# Connect with the portnumber and host
client = MongoClient('localhost', 27017)
  
db = client['cricketdb']

from mongoengine import *
connect('cricketdb', host='localhost', port=27017)

class Player(Document):
    name = StringField(required=True)
    team = StringField(max_length=30)
    age = IntField(max_length=30)
    matches = StringField(max_length=30)
    
    def fun(self):
        print("I'm a", self.name)
        print("I'm a", self.team)
	
    
    
user1 = Player(name="sachin", team="India", age="30",matches='150')
user2 = Player(name="Richards", team="WestIndies", age="35",matches='120')
user3 = Player(name='Kapil Dev', team = 'India', age = '34', matches = '130')
user1.save()
user2.save()
user3.save()
print(user1.id, user1.name, user1.team, user1.age)
print(user2.id, user2.name, user2.team, user2.age)
