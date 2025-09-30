from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base, sessionmaker

DATAbAse_URL='sqlite//relacionamento.db'

engine=create_engine(DATAbAse_URL,echo=False,Future=True)

Base=declarative_base()

Sesssion=sessionmaker(bind=engine,future=True)




from sqlalchemy import create_engine,column,Integer,String,Float,ForeignKey
from sqlalchemy.orm import declarative_base,relationship,sessionmaker