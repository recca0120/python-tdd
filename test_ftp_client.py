import ftplib


class Client:
    def __init__(self, host, username, password, port=21):
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def login(self):
        client = ftplib.FTP()
        client.connect(host=self.host, port=self.port)

        try:
            return '230' in client.login(user=self.username, passwd=self.password)
        except ftplib.error_perm:
            return False


def test_login_successful(ftpserver):
    client = Client(host='127.0.0.1', username='benz', password='erni1')

    assert client.login() is True


def test_login_failed(ftpserver):
    client = Client(host='127.0.0.1', username='benz', password='erni2')

    assert client.login() is False
