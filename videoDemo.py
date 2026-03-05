# Reminders Microservice
# Video Demo Program

import requests
import time

# Start by creating a new reminder
response = requests.post(
    "http://localhost:8000/reminders",
    json={"message": "Team meeting 2", "date": "02-26-2026"}
)
print("Created:", response.json())
# TEST PROGRAM SHOWS: <Created: reminder as json object>
# MICROSERVICE SHOWS: <POST /reminders HTTP/1.1" 201>

# pause between actions
time.sleep(3)

# *Test program programmatically requesting data from the microservice.
#   Get all reminders
response = requests.get("http://localhost:8000/reminders")

# pause between actions
time.sleep(3)

# # *The microservice programmatically responding with data.
# MICROSERVICE SHOWS: <GET /reminders HTTP/1.1" 200>

# *Test program programmatically receiving data from the microservice.
print("\nAll reminders:", response.json())
# TEST PROGRAM SHOWS: <all reminders as json object>
