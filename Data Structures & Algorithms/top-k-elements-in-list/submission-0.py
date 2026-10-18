class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        solution = []

        for el in nums:
            if el not in freq:
                freq[el] = 0
            freq[el] +=1

        sorted_freq = sorted(freq.items(), key = lambda x: x[1])

        return [num for num, count in sorted_freq[-k:]]

        
        
        