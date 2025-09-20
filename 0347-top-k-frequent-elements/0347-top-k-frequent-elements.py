class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        table = {}
        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1

        arr = [[] for _ in range(len(nums) + 1)]
        
        for num, count in table.items():
            arr[count].append(num)

        result = []
        for i in range(len(arr) -1, 0, -1):
            for num in arr[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result


        