import requests

# Create a reminder
response = requests.post(
    "http://localhost:8000/reminders",
    json={"message": "Team meeting", "date": "02-25-2026"}
)
print("Created:", response.json())

# Get all reminders
response = requests.get("http://localhost:8000/reminders")
print("All reminders:", response.json())

# Delete a reminder (use actual ID from create response)
reminder_id = "r_a1b2c3d4"  # Replace with actual ID
response = requests.delete(f"http://localhost:8000/reminders/{reminder_id}")
print("Delete result:", response.json())