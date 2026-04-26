class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            diff = target - num 
            if diff in num_map:
                print(f"Found:[{num_map[diff]},{i}]")
                return [num_map[diff], i]
            num_map[num] = i

        return []