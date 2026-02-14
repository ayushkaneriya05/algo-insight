from django.shortcuts import render, redirect
from django.urls import reverse
from .algo_modules.knapsack_greedy import fractional_knapsack
from .algo_modules.knapsack_dp import zero_one_knapsack
from .algo_modules.activity_greedy import activity_selection
from .algo_modules.job_greedy import job_scheduling
from .algo_modules.weighted_job_dp import weighted_job_scheduling


def home_view(request):
    """Home page with project introduction and problem selection."""
    return render(request, 'home.html')


def knapsack_view(request):
    """
    Handle Knapsack problem - both input form and result display.
    Compares Fractional (Greedy) vs 0/1 (DP) Knapsack.
    Uses session to store results and PRG pattern to avoid form resubmission.
    """
    context = {
        'show_results': False,
        'error': None
    }
    
    if request.method == 'POST':
        try:
            # Parse input
            weights_str = request.POST.get('weights', '')
            values_str = request.POST.get('values', '')
            capacity = request.POST.get('capacity', '')
            
            # Convert to lists
            weights = [float(w.strip()) for w in weights_str.split(',') if w.strip()]
            values = [float(v.strip()) for v in values_str.split(',') if v.strip()]
            capacity = float(capacity)
            
            # Validate input
            if len(weights) != len(values):
                raise ValueError("Number of weights must equal number of values")
            if len(weights) == 0:
                raise ValueError("Please enter at least one item")
            if capacity <= 0:
                raise ValueError("Capacity must be positive")
            
            # Run algorithms
            greedy_result = fractional_knapsack(weights, values, capacity)
            dp_result = zero_one_knapsack(weights, values, capacity)
            
            # Store results in session
            request.session['knapsack_results'] = {
                'show_results': True,
                'input_data': {
                    'weights': weights,
                    'values': values,
                    'capacity': capacity,
                    'num_items': len(weights)
                },
                'greedy_result': greedy_result,
                'dp_result': dp_result,
                'comparison': {
                    'greedy_value': greedy_result['max_value'],
                    'dp_value': dp_result['max_value'],
                    'greedy_time': greedy_result['execution_time'],
                    'dp_time': dp_result['execution_time'],
                    'value_difference': round(greedy_result['max_value'] - dp_result['max_value'], 2)
                }
            }
            
            # Redirect to avoid form resubmission (PRG pattern)
            return redirect('algorithms:knapsack')
            
        except ValueError as e:
            context['error'] = str(e)
        except Exception as e:
            context['error'] = f"An error occurred: {str(e)}"
    
    # GET request - check for results in session
    if 'knapsack_results' in request.session:
        results = request.session.pop('knapsack_results')
        context.update(results)
    
    return render(request, 'knapsack.html', context)


def scheduling_view(request):
    """
    Handle Scheduling problems - Activity Selection, Job Scheduling, and Weighted Job Scheduling.
    Uses session to store results and PRG pattern to avoid form resubmission.
    """
    context = {
        'show_activity_results': False,
        'show_job_results': False,
        'show_weighted_job_results': False,
        'error': None
    }
    
    if request.method == 'POST':
        problem_type = request.POST.get('problem_type', '')
        
        try:
            if problem_type == 'activity':
                # Parse Activity Selection input
                start_times_str = request.POST.get('start_times', '')
                finish_times_str = request.POST.get('finish_times', '')
                
                start_times = [int(s.strip()) for s in start_times_str.split(',') if s.strip()]
                finish_times = [int(f.strip()) for f in finish_times_str.split(',') if f.strip()]
                
                if len(start_times) != len(finish_times):
                    raise ValueError("Number of start times must equal number of finish times")
                if len(start_times) == 0:
                    raise ValueError("Please enter at least one activity")
                
                # Run algorithm
                result = activity_selection(start_times, finish_times)
                
                # Store results in session
                request.session['scheduling_results'] = {
                    'show_activity_results': True,
                    'activity_input': {
                        'start_times': start_times,
                        'finish_times': finish_times,
                        'num_activities': len(start_times)
                    },
                    'activity_result': result
                }
                
                # Redirect to avoid form resubmission
                return redirect('algorithms:scheduling')
                
            elif problem_type == 'job':
                # Parse Job Scheduling input
                job_ids_str = request.POST.get('job_ids', '')
                deadlines_str = request.POST.get('deadlines', '')
                profits_str = request.POST.get('profits', '')
                
                job_ids = [j.strip() for j in job_ids_str.split(',') if j.strip()]
                deadlines = [int(d.strip()) for d in deadlines_str.split(',') if d.strip()]
                profits = [int(p.strip()) for p in profits_str.split(',') if p.strip()]
                
                if not (len(job_ids) == len(deadlines) == len(profits)):
                    raise ValueError("Number of job IDs, deadlines, and profits must match")
                if len(job_ids) == 0:
                    raise ValueError("Please enter at least one job")
                
                # Run algorithm
                result = job_scheduling(job_ids, deadlines, profits)
                
                # Store results in session
                request.session['scheduling_results'] = {
                    'show_job_results': True,
                    'job_input': {
                        'job_ids': job_ids,
                        'deadlines': deadlines,
                        'profits': profits,
                        'num_jobs': len(job_ids)
                    },
                    'job_result': result
                }
                
                # Redirect to avoid form resubmission
                return redirect('algorithms:scheduling')
            
            elif problem_type == 'weighted_job':
                # Parse Weighted Job Scheduling input
                job_ids_str = request.POST.get('wjob_ids', '')
                start_times_str = request.POST.get('wjob_start_times', '')
                end_times_str = request.POST.get('wjob_end_times', '')
                profits_str = request.POST.get('wjob_profits', '')
                
                job_ids = [j.strip() for j in job_ids_str.split(',') if j.strip()]
                start_times = [int(s.strip()) for s in start_times_str.split(',') if s.strip()]
                end_times = [int(e.strip()) for e in end_times_str.split(',') if e.strip()]
                profits = [int(p.strip()) for p in profits_str.split(',') if p.strip()]
                
                if not (len(job_ids) == len(start_times) == len(end_times) == len(profits)):
                    raise ValueError("Number of job IDs, start times, end times, and profits must match")
                if len(job_ids) == 0:
                    raise ValueError("Please enter at least one job")
                
                # Run algorithm
                result = weighted_job_scheduling(job_ids, start_times, end_times, profits)
                
                # Store results in session
                request.session['scheduling_results'] = {
                    'show_weighted_job_results': True,
                    'weighted_job_input': {
                        'job_ids': job_ids,
                        'start_times': start_times,
                        'end_times': end_times,
                        'profits': profits,
                        'num_jobs': len(job_ids)
                    },
                    'weighted_job_result': result
                }
                
                # Redirect to avoid form resubmission
                return redirect('algorithms:scheduling')
                
        except ValueError as e:
            context['error'] = str(e)
        except Exception as e:
            context['error'] = f"An error occurred: {str(e)}"
    
    # GET request - check for results in session
    if 'scheduling_results' in request.session:
        results = request.session.pop('scheduling_results')
        context.update(results)
    
    return render(request, 'scheduling.html', context)
