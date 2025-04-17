from sqlalchemy import Column, Integer, String, Date, Text, func
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column("id", Integer, primary_key=True)
    first_name = Column("first_name", String(50), nullable=False)
    last_name = Column("last_name", String(50), nullable=False)
    email = Column("email", String(100), nullable=False, unique=True)
    phone_number = Column("phone_number", String(20), nullable=False)
    birthday = Column("birthday", Date, nullable=False)
    additional_info = Column(Text)  # необов'язкове поле
    created_at = Column('created_at', DateTime, default=func.now())

    def __repr__(self):
        return f"<Contact(name={self.first_name} {self.last_name}, "\
                "email={self.email}, phone={self.phone_number}, "\
                "birthday={self.birthday})>"
