from datetime import date

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from sql_writer import SqlWriter, Base, Record


def test_write_csv_to_database():
    engine = create_engine("sqlite://", echo=False)
    Base.metadata.create_all(engine)

    csv = 'fixtures/ftp/test_data/MEMBER_TRANS_SET_20220417.csv'
    writer = SqlWriter(engine)
    writer.write(csv)

    session = Session(engine)
    stmt = select(Record).where(Record.id.is_(1))
    record = session.scalars(stmt).first()

    assert record.id == 1
    assert record.active_point == '000000'
    assert record.card_no == 'GID45362771301926'
    assert record.tran_seq == '08621671'
    assert record.dts == date.fromisoformat('2022-04-17')