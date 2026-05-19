#this is a test app
from app import add


def test_add():
    result = add(2, 3)
    print("Result of add(2, 3):", result)


def bad_format():
  return 1
