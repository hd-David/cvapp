from sqlalchemy import Boolean, Column, MetaData, create_engine, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import sessionmaker,relation
from sqlalchemy.ext.declarative import declarative_base
import os , sqlalchemy

Base = declarative_base()

def connect_cloud_sql() -> sqlalchemy.engine.base.Engine:
    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL.create(
            drivername="postgresql",
            username='cvapp',
            password='/cvapp/1',
            host='10.3.96.3',
            database='cvapp_db'
        ))
    return pool

class Applicant(Base):
    __tablename__ = "applicant"
    id = Column(Integer, primary_key=True)
    email = Column(String(64))
    phone_number = Column(String(64))
    linked_in = Column(String(100))
    location = Column(String(64))
    name = Column(String(64))
    summary = Column(String(1000))

class Education(Base):
    __tablename__ = "education"
    id = Column(Integer, primary_key=True)
    school = Column(String(65))
    qualification = Column(String(100))
    duration = Column(String(64))
    applicant = relation('Applicant', backref='education')
    Applicant_id = Column(Integer, ForeignKey('applicant.id'))

class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True)
    skill_name = Column(String(100))
    score = Column(Integer)
    applicant = relation('Applicant', backref='skills')
    Applicant_id = Column(Integer, ForeignKey('applicant.id'))

class Work_experience(Base):
    __tablename__ = "work_experience"
    id = Column(Integer, primary_key=True)
    company = Column(String(65))
    role = Column(String(100))
    duration = Column(String(64))
    description = Column(String(500))
    applicant = relation('Applicant', backref='work_experience')
    Applicant_id = Column(Integer, ForeignKey('applicant.id'))

class Reference(Base):
    __tablename__ = "reference"
    id = Column(Integer, primary_key=True)
    name = Column(String(65))
    position = Column(String(100))
    phone_number = Column(String(64))
    email = Column(String(64))
    applicant = relation('Applicant', backref='references')
    Applicant_id = Column(Integer, ForeignKey('applicant.id'))
    
    
# database connection
def dbconnect():
    Base.metadata.create_all(connect_cloud_sql())
    Session = sessionmaker(bind=connect_cloud_sql())
    return Session()