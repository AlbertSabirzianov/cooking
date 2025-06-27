from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class User(Base):
    __tablename__ = 'users'
    name: Mapped[str]
    phone: Mapped[str] = mapped_column(primary_key=True)
    address: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]

    workspaces = relationship("WorkSpace", back_populates="user")


