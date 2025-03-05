#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie, Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Debug session begins...")
    print(f'Companies:{session.query(Company).all()}')
    print(f'Devs: {session.query(Dev).all()}')
    print(f'Freebies: {session.query(Freebie).all()}')
    print("Debug session ends.")




    import ipdb; ipdb.set_trace()
    



