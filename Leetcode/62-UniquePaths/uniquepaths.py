class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a row with 1's as the number of ways to reach any cell in the first row is 1
        row = [1] * n
        print(f"Initial row: {row}")
        
        # Iterate over each row starting from the second last row to the top
        for i in range(m - 1):
            # Create a new row initialized with 1's
            new_row = [1] * n
            print(f"\nRow {i+1}:")
            # Iterate over each column from second last to the first
            for j in range(n - 2, -1, -1):
                # The number of ways to reach cell (i, j) is the sum of the ways to reach cell to the right and the cell below
                new_row[j] = new_row[j + 1] + row[j]
                print(f"new_row[{j}] (new_row[{j + 1}] + row[{j}]): {new_row[j]} ({new_row[j + 1]} + {row[j]})")
            
            # Update row to be the new_row
            row = new_row
            print(f"Updated row: {row}")
        
        # Return the number of ways to reach the top-left corner
        return row[0]

# Example usage:
solution = Solution()
print("\nExample 1: m = 3, n = 7")
print("Unique paths:", solution.uniquePaths(3, 7))  # Output: 28

print("\nExample 2: m = 3, n = 2")
print("Unique paths:", solution.uniquePaths(3, 2))  # Output: 3
