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


# *Test program and microservice are not directly calling each other (show code).
# TEST PROGRAM: Show no imports, no function calls to microservice code.
# MICROSERVICE: Show no imports, no function calls to test program code.
# SHOW WEB BROWSER AT ENDPOINT: http://localhost:8000/reminders

# **********************************************************************

# *README describes how to request data from the microservice.
# *README has an example call for requesting data.
# *README describes how to receive data from the microservice.
# *README has an example call for receiving data.
# *README has a UML sequence diagram that communicates how to request and receive data from the microservice.

# *UML diagram has no obvious notational errors.
