import os
import shutil

import pytest
from pytest_mock import MockFixture

from ftp import Client
from main import main
from sql_writer import Base, engine
from utils import assert_database


@pytest.fixture(autouse=True)
def after():
    yield
    if os.path.exists('MEMBER_TRANS_SET_20220417.csv'):
        os.unlink('MEMBER_TRANS_SET_20220417.csv')


def download(obj, source, target):
    shutil.copy('fixtures/ftp/' + source, target)


def test_main(mocker: MockFixture):
    mocker.patch.object(Client, 'download', new=download)
    Base.metadata.create_all(engine)

    main('20220417')

    assert_database()

