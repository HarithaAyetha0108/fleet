from sqlmodel import create_engine, Session, SQLModel

SQLALCHEMY_DATABASE_URL = "sqlite:///./fleet_management.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SQLModel.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session
