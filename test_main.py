import os
import shutil

import pytest
from pytest_mock import MockFixture

from ftp import Client
from main import main
from sql_writer import Base, engine
from utils import assert_database_has


@pytest.fixture(autouse=True)
def after():
    yield
    if os.path.exists('MEMBER_TRANS_SET_20220417.csv'):
        os.unlink('MEMBER_TRANS_SET_20220417.csv')


def download(_obj, source, target):
    shutil.copy('fixtures/ftp/' + source, target)


def test_main(mocker: MockFixture):
    Base.metadata.create_all(engine)

    mocker.patch.object(Client, 'download', new=download)

    main('20220417')

    assert_database_has(1)
