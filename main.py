from flask import Flask, request, jsonify
import json
import os
from datetime import datetime
import uuid

app = Flask(__name__)

# ##### SET UP DATA STORAGE AND HELPER FUNCTIONS ##############################

# File to store reminders
DATA_FILE = 'reminders.json'


# Initialize data file if it doesn't exist
def init_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)


# Load reminders from file
def load_reminders():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        return []


# Save reminders to file
def save_reminders(reminders):
    with open(DATA_FILE, 'w') as f:
        json.dump(reminders, f, indent=2)


# Validate date format (MM-DD-YYYY)
def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%m-%d-%Y')
        return True
    except:
        return False


# Check if date is in the past
def is_past_date(date_str):
    try:
        reminder_date = datetime.strptime(date_str, '%m-%d-%Y')
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        return reminder_date < today
    except:
        return False


# Check if date is in the future or today
def is_active_reminder(date_str):
    try:
        reminder_date = datetime.strptime(date_str, '%m-%d-%Y')
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        return reminder_date >= today
    except:
        return False


# Validate data
def validate_data(data):
    # Check if message is provided
    if not data or 'message' not in data:
        return jsonify({'error': 'Message is required'}), 400

    # Check if date is provided
    if 'date' not in data:
        return jsonify({'error': 'Date is required'}), 400

    # Validate date format
    if not validate_date(data['date']):
        return jsonify({'error': 'Invalid date format. Use MM-DD-YYYY'}), 400

    return None


# Build reminder object with unique ID and status
def build_reminder(data):
    # Generate unique ID
    reminder_id = 'r_' + str(uuid.uuid4())[:8]

    # Create reminder object
    reminder = {
        'id': reminder_id,
        'message': data['message'],
        'date': data['date'],
        'status': 'active'
    }

    # Check if date is in the past and add warning
    if is_past_date(data['date']):
        reminder['warning'] = 'Date is in the past'

    return reminder

# ##### DEFINE API ENDPOINTS #################################################


# CREATE: POST /reminders
@app.route('/reminders', methods=['POST'])
def create_reminder():
    data = request.get_json()

    # Validate data received from client
    data_error = validate_data(data)
    if data_error:
        return data_error

    # Build reminder object with unique ID and status
    reminder = build_reminder(data)

    # Load existing reminders, add new one, and save
    reminders = load_reminders()
    reminders.append(reminder)
    save_reminders(reminders)

    return jsonify(reminder), 201


# READ ALL: GET /reminders
@app.route('/reminders', methods=['GET'])
def get_all_reminders():
    reminders = load_reminders()

    # Filter to only active (future or today) reminders
    active_reminders = [r for r in reminders if is_active_reminder(r['date'])]

    # Sort by date (earliest first)
    active_reminders.sort(key=lambda x: datetime.strptime(x['date'], '%m-%d-%Y'))

    # return active reminders
    return jsonify(active_reminders), 200


# READ ONE: GET /reminders/<id>
@app.route('/reminders/<reminder_id>', methods=['GET'])
def get_reminder(reminder_id):
    reminders = load_reminders()

    # Find reminder by ID
    reminder = next((r for r in reminders if r['id'] == reminder_id), None)

    if reminder is None:
        return jsonify({'error': 'Reminder not found'}), 404

    return jsonify(reminder), 200


# DELETE: DELETE /reminders/<id>
@app.route('/reminders/<reminder_id>', methods=['DELETE'])
def delete_reminder(reminder_id):
    reminders = load_reminders()

    # Find reminder by ID
    reminder = next((r for r in reminders if r['id'] == reminder_id), None)

    if reminder is None:
        return jsonify({'error': 'Reminder not found'}), 404

    # Remove reminder and save
    reminders = [r for r in reminders if r['id'] != reminder_id]
    save_reminders(reminders)

    return jsonify({'message': 'Reminder deleted successfully'}), 200


# Initialize data file on startup
init_data_file()

if __name__ == '__main__':
    print("Reminder Microservice starting on http://localhost:8000")
    app.run(host='0.0.0.0', port=8000, debug=True)
