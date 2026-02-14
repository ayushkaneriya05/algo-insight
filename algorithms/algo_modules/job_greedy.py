"""
Job Scheduling with Deadlines - Greedy Approach

This module implements the Job Scheduling problem with deadlines and profits.
Goal: Maximize total profit while meeting deadlines.

Time Complexity: O(n log n) for sorting + O(n * max_deadline) for scheduling
Space Complexity: O(max_deadline) for the time slots
"""
import time


def job_scheduling(job_ids, deadlines, profits):
    """
    Solve the Job Scheduling problem to maximize profit.
    
    Args:
        job_ids: List of job identifiers
        deadlines: List of job deadlines
        profits: List of job profits
    
    Returns:
        Dictionary containing:
        - total_profit: Maximum profit achievable
        - selected_jobs: List of scheduled job details
        - schedule: Time slot assignments
        - execution_time: Time taken to execute in milliseconds
        - time_complexity: Theoretical time complexity
    """
    start_time = time.perf_counter()
    
    n = len(job_ids)
    
    # Create list of jobs
    jobs = []
    for i in range(n):
        jobs.append({
            'id': job_ids[i],
            'deadline': deadlines[i],
            'profit': profits[i]
        })
    
    # Sort jobs by profit in descending order (greedy by profit)
    jobs.sort(key=lambda x: x['profit'], reverse=True)
    
    # Find maximum deadline
    max_deadline = max(deadlines) if deadlines else 0
    
    # Create time slots (1-indexed, slot 0 unused)
    # -1 means the slot is free
    time_slots = [-1] * (max_deadline + 1)
    
    selected_jobs = []
    total_profit = 0
    schedule = {}
    
    for job in jobs:
        # Find a free slot for this job (latest possible before deadline)
        for slot in range(min(max_deadline, job['deadline']), 0, -1):
            if time_slots[slot] == -1:
                # Assign job to this slot
                time_slots[slot] = job['id']
                selected_jobs.append({
                    'job_id': job['id'],
                    'deadline': job['deadline'],
                    'profit': job['profit'],
                    'scheduled_at': slot
                })
                schedule[slot] = job['id']
                total_profit += job['profit']
                break
    
    # Sort selected jobs by scheduled time for display
    selected_jobs.sort(key=lambda x: x['scheduled_at'])
    
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000
    
    # Create schedule visualization
    schedule_display = []
    for slot in range(1, max_deadline + 1):
        if time_slots[slot] != -1:
            schedule_display.append({
                'time_slot': slot,
                'job_id': time_slots[slot]
            })
        else:
            schedule_display.append({
                'time_slot': slot,
                'job_id': 'Empty'
            })
    
    return {
        'total_profit': total_profit,
        'jobs_scheduled': len(selected_jobs),
        'total_jobs': n,
        'selected_jobs': selected_jobs,
        'schedule': schedule_display,
        'max_deadline': max_deadline,
        'execution_time': round(execution_time, 4),
        'time_complexity': 'O(n log n + n × d)',
        'space_complexity': 'O(d)',
        'algorithm_type': 'Greedy with DP-like slot assignment',
        'selection_criteria': 'Highest Profit First'
    }
