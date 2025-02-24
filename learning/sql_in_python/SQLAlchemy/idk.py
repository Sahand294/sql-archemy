from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

varieble = create_engine("postgresql://postgres:sahand91@127.0.0.1/archemy")
# engine = create_engine("sqlite:///example.db")
baseclass = declarative_base()
session = sessionmaker(bind=varieble)
session2 = session()

from sqlalchemy import Column


class User(baseclass):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    email = Column(String(999),unique=True,nullable=False)
    age = Column(Integer,nullable=True)

#new_user = User(name='sahand')
#session2.add(new_user)
#session2.commit()
baseclass.metadata.create_all(varieble)
get_users = session2.query(User).all()
for i in get_users:
    print(i.id,i.name)