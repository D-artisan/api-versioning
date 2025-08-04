from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    price: float  # new field in v2