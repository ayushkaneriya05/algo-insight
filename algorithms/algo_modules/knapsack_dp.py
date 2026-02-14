"""
0/1 Knapsack Algorithm - Dynamic Programming Approach

This module implements the 0/1 Knapsack problem using dynamic programming.
Items cannot be divided - either take the whole item or leave it.

Time Complexity: O(n * W) where W is capacity
Space Complexity: O(n * W) for the DP table
"""
import time


def zero_one_knapsack(weights, values, capacity):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    
    Args:
        weights: List of item weights (must be integers)
        values: List of item values
        capacity: Maximum capacity of the knapsack (must be integer)
    
    Returns:
        Dictionary containing:
        - max_value: Maximum value achievable
        - selected_items: List of selected item indices
        - execution_time: Time taken to execute in milliseconds
        - time_complexity: Theoretical time complexity
    """
    start_time = time.perf_counter()
    
    n = len(weights)
    capacity = int(capacity)
    weights = [int(w) for w in weights]
    
    # Create DP table
    # dp[i][w] = maximum value using first i items with capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i-1][w]
            
            # Take item i if possible
            if weights[i-1] <= w:
                value_with_item = dp[i-1][w - weights[i-1]] + values[i-1]
                dp[i][w] = max(dp[i][w], value_with_item)
    
    max_value = dp[n][capacity]
    
    # Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append({
                'item_index': i,  # 1-indexed for display
                'weight': weights[i-1],
                'value': values[i-1],
                'fraction': 1.0,
                'value_contributed': values[i-1]
            })
            w -= weights[i-1]
    
    selected_items.reverse()  # Show in original order
    
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000

    return {
        'max_value': max_value,
        'selected_items': selected_items,
        'execution_time': round(execution_time, 4),
        'time_complexity': f'O(n × W) = O({n} × {capacity})',
        'space_complexity': f'O(n × W) = O({n} × {capacity})',
        'algorithm_type': 'Dynamic Programming',
        'allows_fraction': False
    }
