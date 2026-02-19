# Reminder Microservice

A simple REST API microservice for creating, retrieving, and deleting reminders. Built with Flask and JSON file storage.


## Features

- Create reminders with custom messages and dates
- Retrieve all active (future/today) reminders
- Retrieve specific reminders by ID
- Delete reminders
- Persistent storage (survives restarts)
- Warns when dates are in the past
- Returns reminders sorted by date


## Installation

1. Clone or download this repository

2. Install dependencies:
```bash
pip install Flask
```

## Running the Microservice

Start the microservice:
```bash
python main.py
```

The service will start on `http://localhost:8000`

You should see:
```
Reminder Microservice starting on http://localhost:8000
 * Running on http://0.0.0.0:8000
```


## Data Storage

Reminders are stored in `reminders.json` in the same directory as `main.py`. This file is created automatically on first run.

**Example `reminders.json`:**
```json
[
  {
    "id": "r_a1b2c3d4",
    "message": "Submit homework",
    "date": "03-15-2026",
    "status": "active"
  },
  {
    "id": "r_b2c3d4e5",
    "message": "Team meeting",
    "date": "02-25-2026",
    "status": "active"
  }
]
```



## Error Handling

The microservice validates:
- Missing `message` field → 400 error
- Missing `date` field → 400 error
- Invalid date format → 400 error
- Non-existent reminder ID → 404 error

## Notes

- Date format must be MM-DD-YYYY (e.g., "03-15-2026")
- Reminders with past dates are accepted but include a warning
- GET /reminders only returns future/today reminders (past reminders are filtered out)
- Reminder IDs are automatically generated as "r_" followed by 8 random characters
- The microservice runs on port 8000 by default

