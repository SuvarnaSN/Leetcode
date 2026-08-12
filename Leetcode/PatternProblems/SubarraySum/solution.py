class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            needed = prefix_sum - k

            if needed in prefix_counts:
                count += prefix_counts[needed]

            prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1

        return count
