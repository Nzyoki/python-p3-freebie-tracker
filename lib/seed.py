#!/usr/bin/env python3

# Script goes here!

from sqlalchemy import create_engine
from models import Company, Dev, Freebie, Base
from sqlalchemy.orm import sessionmaker


engine=create_engine('sqlite:///freebies.db')
Session=sessionmaker(bind=engine)
session=Session()

#clear existing data
session.query(Freebie).delete() 
session.query(Dev).delete()
session.query(Company).delete()
session.commit()

# Create companies
google=Company(name='Google',founding_year=1998)
microsoft=Company(name='Microsoft',founding_year=1975)
tesla=Company(name='Tesla',founding_year=2003)
meta=Company(name='Meta',founding_year=2015)

#Add companies to the session
session.add_all([google, meta, tesla, microsoft])
session.commit()

#create devs
bill_gates=Dev(name="Bill Gates")
mark_zuckerberg=Dev(name="Mark Zuckerberg")
larry_page=Dev(name="Larry Page")
elon_musk=Dev(name="Elon Musk")

#Add devs to the session
session.add_all([bill_gates, mark_zuckerberg, elon_musk, larry_page])
session.commit()

#Create freebies
# bill_gates.freebies.append(Freebie(item_name="Macbook Pro",value=10, company_id=microsoft.id))
# larry_page.freebies.append(Freebie(item_name="google pixel",value=5, company_id=google.id))
# elon_musk.freebies.append(Freebie(item_name="Tesla Model X", company_id=tesla.id))
# mark_zuckerberg.freebies.append(Freebie(item_name="games", value=8, company_id=meta.id))

freebies=[
    Freebie(item_name="Macbook Pro",value=10, company=microsoft, dev=bill_gates),
    Freebie(item_name="google pixel",value=5, company=google, dev=larry_page),
    Freebie(item_name="Tesla Model X",value=50, company=tesla, dev=elon_musk),
    Freebie(item_name="Games", value=8, company=meta, dev=mark_zuckerberg) 
]

#Add freebies to the session
session.add_all(freebies)
session.commit()

#Print test data
print(f"All companies: {session.query(Company).all()}")
print(f"All devs: {session.query(Dev).all()}")
print(f"All freebies: {session.query(Freebie).all()}")
print(f"Bill Gates' freebies: {session.query(Freebie).filter(Freebie.devs.any(Dev.name=='Bill Gates')).all()}")
print(f"Freebies for Google: {session.query(Freebie).filter(Freebie.companies.any(Company.name=='Google')).all()}")
session.close()




