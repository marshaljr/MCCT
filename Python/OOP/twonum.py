class Solution:
    def twoSum(self, nums,target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

obj = Solution()
nums = [2, 7, 11, 15]
target = 9
result = obj.twoSum(nums, target)
print(f"Output: {result}")  # Output: [0, 1]


# class Solution:
#     def twoSum(self, nums, target):
#         seen = {}

#         for i in range(len(nums)):
#             complement = target - nums[i]

#             if complement in seen:
#                 return [seen[complement], i]

#             seen[nums[i]] = i