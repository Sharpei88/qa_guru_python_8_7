import os
import pytest
from utils import TMP_PATH
import shutil


@pytest.fixture(scope='function')
def tmp_dir():
    if not os.path.exists(TMP_PATH):
        os.mkdir('tmp')

    yield

    shutil.rmtree(TMP_PATH, ignore_errors=True)