from sqlalchemy.engine import Engine
from sqlmodel import Session, SQLModel, create_engine, select

from .models import Category, Entry


class Service:
    engine: Engine

    def __init__(self, connection_string: str = "sqlite://") -> None:
        self.engine = create_engine(connection_string)

    def init(self):
        SQLModel.metadata.create_all(self.engine)

    def list_entries(self) -> list[tuple[Entry, Category]]:
        with Session(self.engine) as session:
            statement = (
                select(Entry, Category)
                .where(Entry.category_id == Category.id)
            )

            return session.exec(statement).all()

    def create_entry(self, entry: Entry) -> Entry:
        with Session(self.engine) as session:
            session.add(entry)
            session.commit()
            session.refresh(entry)

            return entry

    def list_categories(self) -> list[Category]:
        with Session(self.engine) as session:
            return session.exec(select(Category)).all()

    def create_category(self, category: Category) -> Category:
        with Session(self.engine) as session:
            session.add(category)
            session.commit()
            session.refresh(category)

            return category
