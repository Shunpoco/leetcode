## Search Insert Position
https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct intergers and a target value, return the index if the target is found.

If not, return the index where it would be if it were inserted in order.

### Example
Example1:
```
Input: nums = [1, 3, 5, 6], target = 5
Output: 2
```

Example2:
```
Input: nums = [1, 3, 5, 6], target = 2
Output: 1
```

Example3:
```
Input: nums = [1, 3, 5, 6], target = 7
Output: 4
```

Example4:
```
Input: nums = [1, 3, 5, 6], target = 0
Ourput: 0
```

Example5:
```
Input: nums = [1], target = 0
Output: 0
```

### Constraints:
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains distinct values sorted in ascending order.
- `-10^4 <= target <= 10^4`
