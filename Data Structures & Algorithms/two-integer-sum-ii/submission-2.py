class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a_idx = 0
        b_idx = len(numbers) - 1

        while a_idx < b_idx:
            while numbers[a_idx] + numbers[b_idx] <= target: 
                if numbers[a_idx] + numbers[b_idx] == target: 
                    return [a_idx+1, b_idx+1]
                else: 
                    a_idx+=1
            b_idx-=1

        return []

         