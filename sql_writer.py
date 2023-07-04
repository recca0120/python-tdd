import pandas
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass


class Record(Base):
    __tablename__ = "records"

    id: Mapped[int] = mapped_column(primary_key=True)
    active_point: Mapped[str] = mapped_column(String(30))
    base_point: Mapped[str] = mapped_column(String(30))
    card_no: Mapped[str] = mapped_column(String(30))
    clerk_no: Mapped[str] = mapped_column(String(30))
    cont_flg: Mapped[str] = mapped_column(String(30))
    cont_no: Mapped[str] = mapped_column(String(30))
    cust_type: Mapped[str] = mapped_column(String(30))
    data_date: Mapped[str] = mapped_column(String(30))
    data_time: Mapped[str] = mapped_column(String(30))
    dtldate: Mapped[str] = mapped_column(String(30))
    file_cnt: Mapped[str] = mapped_column(String(30))
    fk: Mapped[str] = mapped_column(String(30))
    gk: Mapped[str] = mapped_column(String(30))
    good_point: Mapped[str] = mapped_column(String(30))
    job_id: Mapped[str] = mapped_column(String(30))
    member_type: Mapped[str] = mapped_column(String(30))
    new_active_point: Mapped[str] = mapped_column(String(30))
    new_base_point: Mapped[str] = mapped_column(String(30))
    new_total_point: Mapped[str] = mapped_column(String(30))
    num_total: Mapped[str] = mapped_column(String(30))
    payment_no_max: Mapped[str] = mapped_column(String(30))
    payment_no_max_tamt: Mapped[str] = mapped_column(String(30))
    pos_no: Mapped[str] = mapped_column(String(30))
    rec_no: Mapped[str] = mapped_column(String(30))
    store_no: Mapped[str] = mapped_column(String(30))
    topup_point: Mapped[str] = mapped_column(String(30))
    total_point: Mapped[str] = mapped_column(String(30))
    total_sm_of_mny: Mapped[str] = mapped_column(String(30))
    tran_no: Mapped[str] = mapped_column(String(30))
    tran_seq: Mapped[str] = mapped_column(String(30))
    receipt_to: Mapped[str] = mapped_column(String(30))
    uni_no: Mapped[str] = mapped_column(String(30), nullable=True)


class SqlWriter:
    def __init__(self, engine):
        self.engine = engine

    def write(self, csv):
        columns = Record.__table__.columns.keys()[1:]

        df = pandas.read_csv(csv, encoding='utf-8', header=None, dtype=str, names=columns)
        with Session(self.engine) as session:
            data = {}
            for item in df.itertuples():
                for column in columns:
                    value = getattr(item, column)
                    data[column] = value.strip() if type(value) is str else value

                record = Record(**data)
                session.add(record)

            session.commit()
