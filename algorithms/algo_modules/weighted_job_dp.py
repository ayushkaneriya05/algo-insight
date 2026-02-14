"""
Weighted Job Scheduling - Dynamic Programming Approach

This module implements the Weighted Job Scheduling problem using DP.
Find maximum profit subset of non-overlapping jobs.

Time Complexity: O(n log n) - sorting + binary search for each job
Space Complexity: O(n) - for DP table
"""
import time
import bisect


def weighted_job_scheduling(job_ids, start_times, end_times, profits):
    """
    Solve the Weighted Job Scheduling problem using Dynamic Programming.
    
    Args:
        job_ids: List of job identifiers
        start_times: List of job start times
        end_times: List of job end times
        profits: List of profits for each job
    
    Returns:
        Dictionary containing:
        - max_profit: Maximum profit achievable
        - selected_jobs: List of selected job details
        - all_jobs: All jobs with selection status
        - execution_time: Time taken in milliseconds
        - time_complexity: Theoretical time complexity
    """
    start_exec_time = time.perf_counter()
    
    n = len(job_ids)
    
    if n == 0:
        return {
            'max_profit': 0,
            'jobs_selected': 0,
            'total_jobs': 0,
            'selected_jobs': [],
            'all_jobs': [],
            'max_time': 1,
            'execution_time': 0,
            'time_complexity': 'O(n log n)',
            'space_complexity': 'O(n)',
            'algorithm_type': 'Dynamic Programming',
            'approach': 'Sort by end time + Binary Search'
        }
    
    # Create list of jobs with all their details (using original index for tracking)
    jobs = []
    for i in range(n):
        jobs.append({
            'original_index': i,
            'id': job_ids[i],
            'start': start_times[i],
            'end': end_times[i],
            'profit': profits[i]
        })
    
    # Sort jobs by end time
    jobs.sort(key=lambda x: x['end'])
    
    # Extract sorted end times for binary search
    sorted_end_times = [job['end'] for job in jobs]
    
    def find_last_non_conflicting(idx):
        """
        Find the latest job that doesn't conflict with job at idx.
        A job j doesn't conflict if jobs[j].end <= jobs[idx].start
        """
        target = jobs[idx]['start']
        # Find rightmost position where end_time <= target
        pos = bisect.bisect_right(sorted_end_times, target, 0, idx) - 1
        return pos
    
    # DP array: dp[i] = max profit considering jobs 0 to i (after sorting)
    dp = [0] * n
    dp[0] = jobs[0]['profit']
    
    # Fill DP table
    for i in range(1, n):
        # Option 1: Include current job
        include_profit = jobs[i]['profit']
        last_non_conflict = find_last_non_conflicting(i)
        if last_non_conflict >= 0:
            include_profit += dp[last_non_conflict]
        
        # Option 2: Exclude current job (take previous best)
        exclude_profit = dp[i - 1]
        
        # Take the maximum
        dp[i] = max(include_profit, exclude_profit)

    # Backtrack to find selected jobs
    selected_indices = []
    i = n - 1
    while i >= 0:
        include_profit = jobs[i]['profit']
        last_non_conflict = find_last_non_conflicting(i)
        if last_non_conflict >= 0:
            include_profit += dp[last_non_conflict]
        
        # Check if we included this job
        if i == 0:
            # First job is always included if we reach here
            selected_indices.append(i)
            break
        elif include_profit > dp[i - 1]:
            # We included this job
            selected_indices.append(i)
            i = last_non_conflict
        else:
            # We excluded this job
            i = i - 1
    
    selected_indices.reverse()
    selected_set = set(selected_indices)
    
    # Find max time for visualization
    max_time = max(end_times) if end_times else 1
    
    # Build selected jobs list
    selected_jobs = []
    for idx in selected_indices:
        job = jobs[idx]
        duration = job['end'] - job['start']
        left_pct = (job['start'] / max_time) * 100
        width_pct = (duration / max_time) * 100
        selected_jobs.append({
            'job_id': job['id'],
            'start_time': job['start'],
            'end_time': job['end'],
            'profit': job['profit'],
            'duration': duration,
            'left_percent': round(left_pct, 2),
            'width_percent': round(max(width_pct, 5), 2)
        })
    
    # Build all jobs list for visualization (in sorted order)
    all_jobs = []
    for i, job in enumerate(jobs):
        duration = job['end'] - job['start']
        left_pct = (job['start'] / max_time) * 100
        width_pct = (duration / max_time) * 100
        all_jobs.append({
            'job_id': job['id'],
            'start_time': job['start'],
            'end_time': job['end'],
            'profit': job['profit'],
            'duration': duration,
            'is_selected': i in selected_set,
            'left_percent': round(left_pct, 2),
            'width_percent': round(max(width_pct, 5), 2)
        })
    
    # Generate time markers for visualization axis
    time_markers = []
    for t in range(int(max_time) + 1):
        left_pct = (t / max_time) * 100 if max_time > 0 else 0
        time_markers.append({
            'value': t,
            'left_percent': round(left_pct, 2)
        })
    
    end_exec_time = time.perf_counter()
    execution_time = (end_exec_time - start_exec_time) * 1000
    
    return {
        'max_profit': dp[n - 1],
        'jobs_selected': len(selected_jobs),
        'total_jobs': n,
        'selected_jobs': selected_jobs,
        'all_jobs': all_jobs,
        'max_time': max_time,
        'time_markers': time_markers,
        'execution_time': round(execution_time, 4),
        'time_complexity': 'O(n log n)',
        'space_complexity': 'O(n)',
        'algorithm_type': 'Dynamic Programming',
        'approach': 'Sort by end time + Binary Search'
    }
