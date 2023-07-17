from fastapi import FastAPI

from .models import Category, Entry
from .service import Service

app = FastAPI()
service = Service()


@app.on_event("startup")
def on_startup():
    service.init()


@app.get("/entries")
async def list_entries() -> list[tuple[Entry, Category]]:
    return service.list_entries()


@app.post("/entries")
async def create_entries(entry: Entry) -> Entry:
    return service.create_entry(entry)


@app.get("/categories")
async def list_categories() -> list[Category]:
    return service.list_categories()


@app.post("/categories")
async def create_category(category: Category) -> Category:
    return service.create_category(category)
