def generate_str(begin, end):
    if begin == end:
        return str(begin)
    else:
        return str(begin) + '->' + str(end)
        
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        n = len(nums)
        result = []
        # when nums is empty, everything is missing
        if n == 0:
            result.append(generate_str(lower, upper))
            return result
        
        # when first number is greater than lower
        # item is lower to first number minus 1
        if nums[0] > lower:
            result.append(generate_str(lower, nums[0] - 1))
        
        # typical case
        # Think about it as two pointers moving up by 1 each iteration
        # [0,  1,  3, ...]
        #  ^   ^
        # i-1  i
        for i in range(1, n):
            # if the difference is greater than 1, meaning it isn't consecutive
            # item is value from first pointer add one to exclude the value
            # to value from the second point minus one to exlude the value
            if nums[i] - nums[i-1] > 1:
                result.append(generate_str(nums[i-1]+1, nums[i]-1))
            
        # when last number is less than upper
        # item is last number plus 1 to upper
        if nums[n-1] < upper:
            result.append(generate_str(nums[n-1] +1, upper))
        
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.findMissingRanges([0,1], 0 ,20))
