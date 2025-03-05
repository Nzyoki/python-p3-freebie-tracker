from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from models import Base

def migrate():
    engine =create_engine('sqlite:///freebies.db')

    Base.metadata.create_all(engine)

    print("Migration completed successfullly!")

if __name__ == '__main__':
    migrate()