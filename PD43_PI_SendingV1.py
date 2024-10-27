import serial
import time

# Set up the serial connection
# The serial port name might be different depending on your setup
# For example, /dev/ttyS0 or /dev/serial0 may be used for UART on the Raspberry Pi
ser = serial.Serial('/dev/ttyAMA0', baudrate=9600, timeout=1)

def send_data(cell, letter):
    """Send the cell and letter data to the Pico."""
    # Format the data as a string, e.g., '1A' or '0B'
    data = f"{cell}{letter}"
    ser.write(data.encode())  # Send the encoded data over UART
    print(f"Sent: {data}")

def main():
    while True:
        # Get user input for which cell to light up
        cell_to_light = input("Which cell do you want to light up? (1 for L, 0 for R): ")
        if cell_to_light not in ['0', '1']:
            print("Invalid input. Please enter 1 for L or 0 for R.")
            continue

        # Get user input for the letter to light up
        letter_to_light = input("Enter a letter (A-Z, Ñ) to light up: ").upper()
        if len(letter_to_light) != 1 or not (letter_to_light.isalpha() or letter_to_light == 'Ñ'):
            print("Invalid input. Please enter a valid letter (A-Z, Ñ).")
            continue

        # Send the data to the Pico
        send_data(cell_to_light, letter_to_light)

        # Add a small delay to avoid sending data too quickly
        time.sleep(1)

if _name_ == "_main_":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated.")
    finally:
        # Close the serial connection
        if ser.is_open:
            ser.close()