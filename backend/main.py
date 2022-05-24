from fastapi.middleware.cors import CORSMiddleware
from bson.objectid import ObjectId
from pydantic import BaseModel
from datetime import timedelta
from fastapi import FastAPI
import pymongo
import redis
import json
import time

app = FastAPI()
client = pymongo.MongoClient('mongodb://root:root@db:27017/')
db = client['fast_test']
redis_client = redis.Redis(host='redis', port=6379, db=0)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name: str
    age: int
    email: str
    address: str
    zipCode: str
    sex: str


@app.get('/users')
def getUsers():
    if redis_client.exists('users_mongo'):
        return json.loads(redis_client.get('users_mongo'))

    collection = db['users']
    users_db = collection.find()
    users = []

    for i in users_db:
        i['_id'] = str(i['_id'])
        users.append(i)

    redis_client.setex(
        'users_mongo',
        timedelta(minutes=1),
        value=json.dumps(users)
    )

    return users


@app.get('/users/{id}')
def getUser(id: str):
    if redis_client.exists(f'user_{id}_mongo'):
        return json.loads(redis_client.get(f'user_{id}_mongo'))

    collection = db['users']
    user = collection.find_one({'_id': ObjectId(id)})

    if user is None:
        return {}

    user['_id'] = str(user['_id'])

    redis_client.setex(
        f'user_{id}_mongo',
        timedelta(minutes=1),
        value=json.dumps(user)
    )

    return user


@app.post('/user')
def addUser(user: User):
    collection = db['users']
    user_inserted = collection.insert_one(user.dict())

    return {"id": str(user_inserted.inserted_id)} | user.dict()
    

@app.put('/users/{id}')
def updateUser(id: str, user: User):
    collection = db['users']
    user_db = collection.find_one({'_id': ObjectId(id)})

    if user_db is None:
        return {}

    del user_db['_id'] 

    user_db = user_db | user.dict()
    collection.update_one({'_id': ObjectId(id)}, {"$set": user_db})
    redis_client.delete('users_mongo')

    return user


@app.delete('/users/{id}')
def deleteUser(id: str):
    collection = db['users']
    user_db = collection.find_one({'_id': ObjectId(id)})

    if user_db is None:
        return {}

    collection.delete_one({'_id': ObjectId(id)})
    redis_client.delete('users_mongo')

    return "ok"
