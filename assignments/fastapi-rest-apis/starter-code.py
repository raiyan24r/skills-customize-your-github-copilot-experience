from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI REST API Assignment")


class Item(BaseModel):
    id: int
    name: str
    description: str


# In-memory data for assignment practice.
items: list[Item] = [
    Item(id=1, name="Notebook", description="A ruled notebook"),
    Item(id=2, name="Pencil", description="HB pencil"),
]


@app.get("/items")
def get_items() -> list[Item]:
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", status_code=201)
def create_item(item: Item) -> Item:
    for existing in items:
        if existing.id == item.id:
            raise HTTPException(status_code=400, detail="Item ID already exists")
    items.append(item)
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item) -> Item:
    for index, existing in enumerate(items):
        if existing.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, str]:
    for index, existing in enumerate(items):
        if existing.id == item_id:
            del items[index]
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
