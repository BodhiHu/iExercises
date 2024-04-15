
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


def encrypt():
  line = input()
  letters = list(line)
  encrypted = []
  for l in letters:
    if l.isalpha():
      if l == 'z':
        l = 'a'
      elif l == 'Z':
        l = 'A'
      else:
        l = chr(ord(l) + 1)

      l = l.lower() if l.isupper() else l.upper()
    elif l.isnumeric():
      l = str((int(l) + 1) % 10) 
    
    encrypted.append(l)

  print("".join(encrypted))


# input: 1 2 3 4 3 2 1 1 7
# the last num is k, the rest are the array of numbers
# find consecutive sub arrays that sum to k
def count_subarrays():
  line = input()
  args = line.split(" ")
  nums = [ int(num) for num in args[0:-1] ]
  k = int(args[-1])

  count = 0

  for i in range(0, len(nums)):
    sum = 0
    for j in range(i, len(nums)):
      if j == i:
        sum = nums[i]
      else:
        sum += nums[j]
      if sum >= k:
        if sum == k:
          count += 1
        break
    print("  debug >> ", i, sum)

  print(count)


# 3_ABAKKABA_7
# AHHHA
def longest_symmetric_substr():
  import math
  s = input()
  longest_subs = ""
  for i in range(0, len(s)-1):
    for j in range(i+2, len(s)):
      subs = s[i:j]
      if len(subs) > math.ceil(len(s[i:])/2):
        break

      reversed_subs = "".join(reversed(subs))
      if s[j-1:j-1+len(subs)] == reversed_subs:
        concated = subs[i:j-1] + reversed_subs
        if len(concated) > len(longest_subs):
          longest_subs = concated
      if s[j:j+len(subs)] == reversed_subs:
        concated = subs + reversed_subs
        if len(concated) > len(longest_subs):
          longest_subs = concated

      # print(subs, s[j-1:j-1+len(subs)], s[j:j+len(subs)])
  
  print(longest_subs)


if __name__ == '__main__':
  # make_chore()
  # search_word()
  # encrypt()
  # count_subarrays()
  longest_symmetric_substr()
