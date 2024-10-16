import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

# Define a data model using Pydantic
class Item(BaseModel):
    id: int
    name: str
    description: str = None

# In-memory "database"
items = []

def generate_sample_items(num_items: int):
    sample_names = [
        "Widget A", "Gadget B", "Thingamajig C", 
        "Doodad D", "Contraption E", "Appliance F", 
        "Device G", "Tool H", "Instrument I", "Equipment J"
    ]
    
    for i in range(num_items):
        item_id = i + 1
        item_name = random.choice(sample_names)
        item_description = f"This is a description for {item_name}."
        
        item = Item(id=item_id, name=item_name, description=item_description)
        items.append(item)

# Generate 10 sample items
generate_sample_items(10)


@app.get("/")
def index():
    return "Hello world"

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    # Check if item already exists
    for existing_item in items:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Item already exists")
    items.append(item)
    return item

@app.get("/items/", response_model=List[Item])
def read_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            return items.pop(index)
    raise HTTPException(status_code=404, detail="Item not found")

# Run the application with: uvicorn app:app --reload
if __name__ == "__main__":  
    uvicorn.run(app, host="0.0.0.0", port=8010)