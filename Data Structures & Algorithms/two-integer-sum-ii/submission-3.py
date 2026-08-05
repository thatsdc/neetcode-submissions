class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a_idx = 0
        b_idx = len(numbers) - 1

        while a_idx < b_idx:
            numbs_sum = numbers[a_idx] + numbers[b_idx]
            if numbs_sum == target: 
                return [a_idx+1, b_idx+1]
            elif numbs_sum < target: 
                a_idx+=1
            else: 
                b_idx-=1

        return []

         