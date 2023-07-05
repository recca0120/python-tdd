from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass


class Record(Base):
    __tablename__ = "records"

    id: Mapped[int] = mapped_column(primary_key=True)


engine = create_engine("sqlite://", echo=True)


class SqlWriter:
    def write(self, csv):
        with Session(engine) as session:
            record = Record()
            session.add(record)
            session.commit()
