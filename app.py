from fastapi import FastAPI, HTTPException
import json
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from fastapi.responses import RedirectResponse
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_methods=["*"],
    allow_headers=["*"],
)

client = MongoClient(
    'mongodb+srv://sebin:sebin123@cluster0.pkumg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client['my-links']
links = db['links']


@app.post('/')
def add_link(data: dict):
    links.insert_one(data)
    return 'saved'


@app.get('/')
def hello():
    return RedirectResponse("/docs")


@app.get('/my-links/{path}')
def get_page(path):
    l = links.find_one({"path": path}, {"_id": 0})
    if l is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return links.find_one({"path": path}, {"_id": 0})
