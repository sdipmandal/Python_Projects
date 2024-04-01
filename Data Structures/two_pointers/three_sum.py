'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''
class Solution:
    def twoSum(self, nums, target):
        l, r = 0, len(nums)-1
        solutions = []
        while l < r:
            total = nums[l] + nums[r]
            if total == target:
                solutions.append([nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l<r:
                    l+=1
            elif total > target:
                r -= 1
            elif total < target:
                l += 1
        
        return solutions

    def threeSum(self, nums):
        nums.sort()
        a = set()
        solution_list = []
        for i, num in enumerate(nums):
            if num not in a:
                a.add(num)
                output = self.twoSum(nums[i+1:], -num)
                if output:
                    for op in output:
                        op.append(num)
                        solution_list.append(op)
        
        return solution_list

print(Solution().threeSum([0,0,0]))
        