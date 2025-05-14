from fastapi import FastAPI, HTTPException
from models import Item
from database import collection
from bson import ObjectId

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    result = await collection.insert_one(item.dict())
    return {"id": str(result.inserted_id), "message": "Item created"}

@app.get("/pingdb")
async def ping_db():
    try:
        await collection.database.command("ping")
        return {"message": "MongoDB connection is working ✅"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
