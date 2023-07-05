from datetime import date

import pytest
from sqlalchemy import select
from sqlalchemy.orm import Session

from sql_writer import SqlWriter, Base, engine, Record


def test_write_csv_to_database_failed_when_date_not_allowed():
    Base.metadata.create_all(engine)

    with pytest.raises(ValueError) as e:
        csv = 'fixtures/ftp/test_data/MEMBER_TRANS_SET.csv'
        writer = SqlWriter()
        writer.write(csv)


def test_write_csv_to_database():
    Base.metadata.create_all(engine)

    csv = 'fixtures/ftp/test_data/MEMBER_TRANS_SET_20220417.csv'
    writer = SqlWriter()
    writer.write(csv)

    session = Session(engine)
    stmt = select(Record).where(Record.id.is_(1))
    record = session.scalars(stmt).first()

    assert record.id is 1
    assert record.active_point == '000000'
    assert record.card_no == 'GID45362771301926'
    assert record.tran_seq == '08621671'
    assert record.dts == date.fromisoformat('2022-04-17')
