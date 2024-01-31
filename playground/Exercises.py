from typing import *
from datetime import datetime
import re

def foo(i: int) -> int:
  tup = (1, 2, 3)
  li = list(tup)
  a_set = { "a", 123, tup }
  a_dict = {
    "a": "a",
    "b": "b",
  }

  len(tup)
  "abc %s".format("ha")
  enumerate(a_dict)

  for v in a_dict:
    print(v)

  for i, v in enumerate(a_set):
    print(i, v)

  for i in range(0, 10):
    print(i)

  """
  Scan from the start
  """
  re.match("(w*)", "www.abc.com")
  """
  Scan through string looking for a match to the pattern, returning
  a Match object, or None if no match was found.
  """
  re.search("(w*)", "www.abc.com")


async def fooAsync() -> any:
  dt = datetime.now()
  dt.strftime()

  i = "123"
  match i:
    case 123:
      print(i)
    case "123":
      print(i)
    case _:
      print("default")

  return dt


class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

