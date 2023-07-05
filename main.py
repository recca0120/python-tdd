# This is a sample Python script.
from ftp import Client
from sql_writer import SqlWriter


def main(date):
    client = Client()
    target = f'MEMBER_TRANS_SET_{date}.csv'
    client.download('test_data/' + target, target)

    writer = SqlWriter()
    writer.write(target)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
