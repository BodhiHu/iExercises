from typing import Self

# Decorator function to wrap a class as singleton
def singleton(cls):
  instances = {}
  def instantiator(*args, **kwargs):
    if cls not in instances:
      instances[cls] = cls(*args, **kwargs)
    return instances[cls]

  return instantiator


@singleton
class Foo:
  def __new__(cls, *args, **kwargs) -> Self:
    return super().__new__(cls, *args, **kwargs)

  def __init__(self, *args, **kwargs) -> None:
    return super().__init__(*args, **kwargs)


class SingletonCls:
  def __new__(cls, *args, **kwargs) -> Self:
    if not hasattr(cls, "_instance"):
      cls._instance = super().__new__(cls, *args, **kwargs)
    return cls._instance


class ReverseInt:
  """
  Reverse an integer: 123 -> 321
  """
  @staticmethod
  def reverse(num: int) -> int:
    num = int(num)
    ret = 0
    while True:
      tmp = int(num / 10)
      ret = ret * 10 + (num - tmp*10)
      num = tmp
      if num == 0:
        break
    return ret


def missingLetters(s):
  alphas = set("abcdefghijklmnopqrstuvwxyz")
  return alphas - set(s)

def numsOfSum(nums, sum):
  for n in nums:
    if sum - n in nums:
      return [ n, sum - n ]

def mostWord(s: str):
  words = s.split()
  freqs = {}
  _mostWord = None
  for word in words:
    if word not in freqs:
      freqs[word] = 0
    freqs[word] += 1

    if _mostWord == None:
      _mostWord = word
    else:
      if freqs[word] > freqs[_mostWord]:
        _mostWord = word

  return _mostWord

def numProcess(num):
  digits = list(str(num))
  evens = [], odds = []
  for d in digits:
    if int(d) % 2 == 0:
      evens.append(d)
    else:
      odds.append(d)
  odds.sort()
  evens.sort(reversed=True)
  return "".join(odds + evens)


if __name__ == "__main__":
  assert(Foo() is Foo())
