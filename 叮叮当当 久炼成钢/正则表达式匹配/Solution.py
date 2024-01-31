class Solution:
  def __init__(self) -> None:
    pass

  # "abbcd", "ab*.*d"
  @staticmethod
  def isMatch(s: str, p: str) -> bool:
    if len(p) == 0:
      return len(s) == 0

    if len(p) == 1:
      if p == '.':
        return len(s) == 1
      else:
        return len(s) == 1 and s == p

    if p[1] != '*':
      if s[0] != p[0]:
        return False
      else:
        return Solution.isMatch(s[1:], p[1:])
    else:
      c0 = s[0] if p[0] == '.' else p[0]
      while s[0] == c0:
        s = s[1:]
      p = p[2:]
      return Solution.isMatch(s, p)

