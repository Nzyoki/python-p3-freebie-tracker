from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from models import Base

def migrate():
    engine =create_engine('sqlite:///freebies.db')

    print(f"Tables before migration:{Base.metadata.tables.keys()}")

    Base.metadata.create_all(engine)

    print(f"Tables after migration: {Base.metadata.tables.keys()}")

    print("Migration completed successfullly!")

if __name__ == '__main__':
    migrate()