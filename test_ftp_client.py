import filecmp
import os

import pytest

from ftp import Client


@pytest.fixture(autouse=True)
def after():
    yield
    if os.path.exists('fixtures/MEMBER_TRANS_SET_20220417.csv'):
        os.unlink('fixtures/MEMBER_TRANS_SET_20220417.csv')


def test_login_successful(ftpserver):
    client = given_client()

    assert client.login() is True


def test_login_failed(ftpserver):
    client = given_client(password='erni2')

    assert client.login() is False


def test_download_file(ftpserver):
    client = given_client()
    source = 'test_data/MEMBER_TRANS_SET_20220417.csv'
    target = 'fixtures/MEMBER_TRANS_SET_20220417.csv'

    assert client.download(source, target) is True
    assert filecmp.cmp(ftpserver.server_home + '/' + source, target)


def given_client(password=None):
    client = Client(password=password)

    return client
