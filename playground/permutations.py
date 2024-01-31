import json
from typing import List

def permutations(perms: List[any], items: List[any], startIdx: int) -> None:
  if startIdx >= len(items):
    return

  # print("\nitems, startIdx =", items, startIdx)

  if startIdx == len(items) - 1:
    perms.append(json.dumps(items))
    return

  i = startIdx
  # [0,1,2,3]
  while i <= len(items) - 1:
    nextItems = [ *items[0:startIdx], items[i], *items[startIdx:i], *items[i+1:] ]
    # print(nextItems)
    permutations(
      perms,
      nextItems,
      startIdx + 1
    )
    i += 1


if __name__ == '__main__':
  perms = []
  permutations(perms, [0,1,2,3], 0)

  print(f"\ntotal = {len(perms)}, perms =\n", "\n".join(perms))

  # perms = []
  # permutations(perms, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], 0)
  # print(f"\ntotal = {len(perms)}, perms =\n", "\n".join(perms))
