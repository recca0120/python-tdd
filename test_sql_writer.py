import pytest

from sql_writer import SqlWriter, Base, engine
from utils import assert_database


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

    assert_database()
