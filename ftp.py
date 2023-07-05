import ftplib

import config


class Client:
    connected = False

    def __init__(self, host=None, username=None, password=None, port=None):
        self.host = host if host is not None else config.ftp.get('host')
        self.username = username if username is not None else config.ftp.get('username')
        self.password = password if password is not None else config.ftp.get('password')
        self.port = port if port is not None else config.ftp.get('port')
        self.client = ftplib.FTP()

    def login(self):
        if self.connected is True:
            return True

        try:
            self.client.connect(host=self.host, port=self.port)
            self.connected = '230' in self.client.login(user=self.username, passwd=self.password)

            return self.connected
        except ftplib.error_perm:
            return False

    def download(self, source, target):
        self.login()

        with open(target, 'wb') as fp:
            return '226' in self.client.retrbinary(f'RETR {source}', fp.write)
