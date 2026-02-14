<p align="center">
  <h1 align="center">🧠 AlgoInsight — Algorithm Analysis Platform</h1>
  <p align="center">
    An interactive Django web application for comparing <strong>Greedy</strong> and <strong>Dynamic Programming</strong> algorithmic paradigms through real-time computation and side-by-side visualizations.
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/License-Educational-orange?style=for-the-badge" alt="License">
</p>

---

## 📖 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Algorithm Details](#-algorithm-details)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage Guide](#-usage-guide)
- [Screenshots](#-screenshots)
- [Architecture](#-architecture)
- [API Reference](#-api-reference)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

---

## 🎯 About the Project

**AlgoInsight** is a full-stack web application developed as a Semester 5 **Design & Analysis of Algorithms (DAA)** course project. It serves as an interactive educational tool that allows users to:

- Input custom problem instances for classic optimization problems.
- Execute both **Greedy** and **Dynamic Programming** solutions in real-time.
- Compare results side-by-side with detailed metrics including execution time, selected items/activities, and complexity analysis.
- Visualize scheduling solutions through interactive **Gantt chart** timelines.

The platform bridges the gap between theoretical algorithm study and practical experimentation, making it easy to understand **when and why** one paradigm outperforms the other.

---

## ✨ Features

### 🎒 Knapsack Problem Suite

| Feature | Greedy (Fractional) | Dynamic Programming (0/1) |
|---------|-------------------|--------------------------|
| **Approach** | Sort by value-to-weight ratio | Build optimal DP table |
| **Item Handling** | Fractional items allowed | Whole items only |
| **Guarantee** | Optimal for fractional variant | Globally optimal |
| **Input** | Weights, values, capacity | Weights, values, capacity |
| **Output** | Max value, fractions taken | Max value, items selected |

- ✅ Side-by-side result comparison with value difference analysis
- ✅ Detailed per-item breakdown (fraction taken, value contributed)
- ✅ Real-time execution time measurement (milliseconds)
- ✅ Input validation with user-friendly error messages

### 📅 Scheduling Problem Suite

#### 1. Activity Selection (Greedy)
- Selects the **maximum number of non-overlapping activities** using the *Earliest Finish Time First* strategy.
- Interactive **Gantt chart** visualization with color-coded selected vs. rejected activities.
- Displays time axis with markers for visual scaling.

#### 2. Job Scheduling with Deadlines (Greedy)
- Maximizes **total profit** by scheduling jobs within their deadlines using *Highest Profit First* strategy.
- Visual time-slot grid showing job assignments.
- Handles empty slots and deadline conflicts.

#### 3. Weighted Job Scheduling (Dynamic Programming)
- Finds the **maximum-weight subset of non-overlapping jobs** using DP with binary search.
- Gantt chart timeline with selected/rejected job distinction.
- Backtracking to identify the optimal job subset.

### 🌐 General Features
- 🎨 **Modern dark-themed UI** with the Outfit font and solid color palette
- 📱 **Fully responsive design** — works on desktop, tablet, and mobile
- 🔄 **PRG (Post-Redirect-Get) pattern** — prevents form resubmission on refresh
- 🗂️ **Session-based result storage** — clean separation of form handling and display
- ⚡ **No external API calls** — all algorithms run server-side in Python

---

## � Algorithm Details

### Complexity Comparison

| Algorithm | Paradigm | Time Complexity | Space Complexity | Optimal? |
|-----------|----------|-----------------|------------------|----------|
| Fractional Knapsack | Greedy | `O(n log n)` | `O(n)` | ✅ For fractional |
| 0/1 Knapsack | DP | `O(n × W)` | `O(n × W)` | ✅ Globally |
| Activity Selection | Greedy | `O(n log n)` | `O(n)` | ✅ Yes |
| Job Scheduling (Deadlines) | Greedy | `O(n log n + n × d)` | `O(d)` | ✅ Yes |
| Weighted Job Scheduling | DP | `O(n log n)` | `O(n)` | ✅ Yes |

> **Legend:** `n` = number of items/jobs, `W` = knapsack capacity, `d` = max deadline

### How Each Algorithm Works

<details>
<summary><strong>🟢 Fractional Knapsack (Greedy)</strong></summary>

1. Calculate value-to-weight ratio for each item.
2. Sort items by ratio in **descending order**.
3. Greedily take items — full items if capacity allows, otherwise take a fraction.
4. **Key insight:** The greedy choice (highest ratio first) is provably optimal when fractions are allowed.

```
Greedy Choice: max(value[i] / weight[i])
```
</details>

<details>
<summary><strong>🔵 0/1 Knapsack (Dynamic Programming)</strong></summary>

1. Build a 2D DP table `dp[i][w]` = max value using first `i` items with capacity `w`.
2. For each item, decide: **include it** or **skip it**.
3. Backtrack through the table to find which items were selected.
4. **Key insight:** Overlapping subproblems make DP essential — greedy fails for the 0/1 variant.

```
dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight[i]] + value[i])
```
</details>

<details>
<summary><strong>🟢 Activity Selection (Greedy)</strong></summary>

1. Sort activities by **finish time** in ascending order.
2. Select the first activity, then iteratively select the next activity whose start time ≥ the finish time of the last selected activity.
3. **Key insight:** Earliest Finish Time First maximizes the remaining time for future activities.

```
Selection Criteria: start_time[i] >= last_finish_time
```
</details>

<details>
<summary><strong>🟢 Job Scheduling with Deadlines (Greedy)</strong></summary>

1. Sort jobs by **profit in descending order**.
2. For each job, find the **latest available time slot** before its deadline.
3. Assign the job to that slot; skip if no slot is available.
4. **Key insight:** Scheduling the highest-profit jobs first with latest-slot assignment avoids blocking future high-value jobs.

```
Strategy: Highest Profit First → Latest Available Slot
```
</details>

<details>
<summary><strong>🔵 Weighted Job Scheduling (Dynamic Programming)</strong></summary>

1. Sort jobs by **end time**.
2. For each job, use **binary search** to find the latest non-conflicting job.
3. Build DP array: `dp[i] = max(include job i, exclude job i)`.
4. Backtrack to find the selected subset.
5. **Key insight:** Binary search reduces the conflict-checking step from O(n) to O(log n).

```
dp[i] = max(profit[i] + dp[last_non_conflicting(i)], dp[i-1])
```
</details>

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Django 6.0 | Web framework, routing, session management |
| **Language** | Python 3.11+ | Algorithm implementation, server logic |
| **Frontend** | HTML5, Bootstrap 5.3 | Responsive layout, UI components |
| **Styling** | Custom CSS (dark theme) | Solid color palette, Outfit font |
| **Interactivity** | Vanilla JavaScript | Gantt charts, dynamic form handling |
| **Icons** | Bootstrap Icons | UI iconography |
| **Database** | SQLite 3 | Default Django session/admin storage |

---

## 📁 Project Structure

```
algoinsight/
│
├── 📄 manage.py                      # Django management entry point
├── 📄 requirements.txt               # Python dependencies
├── 📄 db.sqlite3                     # SQLite database
├── 📄 README.md                      # This file
│
├── 📁 algoinsight/                   # Django project configuration
│   ├── __init__.py
│   ├── settings.py                   # Project settings (DEBUG, apps, DB)
│   ├── urls.py                       # Root URL router → includes algorithms.urls
│   ├── wsgi.py                       # WSGI application entry point
│   └── asgi.py                       # ASGI application entry point
│
└── 📁 algorithms/                    # Main application
    ├── __init__.py
    ├── apps.py                       # App configuration
    ├── urls.py                       # App-level URL routing (3 routes)
    ├── views.py                      # View controllers (home, knapsack, scheduling)
    │
    ├── 📁 algo_modules/              # Algorithm implementations
    │   ├── __init__.py
    │   ├── knapsack_greedy.py        # Fractional Knapsack — Greedy
    │   ├── knapsack_dp.py            # 0/1 Knapsack — Dynamic Programming
    │   ├── activity_greedy.py        # Activity Selection — Greedy
    │   ├── job_greedy.py             # Job Scheduling with Deadlines — Greedy
    │   └── weighted_job_dp.py        # Weighted Job Scheduling — DP
    │
    ├── 📁 static/                    # Static assets
    │   ├── css/
    │   │   └── style.css             # Custom dark-theme styling
    │   └── js/
    │       └── main.js               # Client-side interactivity
    │
    └── 📁 templates/                 # Django HTML templates
        ├── base.html                 # Base layout (navbar, footer, CDN links)
        ├── home.html                 # Landing page with problem selection
        ├── knapsack.html             # Knapsack input form + results display
        └── scheduling.html           # Scheduling problems (3-in-1 page)
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.11** or higher — [Download Python](https://www.python.org/downloads/)
- **pip** — comes bundled with Python
- **Git** (optional) — for cloning the repository

### Installation

#### 1. Clone or Download the Repository

```bash
git clone <repository-url>
cd algoinsight
```

#### 2. Create a Virtual Environment

```bash
# Create
python -m venv .venv

# Activate (Windows - PowerShell)
.venv\Scripts\Activate.ps1

# Activate (Windows - Command Prompt)
.venv\Scripts\activate.bat

# Activate (macOS / Linux)
source .venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
| Package | Version | Purpose |
|---------|---------|---------|
| Django | 6.0.2 | Web framework |

#### 4. Configure Django Settings

> **Note:** `settings.py` is not included in the repository for security reasons. You need to create it manually.

Create the file `algoinsight/settings.py` with the following content:

```python
"""
Django settings for algoinsight project.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: Generate your own secret key!
# Run: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
SECRET_KEY = 'your-secret-key-here'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'algorithms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'algoinsight.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'algoinsight.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
```

> **⚠️ Important:** Replace `'your-secret-key-here'` with a unique secret key. Generate one by running:
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

#### 5. Apply Database Migrations

```bash
python manage.py migrate
```

#### 6. Start the Development Server

```bash
python manage.py runserver
```

#### 7. Open in Browser

Navigate to **http://127.0.0.1:8000** — you'll see the AlgoInsight home page.

---

## 📋 Usage Guide

### Knapsack Problem

1. Navigate to the **Knapsack** page from the home screen.
2. Enter item **weights** as comma-separated values (e.g., `10, 20, 30`).
3. Enter corresponding **values** as comma-separated values (e.g., `60, 100, 120`).
4. Enter the **knapsack capacity** (e.g., `50`).
5. Click **Solve** — the app runs both Greedy and DP algorithms simultaneously.
6. View the side-by-side comparison:
   - Maximum value achieved by each approach
   - Items selected (with fractions for Greedy)
   - Execution time in milliseconds
   - Value difference between the two approaches

### Scheduling Problems

1. Navigate to the **Scheduling** page from the home screen.
2. Choose a problem type:

   **Activity Selection:**
   - Enter **start times** (e.g., `1, 3, 0, 5, 8, 5`)
   - Enter **finish times** (e.g., `2, 4, 6, 7, 9, 9`)
   - View the Gantt chart with selected activities highlighted

   **Job Scheduling with Deadlines:**
   - Enter **job IDs** (e.g., `J1, J2, J3, J4`)
   - Enter **deadlines** (e.g., `4, 1, 1, 1`)
   - Enter **profits** (e.g., `20, 10, 40, 30`)
   - View the time-slot assignment grid

   **Weighted Job Scheduling:**
   - Enter **job IDs** (e.g., `J1, J2, J3, J4`)
   - Enter **start times** (e.g., `1, 2, 3, 3`)
   - Enter **end times** (e.g., `3, 5, 4, 6`)
   - Enter **profits** (e.g., `5, 6, 5, 8`)
   - View the Gantt chart with optimal job subset highlighted

---

## 🏗️ Architecture

### Application Flow

```
User Input (Browser)
        │
        ▼
  ┌──────────┐     POST      ┌──────────────┐
  │  Template │ ────────────► │   views.py   │
  │  (HTML)   │               │              │
  └──────────┘               │  Parse Input  │
        ▲                     │  Validate     │
        │                     │  Run Algos    │
        │      GET            │  Store in     │
        │  (after redirect)   │  Session      │
        │                     └──────┬───────┘
        │                            │
        │     ┌──────────────────────┘
        │     │  PRG Redirect
        │     ▼
  ┌──────────┐               ┌──────────────┐
  │  Session  │ ◄──────────── │ algo_modules │
  │  Storage  │               │              │
  └──────────┘               │ • knapsack_  │
        │                     │   greedy.py  │
        │  Pop results        │ • knapsack_  │
        └─────────────────►   │   dp.py      │
              Render           │ • activity_  │
              Template         │   greedy.py  │
                              │ • job_       │
                              │   greedy.py  │
                              │ • weighted_  │
                              │   job_dp.py  │
                              └──────────────┘
```

### Design Patterns Used

| Pattern | Where | Purpose |
|---------|-------|---------|
| **PRG (Post-Redirect-Get)** | `views.py` | Prevents duplicate form submissions on page refresh |
| **Session Storage** | `views.py` | Decouples POST processing from GET rendering |
| **Strategy Pattern** | `algo_modules/` | Each algorithm is an independent, swappable module |
| **Template Inheritance** | `base.html` | Consistent layout across all pages |
| **MVC (MTV in Django)** | Project-wide | Model–Template–View separation |

### URL Routing

| URL Path | View Function | Template | Description |
|----------|--------------|----------|-------------|
| `/` | `home_view` | `home.html` | Landing page with problem cards |
| `/knapsack/` | `knapsack_view` | `knapsack.html` | Knapsack comparison tool |
| `/scheduling/` | `scheduling_view` | `scheduling.html` | All scheduling problems |

---

## � API Reference

### Algorithm Module Functions

Each algorithm module exposes a single function that accepts problem parameters and returns a standardized result dictionary.

#### `fractional_knapsack(weights, values, capacity)`
| Parameter | Type | Description |
|-----------|------|-------------|
| `weights` | `list[float]` | Item weights |
| `values` | `list[float]` | Item values |
| `capacity` | `float` | Knapsack capacity |
| **Returns** | `dict` | `max_value`, `selected_items`, `execution_time`, `time_complexity` |

#### `zero_one_knapsack(weights, values, capacity)`
| Parameter | Type | Description |
|-----------|------|-------------|
| `weights` | `list[float]` | Item weights (converted to int internally) |
| `values` | `list[float]` | Item values |
| `capacity` | `float` | Knapsack capacity (converted to int internally) |
| **Returns** | `dict` | `max_value`, `selected_items`, `execution_time`, `time_complexity` |

#### `activity_selection(start_times, finish_times)`
| Parameter | Type | Description |
|-----------|------|-------------|
| `start_times` | `list[int]` | Activity start times |
| `finish_times` | `list[int]` | Activity finish times |
| **Returns** | `dict` | `selected_count`, `selected_activities`, `all_activities`, `time_markers` |

#### `job_scheduling(job_ids, deadlines, profits)`
| Parameter | Type | Description |
|-----------|------|-------------|
| `job_ids` | `list[str]` | Job identifiers |
| `deadlines` | `list[int]` | Job deadlines |
| `profits` | `list[int]` | Job profits |
| **Returns** | `dict` | `total_profit`, `selected_jobs`, `schedule`, `max_deadline` |

#### `weighted_job_scheduling(job_ids, start_times, end_times, profits)`
| Parameter | Type | Description |
|-----------|------|-------------|
| `job_ids` | `list[str]` | Job identifiers |
| `start_times` | `list[int]` | Job start times |
| `end_times` | `list[int]` | Job end times |
| `profits` | `list[int]` | Job profits |
| **Returns** | `dict` | `max_profit`, `selected_jobs`, `all_jobs`, `time_markers` |

---

## 🤝 Contributing

Contributions are welcome! To add a new algorithm:

1. **Create a module** in `algorithms/algo_modules/` following the existing naming convention (`<name>_<paradigm>.py`).
2. **Implement a single function** that accepts problem inputs and returns a standardized dictionary with:
   - Result values (e.g., `max_value`, `max_profit`)
   - `execution_time` (measured via `time.perf_counter()`)
   - `time_complexity` and `space_complexity` strings
   - `algorithm_type` (e.g., `'Greedy'` or `'Dynamic Programming'`)
3. **Import the function** in `views.py` and create the corresponding view logic.
4. **Add a URL route** in `algorithms/urls.py`.
5. **Create or update templates** in `algorithms/templates/`.

---

## 📝 License

This project is developed for **educational purposes** as part of the Semester 5 **Design & Analysis of Algorithms** course. It is free to use for learning and academic reference.

---

## � Acknowledgements

- **Django Documentation** — [docs.djangoproject.com](https://docs.djangoproject.com/)
- **Bootstrap 5** — [getbootstrap.com](https://getbootstrap.com/)
- **Introduction to Algorithms (CLRS)** — For algorithm theory and pseudocode reference
- **Google Fonts (Outfit)** — Typography

---

<p align="center">
  Made with ❤️ for <strong>Design & Analysis of Algorithms</strong>
</p>
