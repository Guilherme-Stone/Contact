from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from Database.database import Base

class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    phone: Mapped[str] = mapped_column(String(13))

    def __repr__(self):
        return f"<User {self.name}>,<Phone {self.phone}>,<Name {self.name}>"

    def change_number(self,number:str):
        self.phone = number
        return self