from sqlalchemy import ForeignKey, Column, Integer, String, MetaData,create_engine
from sqlalchemy.orm import relationship,sessionmaker,declarative_base
from sqlalchemy.orm import registry 

#create engine
engine =create_engine('sqlite:///freebies.db')
Session =sessionmaker(bind=engine)

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    #relationship with freebie
    freebies=relationship('Freebie',back_populates='company')

    #relationship with dev through Freebie
    devs=relationship('Dev',secondary='freebies',back_populates='companies',overlaps='freebies')

    def __repr__(self):
        return f'<Company {self.name}>'
    
    def give_freebie(self, dev,item_name,value):
        session=Session()
        new_freebie=Freebie(
            item_name=item_name,
            value=value,
            company=self,
            dev=dev
        )
        session.add(new_freebie)
        session.commit()
        session.close()
        return new_freebie
    @classmethod
    def oldest_company(cls):
        session=Session()
        oldest=session.query(cls).order_by(cls.founding_year).first()
        session.close()
        return oldest
    


class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())


    #relationship with Freebie
    freebies=relationship('Freebie',back_populates='dev')

    #relationship with company through Freebie
    companies=relationship('Company',secondary='freebies',back_populates='devs')



    def __repr__(self):
        return f'<Dev {self.name}>'
    

    def received_one(self,item_name):
        return any(freebie.item_name ==item_name for freebie in self.freebies)
    
    def give_away(self,recipient_dev,freebie):
        session=Session()
        if freebie in self.freebies:
            freebie.dev_id=recipient_dev
            session.commit()
            session.close()
            return True
        session.close()
        #else:
        return False
        
class Freebie(Base):
    __tablename__ = 'freebies'

    id =Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())

    dev_id=Column(Integer, ForeignKey('devs.id'))
    company_id=Column(Integer, ForeignKey('companies.id'))
     
     #relationship with Dev and company through freebie
    dev=relationship('Dev',back_populates='freebies')
    company=relationship('Company',back_populates='freebies')

    def __repr__(self):
     return f'<Freebie {self.item_name}>'
    
    def print_details(self):
        return f'{self.dev.name} owns a {self.item_name} from {self.company.name}'
