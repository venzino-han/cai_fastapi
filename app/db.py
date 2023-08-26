# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from config import settings

ENGINE = create_engine(
    settings.DATABASE_URL,
    echo=True,
    pool_recycle = 500,
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)


Base = declarative_base()
Base.query = session.query_property()
# Dependency
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

if __name__ == '__main__': 
    get_db()