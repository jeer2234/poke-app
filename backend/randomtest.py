from pymongo import MongoClient
from random import randint

client = MongoClient("mongodb+srv://javier2234:7jzUUZXvFpon0q7Y@cluster0.bpm8m.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",port=27017)
db=client.pokedata


trainer = db.trainers.find({'pokemons': "raticate"})



print(trainer)
