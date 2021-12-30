import pytest
from stuff.accum import Accumulator


@pytest.fixture
def accum():
    yield Accumulator()
    print("DONE")


def test_accum_init(accum):
    assert accum.count == 0


def test_accum_add_one(accum):
    accum.add()
    assert accum.count == 1


def test_accum_add_three(accum):
    accum.add(3)
    assert accum.count == 3


def test_accum_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2


def test_accum_cannot_set_count(accum):
    with pytest.raises(AttributeError, match=r'can\'t set attribute') as e:
        accum.count = 10


