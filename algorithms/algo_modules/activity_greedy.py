"""
Activity Selection Algorithm - Greedy Approach

This module implements the Activity Selection problem using a greedy algorithm.
Select maximum number of non-overlapping activities.

Time Complexity: O(n log n) - due to sorting by finish time
Space Complexity: O(n) - for storing activities
"""
import time


def activity_selection(start_times, finish_times):
    """
    Solve the Activity Selection problem using a greedy approach.
    
    Args:
        start_times: List of activity start times
        finish_times: List of activity finish times
    
    Returns:
        Dictionary containing:
        - selected_count: Number of activities selected
        - selected_activities: List of selected activity details
        - execution_time: Time taken to execute in milliseconds
        - time_complexity: Theoretical time complexity
    """
    start_time = time.perf_counter()
    
    n = len(start_times)
    
    # Create list of activities with their indices
    activities = []
    for i in range(n):
        activities.append({
            'index': i,
            'start': start_times[i],
            'finish': finish_times[i]
        })
    
    # Sort activities by finish time (Greedy choice)
    activities.sort(key=lambda x: x['finish'])
    
    selected_activities = []
    last_finish_time = -1
    
    # Find max time for visualization scaling
    max_time = max(finish_times) if finish_times else 1
    
    for activity in activities:
        # If this activity starts after or when the last selected activity finishes
        if activity['start'] >= last_finish_time:
            duration = activity['finish'] - activity['start']
            # Calculate percentage positions for visualization
            left_pct = (activity['start'] / max_time) * 100
            width_pct = (duration / max_time) * 100
            selected_activities.append({
                'activity_index': activity['index'] + 1,  # 1-indexed for display
                'start_time': activity['start'],
                'finish_time': activity['finish'],
                'duration': duration,
                'left_percent': round(left_pct, 2),
                'width_percent': round(max(width_pct, 5), 2)  # Min 5% for visibility
            })
            last_finish_time = activity['finish']
    
    # Create all activities data for visualization (both selected and not selected)
    all_activities = []
    selected_indices = {a['activity_index'] for a in selected_activities}
    for i in range(n):
        duration = finish_times[i] - start_times[i]
        left_pct = (start_times[i] / max_time) * 100
        width_pct = (duration / max_time) * 100
        all_activities.append({
            'activity_index': i + 1,
            'start_time': start_times[i],
            'finish_time': finish_times[i],
            'duration': duration,
            'is_selected': (i + 1) in selected_indices,
            'left_percent': round(left_pct, 2),
            'width_percent': round(max(width_pct, 5), 2)  # Min 5% for visibility
        })
    
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000
    
    # Generate time markers for visualization axis
    time_markers = []
    for t in range(int(max_time) + 1):
        left_pct = (t / max_time) * 100 if max_time > 0 else 0
        time_markers.append({
            'value': t,
            'left_percent': round(left_pct, 2)
        })
    
    return {
        'selected_count': len(selected_activities),
        'total_activities': n,
        'selected_activities': selected_activities,
        'all_activities': all_activities,
        'max_time': max_time,
        'time_markers': time_markers,
        'execution_time': round(execution_time, 4),
        'time_complexity': 'O(n log n)',
        'space_complexity': 'O(n)',
        'algorithm_type': 'Greedy',
        'selection_criteria': 'Earliest Finish Time First'
    }


