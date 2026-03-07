import requests

# Create a reminder
response = requests.post(
    "http://localhost:8000/reminders",
    json={"message": "Team meeting", "date": "05-30-2026"}
)
print("Created:", response.json())

# Get all reminders
response = requests.get("http://localhost:8000/reminders")
print("All reminders:", response.json())

# Delete a reminder (use actual ID from create response)
reminder_id = "r_a1b2c3d4"  # Replace with actual ID
response = requests.delete(f"http://localhost:8000/reminders/{reminder_id}")
print("Delete result:", response.json())

# Test invalid reminder creation (missing fields)
response = requests.post(
    "http://localhost:8000/reminders",
    json={"message": "Invalid reminder"}
)
print("Invalid create response, no date:", response.json())

# Test invalid date format
response = requests.post(
    "http://localhost:8000/reminders",
    json={"message": "Invalid date format", "date": "2026-05-01"}
)
print("Invalid date format response:", response.json())

# Test past reminder
response = requests.post(
    "http://localhost:8000/reminders",
    json={"message": "Past reminder", "date": "01-01-2020"}
)
print("Past reminder response:", response.json())

# Test no message:
response = requests.post(
    "http://localhost:8000/reminders",
    json={"date": "04-30-2026"}
)
print("No message response:", response.json())
