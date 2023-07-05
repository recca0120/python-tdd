from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import Session

from sql_writer import engine, Record


def assert_database_has(_id):
    session = Session(engine)
    stmt = select(Record).where(Record.id.is_(_id))
    record = session.scalars(stmt).first()
    assert record.id == _id
    assert record.active_point == '000000'
    assert record.card_no == 'GID45362771301926'
    assert record.tran_seq == '08621671'
    assert record.dts == date.fromisoformat('2022-04-17')
