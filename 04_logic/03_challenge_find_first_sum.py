
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



# Solución alternativa con diccionarios
def find_first_sum(nums, goal):
    seen = {} # disccionario para almacenar numeros e indices
    for index, value in enumerate(nums):
        missing = goal - value
        if missing in seen: return [seen [missing], index]
        seen[value] = index
    return None  # Return None if no pair is found
        
nums = [1, 2, 6, 4, 2]
goal = 8
result = find_first_sum(nums, goal)
print(result)  # Output the result
