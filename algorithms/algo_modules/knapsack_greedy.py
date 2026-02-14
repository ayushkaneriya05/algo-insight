"""
Fractional Knapsack Algorithm - Greedy Approach

This module implements the Fractional Knapsack problem using a greedy algorithm.
Items can be divided and fractional parts can be taken.

Time Complexity: O(n log n) - due to sorting
Space Complexity: O(n) - for storing items
"""
import time


def fractional_knapsack(weights, values, capacity):
    """
    Solve the Fractional Knapsack problem using a greedy approach.
    
    Args:
        weights: List of item weights
        values: List of item values
        capacity: Maximum capacity of the knapsack
    
    Returns:
        Dictionary containing:
        - max_value: Maximum value achievable
        - selected_items: List of tuples (item_index, fraction_taken, value_contributed)
        - execution_time: Time taken to execute in milliseconds
        - time_complexity: Theoretical time complexity
    """
    start_time = time.perf_counter()
    
    n = len(weights)
    
    # Create list of items with their ratio (value/weight)
    items = []
    for i in range(n):
        if weights[i] > 0:
            ratio = values[i] / weights[i]
        else:
            ratio = float('inf')
        items.append({
            'index': i,
            'weight': weights[i],
            'value': values[i],
            'ratio': ratio
        })
    
    # Sort items by value-to-weight ratio in descending order (Greedy choice)
    items.sort(key=lambda x: x['ratio'], reverse=True)
    
    total_value = 0.0
    remaining_capacity = capacity
    selected_items = []
    
    for item in items:
        if remaining_capacity <= 0:
            break
        
        if item['weight'] <= remaining_capacity:
            # Take the whole item
            fraction = 1.0
            value_added = item['value']
            remaining_capacity -= item['weight']
        else:
            # Take fraction of the item
            fraction = remaining_capacity / item['weight']
            value_added = item['value'] * fraction
            remaining_capacity = 0
        
        total_value += value_added
        selected_items.append({
            'item_index': item['index'] + 1,  # 1-indexed for display
            'weight': item['weight'],
            'value': item['value'],
            'fraction': round(fraction, 4),
            'value_contributed': round(value_added, 2)
        })
    
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    
    return {
        'max_value': round(total_value, 2),
        'selected_items': selected_items,
        'execution_time': round(execution_time, 4),
        'time_complexity': 'O(n log n)',
        'space_complexity': 'O(n)',
        'algorithm_type': 'Greedy',
        'allows_fraction': True
    }
