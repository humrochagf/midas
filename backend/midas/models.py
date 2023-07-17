from datetime import date

from pydantic import condecimal
from sqlmodel import Field, SQLModel

Decimal = condecimal(max_digits=5, decimal_places=3)


class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str


class Entry(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str
    value: Decimal  # type: ignore
    date: date
    posted: bool = False

    category_id: int = Field(foreign_key="category.id")
