import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
print(MONGO_URI)

# Connect to MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client["squareyards"]  # Your DB name from the URI
collection = db["items"]    # You can change this to your preferred collection
