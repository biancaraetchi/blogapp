from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Author(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    posts: List["Post"] = Relationship(back_populates="author")


class AuthorCreate(SQLModel, table=False):
    first_name: str
    last_name: str


class AuthorUpdate(AuthorCreate):
    """Basically, yeah"""


class Post(SQLModel, table=True):
    """This is the model connected to the database."""

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    subtitle: Optional[str]
    content: str
    views: int = 0
    sticky: bool = False
    author_id: Optional[int] = Field(default=None, foreign_key="author.id")
    author: Optional[Author] = Relationship(back_populates="posts")
    date_created: Optional[datetime] = Field(default_factory=datetime.utcnow)


class PostCreate(SQLModel, table=False):
    """This is the model, used mainly for serialization of inputs on create."""

    title: str
    content: str
    subtitle: Optional[str]
    author_id: Optional[int]
    sticky: Optional[bool]


class PostUpdate(PostCreate):
    """This is the model, used mainly for serialization of inputs on update."""

    views: Optional[int]
