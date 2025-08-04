from fastapi import APIRouter, HTTPException
from typing import List
from app.v2.models.item import Item

router = APIRouter()

# in-memory store with prices
items_db = {
    1: {"id": 1, "name": "Foo", "price": 9.99},
    2: {"id": 2, "name": "Bar", "price": 19.99},
}

@router.get("/items", response_model=List[Item])
def list_items():
    return list(items_db.values())

@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]