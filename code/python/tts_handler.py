import pyttsx3
import serial

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Establish serial connection with Arduino
ser = serial.Serial('COM3', 9600)  # Update COM port as needed

# Mapping of RFID tag IDs to location descriptions
rfid_locations = {
    'a1b2c3d4': 'You are at the main entrance.',
    'e5f6g7h8': 'You are near the information desk.',
    # Add more mappings as needed
}

while True:
    if ser.in_waiting > 0:
        rfid_tag = ser.readline().decode('utf-8').strip()
        location = rfid_locations.get(rfid_tag, 'Unknown location.')
        engine.say(location)
        engine.runAndWait()
