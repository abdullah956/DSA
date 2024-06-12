from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:  # Corrected 'str' to 'strs'
            count = [0] * 26

            # Counting occurrences of characters in the string
            for c in s:
                count[ord(c) - ord('a')] += 1

            # Print the count and the corresponding string
            print(f"Count: {count}, String: {s}")

            # Append the string to the appropriate group based on its count
            res[tuple(count)].append(s)
        return res.values()

# Example usage:
solution = Solution()
result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(list(result))
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:  # Corrected 'str' to 'strs'
            count = [0] * 26

            # Counting occurrences of characters in the string
            for c in s:
                count[ord(c) - ord('a')] += 1

            # Print the count and the corresponding string
            print(f"Count: {count}, String: {s}")

            # Append the string to the appropriate group based on its count
            res[tuple(count)].append(s)
            #print(res)
        return res.values()

# Example usage:
solution = Solution()
result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(list(result))
