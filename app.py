from flask import Flask, request, jsonify, render_template
from enum import Enum

app = Flask(__name__)

# Enum for Room Types
class RoomType(Enum):
    STANDARD = "Standard Room"
    DELUXE = "Deluxe Room"
    FAMILY_SUITE = "Family Suite"
    EXECUTIVE_SUITE = "Executive Suite"

# Mock data for rooms using the enum
rooms = [
    {"id": 1, "type": RoomType.STANDARD.value, "price": 99.99, "is_available": False},
    {"id": 2, "type": RoomType.DELUXE.value, "price": 149.99, "is_available": True},
    {"id": 3, "type": RoomType.FAMILY_SUITE.value, "price": 199.99, "is_available": False},
    {"id": 4, "type": RoomType.EXECUTIVE_SUITE.value, "price": 249.99, "is_available": True},
    {"id": 5, "type": RoomType.STANDARD.value, "price": 99.99, "is_available": True},
]

# Mock data for bookings
bookings = [
    {
        "id": 1,
        "room_id": 1,
        "customer_name": "John Doe",
        "check_in_date": "2024-11-01",
        "check_out_date": "2024-11-05"
    },
    {
        "id": 2,
        "room_id": 3,
        "customer_name": "Jane Smith",
        "check_in_date": "2024-11-03",
        "check_out_date": "2024-11-07"
    }
]

# Admin password (for simplicity)
ADMIN_PASSWORD = "admin123"

@app.route('/')
def index():
    return render_template('index.html', rooms=rooms, bookings=bookings)

# READ: Get available or unavailable rooms
@app.route('/rooms', methods=['GET'])
def get_rooms():
    available = request.args.get('available', 'true').lower() == 'true'
    filtered_rooms = [room for room in rooms if room["is_available"] == available]
    return jsonify(filtered_rooms)

# READ: Get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    return jsonify(bookings)

# CREATE: Add a new room (admin only)
@app.route('/rooms', methods=['POST'])
def add_room():
    data = request.get_json()
    password = data.get("admin_password")

    if password != ADMIN_PASSWORD:
        return jsonify({"error": "Unauthorized access"}), 403

    new_room = {
        "id": len(rooms) + 1,
        "type": data.get("type"),
        "price": data.get("price"),
        "is_available": True
    }

    if not new_room["type"] or not new_room["price"]:
        return jsonify({"error": "Invalid room data"}), 400

    rooms.append(new_room)
    return jsonify(new_room), 201

# CREATE: Book a room by type
@app.route('/bookings', methods=['POST'])
def create_booking():
    new_booking = request.get_json()
    chosen_type = new_booking.get("room_type")
    customer_name = new_booking.get("customer_name")
    check_in_date = new_booking.get("check_in_date")
    check_out_date = new_booking.get("check_out_date")

    available_room = next((room for room in rooms if room["type"] == chosen_type and room["is_available"]), None)

    if not available_room:
        return jsonify({"error": "No available rooms of the selected type"}), 400

    booking_id = len(bookings) + 1
    new_booking = {
        "id": booking_id,
        "room_id": available_room["id"],
        "customer_name": customer_name,
        "check_in_date": check_in_date,
        "check_out_date": check_out_date
    }
    bookings.append(new_booking)
    available_room["is_available"] = False

    return jsonify(new_booking), 201

if __name__ == '__main__':
    app.run(debug=True)
