nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter target number: "))

class Solution:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i
        return []

solution = Solution()
result = solution.twoSum(nums, target)
print(result)