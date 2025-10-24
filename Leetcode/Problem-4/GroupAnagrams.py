from collections import defaultdict

# strs = ["", ""]
strs = ["eat","tea","tan","ate","nat","bat"]

# Step 1: Build groups by sorted characters
anagrams_dict = defaultdict(list)

for string in strs:
    key = tuple(sorted(string))  
    # print(sorted(string), key)
    anagrams_dict[key].append(string)

# Step 2: Convert to list of lists
anagrams = list(anagrams_dict.values())

print("\nANAGRAMS =", anagrams)
