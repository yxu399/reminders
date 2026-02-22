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
## Request Data

Submit a new reminder by POSTing a JSON object
Request all reminders by sending a GET request
Request one reminder by sending a GET request with the reminder ID
Delete one reminder by sending a DELETE request with the reminder ID

## Request Data - Example Calls
##  Record a new reminder
```
response = requests.post(
    "http://localhost:8000/reminders",
    json={"message": "Team meeting 2", "date": "02-26-2026"}
)
```

## Request all reminders
```
response = requests.get("http://localhost:8000/reminders")
```

## Request one reminder
```
response = requests.get("http://localhost:8000/reminders/{reminder_id}")
```

## Delete one reminder
```
response = requests.delete("http://localhost:8000/reminders/{reminder_id}")
```

## Receiving Data
Receive data back for requesting all reminders or one reminder in a JSON object.
Store that object in a variable.
## Receive all reminders, store JSON object in response variable
```
responseAllReminders = requests.get("http://localhost:8000/reminders")
```

## Request one reminder, store JSON object in response variable
```
responeOneReminder = requests.get("http://localhost:8000/reminders/{reminder_id}")
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

## UML Diagram

![Reminder Microservice UML](https://github.com/user-attachments/assets/9431b6f2-1dbb-4364-91e5-4b1995fb483f)

