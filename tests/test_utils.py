from src.myproject.utils import greet
from src.myproject.newpo import Run_Length_Encoding


def test_greet():
    assert greet("Ann") == "Hello, Ann!"
    assert greet("So?") == "Hello, So?"
    assert Run_Length_Encoding([1, 1, 1, 2, 2, 3]) == [(1, 3), (2, 2), (3, 1)]
