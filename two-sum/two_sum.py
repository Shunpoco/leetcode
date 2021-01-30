from typing import List

def twoSum(nums: List[int], target: int)-> List[int]:
  hashTable = {}
  for i in range(len(nums)):
    val = nums[i]
    if val in hashTable.keys():
      hashTable[val].append(i)
    else:
      hashTable[val] = [i]
  
  for val in hashTable:
    sub = target - val
    res1 = hashTable[val][0]

    if sub == val and len(hashTable[val]) > 1:
      res2 = hashTable[val][1]
      break
    elif sub != val and sub in hashTable.keys():
      res2 = hashTable[sub][0]
      break

  return [res1, res2]
