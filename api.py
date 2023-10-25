from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter

from db import get_db
from models import (Author, AuthorCreate, AuthorUpdate, Post, PostCreate,
                    PostUpdate)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # Expose 'Content-Disposition' header
    expose_headers=["Content-Disposition"],
)

app.include_router(
    CRUDRouter(
        schema=Post,
        create_schema=PostCreate,
        update_schema=PostUpdate,
        db_model=Post,
        db=get_db,
    )
)

app.include_router(
    CRUDRouter(
        schema=Author,
        create_schema=AuthorCreate,
        update_schema=AuthorUpdate,
        db_model=Author,
        db=get_db,
    )
)
