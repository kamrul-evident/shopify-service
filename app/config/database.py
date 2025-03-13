from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///./test.db")


def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()
