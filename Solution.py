class Solution:
    # Function to return max value that can be put in knapsack of capacity.
    def knapSack(self, capacity, val, wt):
        n = len(val)  # Number of items
        # Initialize DP table with 0s
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        # Fill DP table
        for i in range(1, n + 1):  # Iterate over items
            for w in range(1, capacity + 1):  # Iterate over capacities
                if wt[i - 1] <= w:  # Current item's weight fits in capacity
                    dp[i][w] = max(dp[i - 1][w],  # Exclude the item
                                   dp[i - 1][w - wt[i - 1]] + val[i - 1])  # Include the item
                else:
                    dp[i][w] = dp[i - 1][w]  # Exclude the item

        return dp[n][capacity]  # Maximum value for all items and full capacity


# Driver Code
if __name__ == '__main__':
    test_cases = int(input("Enter number of test cases: "))
    for _ in range(test_cases):
        # Read capacity
        capacity = int(input("Enter knapsack capacity: "))
        values = list(map(int, input("Enter values: ").strip().split()))
        weights = list(map(int, input("Enter weights: ").strip().split()))
        ob = Solution()
        print("Maximum value:", ob.knapSack(capacity, values, weights))
        print("~")

# Test Example
# Input:
# 1
# 50
# 60 100 120
# 10 20 30
# Output: 220
