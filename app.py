from fastapi import FastAPI, HTTPException
import json
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


# links: dict
# links = json.loads("""
# {   "sebinllas":
#     {
#         "b444c170-66a3-11ec-b05d-331e3156958b":
#         {
#             "url":"http://twitter.com/sebinllas",
#             "title":"twitter",
#             "description":"descripción twitter sebinllas",
#             "img":"https://i0.wp.com/hipertextual.com/wp-content/uploads/2012/06/twitter-bird-white-on-blue.jpg?fit=300%2C300&ssl=1"
#         },
#         "b444c171-66a3-11ec-b05d-331e3156958b":
#         {
#             "url":"http://facebook.com",
#             "title":"facebook",
#             "description":"descripción y ujdnsf f ajd iu wadc aiwjdc lorem eekner iofr efm ier fjermveriv rjeer jfner ev rejf ervsreoi erjkerjier cnweje ",
#             "img":"https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg"
#         },
#         "8376f130-678e-11ec-9dcd-7d707d933457":
#         {
#             "url": "https://udea.edu.co",
#             "title": "UdeA",
#             "description": "Mi universidad, es la mejor universidad en el departamento de Antioquia y una de las mejeros institu"
#         }
#     }
# }
# """)


test_links = {"sebinllas":
              {
                  "b444c170-66a3-11ec-b05d-331e3156958b":
                  {
                      "url": "http://twitter.com/sebinllas",
                      "title": "twitter",
                      "description": "descripción twitter sebinllas",
                      "img": "https://i0.wp.com/hipertextual.com/wp-content/uploads/2012/06/twitter-bird-white-on-blue.jpg?fit=300%2C300&ssl=1"
                  },
                  "b444c171-66a3-11ec-b05d-331e3156958b":
                  {
                      "url": "http://facebook.com",
                      "title": "facebook",
                      "description": "descripción y ujdnsf f ajd iu wadc aiwjdc lorem eekner iofr efm ier fjermveriv rjeer jfner ev rejf ervsreoi erjkerjier cnweje ",
                      "img": "https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg"
                  },
                  "8376f130-678e-11ec-9dcd-7d707d933457":
                  {
                      "url": "https://udea.edu.co",
                      "title": "UdeA",
                      "description": "Mi universidad, es la mejor universidad en el departamento de Antioquia y una de las mejeros institu"
                  }
              }
              }

client = MongoClient(
    'mongodb+srv://sebin:sebin123@cluster0.pkumg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client['my-links']
links = db['links']

# links.insert_one(test_links)


@app.post('/')
def add_link(data: dict):
    links.insert_one(data)
    return 'saved'


@app.get('/links')
def get_links():
    return links


@app.get('/my-links/{path}')
def get_page(path):
    # link = links.find_one({"path": id})
    # if id not in links.keys():
    #     raise HTTPException(status_code=404, detail="Item not found")
    l = links.find_one({"path": path}, {"_id": 0})
    if l is None:
        raise HTTPException(status_code=404, detail="Item not found")
    #print(l, type(l))
    return links.find_one({"path": path}, {"_id": 0})
