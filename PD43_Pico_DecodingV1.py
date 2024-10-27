import machine
import time
from machine import UART, Pin

# Set up UART communication
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Set up the LED pins
f1 = Pin(9, Pin.OUT)
f2 = Pin(10, Pin.OUT)
f3 = Pin(11, Pin.OUT)
f4 = Pin(12, Pin.OUT)
f5 = Pin(14, Pin.OUT)
f6 = Pin(15, Pin.OUT)

s1 = Pin(27, Pin.OUT)
s2 = Pin(26, Pin.OUT) 
s3 = Pin(22, Pin.OUT) 
s4 = Pin(21, Pin.OUT) 
s5 = Pin(20, Pin.OUT) 
s6 = Pin(19, Pin.OUT) 

def turn_all_off():
    """Turn off all LEDs and pins."""
    f1.value(0)
    f2.value(0)
    f3.value(0)
    f4.value(0)
    f5.value(0)
    f6.value(0)
    s1.value(0)
    s2.value(0)
    s3.value(0)
    s4.value(0)
    s5.value(0)
    s6.value(0)

def turn_on_combination(combination):
    """Turn on the specified lights based on the combination."""
    turn_all_off()  # Turn off all lights first

    for pin in combination:
        pin.value(1)  # Turn on the specified pins

def get_combinationL(letterL):
    """Return the combination of pins to light up for a given letter."""
    case_statements = {
        'A': [f1],
        'B': [f1, f2],
        'C': [f1, f4],
        'D': [f1, f4, f5],
        'E': [f1, f5],
        'F': [f1, f2, f4],
        'G': [f1, f2, f4, f5],
        'H': [f1, f2, f5],
        'J': [f2, f4, f5],
        'K': [f1, f3],
        'L': [f1, f2, f3],
        'M': [f1, f3, f4],
        'N': [f1, f3, f4, f5],
        'Ñ': [f4, s1, s3, s4, s5],
        'O': [f1, f3, f5],
        'P': [f1, f2, f3, f4],
        'Q': [f1, f2, f3, f4, f5],
        'R': [f1, f2, f3, f5],
        'S': [f2, f3, f4],
        'T': [f2, f3, f4, f5],
        'U': [f1, f3, f6],
        'V': [f1, f2, f3, f6],
        'W': [f2, f4, f5, f6],
        'X': [f1, f3, f4, f6],
        'Y': [f1, f3, f4, f5, f6],
        'Z': [f1, f3, f5, f6],
    }
    return case_statements.get(letterL.upper(), [])  # Return empty if letter not found

def get_combinationR(letterR):
    """Return the combination of pins to light up for a given letter."""
    case_statements = {
        'A': [s1],
        'B': [s1, s2],
        'C': [s1, s4],
        'D': [s1, s4, s5],
        'E': [s1, s5],
        'F': [s1, s2, s4],
        'G': [s1, s2, s4, s5],
        'H': [s1, s2, s5],
        'J': [s2, s4, s5],
        'K': [s1, s3],
        'L': [s1, s2, s3],
        'M': [s1, s3, s4],
        'N': [s1, s3, s4, s5],
        'Ñ': [f4, f1, f3, s4, s5],
        'O': [s1, s3, s5],
        'P': [s1, s2, s3, f4],
        'Q': [s1, s2, s3, f4, f5],
        'R': [s1, s2, s3, f5],
        'S': [s2, s3, s4],
        'T': [s2, s3, s4, f5],
        'U': [s1, s3, s6],
        'V': [f1, s2, s3, s6],
        'W': [s2, s4, s5, s6],
        'X': [s1, s3, s4, s6],
        'Y': [s1, s3, s4, s5, s6],
        'Z': [s1, s3, s5, s6],
    }
    return case_statements.get(letterR.upper(), [])  # Return empty if letter not found

# Main loop for receiving UART data
while True:
    if uart.any():  # Check if any data is available
        data = uart.read(2)  # Read 2 bytes (cell and letter)
        if data:
            cell_to_light = data[0]  # '0' or '1' as a byte
            letter_to_light = chr(data[1]).upper()  # 'A'-'Z' or 'Ñ'

            print(f"Received: Cell={cell_to_light}, Letter={letter_to_light}")

            # Get the combination for the entered letter based on the selected cell
            if cell_to_light == 48:  # Use '1' for left
                combination = get_combinationL(letter_to_light)
            else:  # Use '0' for right
                combination = get_combinationR(letter_to_light)

            # Turn on the lights for the given combination
            turn_on_combination(combination)

            # Keep the lights on for a while
            time.sleep(1)  # Duration for lights to stay on

            # Turn off all LEDs again
            turn_all_off()  # Reset all lights to off

