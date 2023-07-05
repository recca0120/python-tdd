# This is a sample Python script.
from ftp import Client
from sql_writer import SqlWriter, engine


def main(date):
    client = Client()
    csv = 'MEMBER_TRANS_SET_%s.csv' % date
    client.download(f'test_data/{csv}', csv)
    writer = SqlWriter(engine)
    writer.write(csv)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
