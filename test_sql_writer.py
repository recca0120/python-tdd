from sql_writer import SqlWriter, Base, engine
from utils import assert_database_has


def test_write_csv_to_database():
    Base.metadata.create_all(engine)

    csv = 'fixtures/ftp/test_data/MEMBER_TRANS_SET_20220417.csv'
    writer = SqlWriter(engine)
    writer.write(csv)

    assert_database_has(1)
