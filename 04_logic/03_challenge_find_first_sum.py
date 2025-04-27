
from typing import List, Tuple, Optional, Union

def find_first_sum(nums: List[int], goal: int) -> Optional[Union[Tuple[int, int], List[int]]]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == goal:
                return (nums[i], nums[j])
    return None  # Return None if no pair is found

nums = [1, 2, 6, 4, 2]
goal = 8
result = find_first_sum(nums, goal)
print(result)  # Output the result
