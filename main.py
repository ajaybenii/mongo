from fastapi import FastAPI, HTTPException
from models import Item
from database import collection
from bson import ObjectId

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI + MongoDB Atlas is working!"}

@app.post("/items/")
async def create_item(item: Item):
    result = await collection.insert_one(item.dict())
    return {"id": str(result.inserted_id), "message": "Item created"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    item = await collection.find_one({"_id": ObjectId(item_id)})
    if item:
        item["id"] = str(item["_id"])
        del item["_id"]
        return item
    raise HTTPException(status_code=404, detail="Item not found")
