from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class WorkSpace(Base):
    __tablename__ = 'workspace'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    color: Mapped[str]

    user_phone = Column(String, ForeignKey('users.phone'))
    user = relationship("User", back_populates="workspaces")
    ingredients = relationship("Ingredient", back_populates="work_space")


class Ingredient(Base):

    __tablename__ = "ingredient"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    unit: Mapped[str]
    quantity: Mapped[int]

    work_space_id = Column(Integer, ForeignKey("workspace.id"))
    work_space = relationship("WorkSpace", back_populates="ingredients")
