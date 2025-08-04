from fastapi import APIRouter, HTTPException
from app.v1.models.item import Item
from typing import List

router = APIRouter()

# in-memory store for example
items_db = {
    1: {"id": 1, "name": "Foo"},
    2: {"id": 2, "name": "Bar"},
}

@router.get("/items", response_model=List[Item])
def list_items():
    return list(items_db.values())

@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]