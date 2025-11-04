
# using dictionary python
import heapq

nums = list(map(int, input("Enter nums list (comma separated): ").split(",")))
k = int(input("Enter k = "))

# Step 1: Count frequencies manually
count_dict = {}
for num in nums:
    #return 0 bydefault else if more count(nums) are present then return that count
    count_dict[num] = count_dict.get(num, 0) + 1

# Step 2: Use a heap to get top k frequent elements
heap = []
print(count_dict.items())
for num, freq in count_dict.items():
    heapq.heappush(heap, (freq, num))
    if len(heap) > k:
        heapq.heappop(heap)
print("Heap = ",heap)
# Step 3: Extract result
result = [num for freq, num in heap]
print("Top", k, "frequent elements:", result)


