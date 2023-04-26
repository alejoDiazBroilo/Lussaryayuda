import pytest

from project import app

@pytest.fixture()
def app():
    app = app   