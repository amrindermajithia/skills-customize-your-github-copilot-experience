from typing import Optional, List
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


# In-memory store (starter scaffold)
_items: List[Item] = [Item(id=1, name="Sample", description="A sample item")]
_next_id = 2


@app.get("/items", response_model=List[Item])
def list_items():
    return _items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for it in _items:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")


class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
    global _next_id
    new_item = Item(id=_next_id, name=item.name, description=item.description)
    _items.append(new_item)
    _next_id += 1
    return new_item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global _items
    for i, it in enumerate(_items):
        if it.id == item_id:
            _items.pop(i)
            return {"detail": "deleted"}
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/")
def root():
    return RedirectResponse(url="/docs")


# To run locally:
# uvicorn assignments.fastapi_rest.starter_code:app --reload
