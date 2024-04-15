
def make_chore():
  # input: 186 186 150 200 160 130 197 200
  # -> deduped: 148 161 186 149 150 200 160 130 197

  def get_longest_left(nums: list[int], idx):
    longest_n = 0
    for i in range(idx-1, 0, -1):
      n = 0
      for j in range(i, -1, -1):
        if nums[j] < nums[j+1]:
          n += 1

      if longest_n == 0 or longest_n < n:
        longest_n = n 

    return n

  def get_longest_right(nums: list[int], idx):
    n = 0
    for i in range(idx+1, len(nums)):
      if nums[i] < nums[i-1]:
        n += 1

    return n

  input1 = input().strip()
  items = input1.split(" ")
  deduped_items = []
  for item in items:
    if deduped_items.count(item) == 0:
      deduped_items.append(item)

  dup_count = len(items) - len(deduped_items)

  nums = [ int(item) for item in deduped_items ]

  print(f'deduped nums = {nums}')

  minimum_outs = -1
  for i in range(1, len(nums)-1):
    # print(f'i = {i}')
    if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
      outs = len(nums) - get_longest_left(nums, i) - get_longest_right(nums, i) - 1
      # print(f'outs = {outs}')
      if minimum_outs == -1:
        minimum_outs = outs
      if minimum_outs > outs:
        minimum_outs = outs

  if minimum_outs < 0:
    minimum_outs = 0

  print('\nResult =', dup_count + minimum_outs)


# HJ27 查找兄弟单词
# input: 3 abc bca cab abc 1
def search_word():
  line = input().strip()
  args = line.split(" ")
  word_cnt = int(args[0])
  words = [ word for word in args[1:word_cnt+1] ]
  query = args[-2]
  k = int(args[-1])

  print(words, query, k)

  matched_words = [] 
  for w in words:
    if w == query:
      continue
    if set(w) == set(query):
      matched_words.append(w)
  matched_words.sort()

  print(matched_words[k])


if __name__ == '__main__':
  # make_chore()
  search_word()
