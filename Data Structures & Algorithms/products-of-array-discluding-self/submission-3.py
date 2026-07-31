class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Without using division operator O(n)
        prefix_list = []
        postfix_list = []

        mult_a = 1
        mult_b = 1
        for i in range(len(nums)): 
            a = nums[i]
            b = nums[len(nums)-1-i]

            mult_a *= a
            mult_b *= b

            prefix_list.append(mult_a)
            postfix_list.append(mult_b)
        postfix_list = postfix_list[::-1]

        result = []
        for i in range(len(nums)):
            prefix_value = prefix_list[i-1] if i > 0 else 1
            postfix_value = postfix_list[i+1] if i < len(nums)-1 else 1

            mult = prefix_value  * postfix_value 
            result.append(mult)

        return result
            
            


        