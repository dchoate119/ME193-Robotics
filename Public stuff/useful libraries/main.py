"""
Install first:
    pip install legoeducation
Then copy lelib.py from the SimpleLE repo into this project's folder.

"""

import time

import legoeducation as le
from lelib import colorSensor, controller, singleMotor, doubleMotor

# --- Bluetooth card info for your hardware -------------------------------
# Fill these in with the color/serial printed on your LEGO connection card.
# Valid values: le.LEGO_COLOR_RED, _YELLOW, _BLUE, _GREEN, _PURPLE,
# _MAGENTA, _AZURE, _ORANGE.
COLOR_SENSOR_CARD_COLOR = le.LEGO_COLOR_MAGENTA
COLOR_SENSOR_CARD_SERIAL = "0998"

CONTROLLER_CARD_COLOR = le.LEGO_COLOR_MAGENTA
CONTROLLER_CARD_SERIAL = "0998"

SINGLE_MOTOR_CARD_COLOR = le.LEGO_COLOR_MAGENTA
SINGLE_MOTOR_CARD_SERIAL = "0998"

DOUBLE_MOTOR_CARD_COLOR = le.LEGO_COLOR_MAGENTA
DOUBLE_MOTOR_CARD_SERIAL = "0998"

POLL_DELAY_S = 0.1  # seconds between reads

# Motors are module-level so the Do* handlers below can use them,
# e.g. sm.run(50) or dm.turn_left(90). They're connected in main().
sm = singleMotor()
dm = doubleMotor()



# --- Empty handler functions ----------------------------------------------
# Fill these in with whatever behavior you want.

def DoRed():
    print("red")



def DoYellow():
    print("yellow")



def DoBlue():
    print("blue")



def DoTeal():
    pass



def DoGreen():
    pass



def DoPurple():
    pass



def DoWhite():
    pass



def DoMagenta():
    pass



def DoOrange():
    # Stop driving and spin the single motor (e.g. an arm or flag).
    print("orange")
    dm.stop()
    sm.run(50)



def DoAzure():
    # Stop the single motor and drive forward.
    print("azure")
    sm.stop()
    dm.run(50)



def DoNoColor():
    pass



def DoUnknownColor():
    pass



def DoLeftUp():
    pass



def DoLeftDown():
    # Emergency stop: halt both motors.
    print("left down: stop")
    sm.stop()
    dm.stop()



def DoLeftReleased():
    pass



def DoRightUp():
    pass



def DoRightDown():
    pass



def DoRightReleased():
    pass



# --- Dispatch helpers -------------------------------------------------

def handle_color(color_name):
    """Big switch statement on the color sensor's detected color."""
    match color_name:
        case "Red":
            DoRed()
        case "Yellow":
            DoYellow()
        case "Blue":
            DoBlue()
        case "Teal":
            DoTeal()
        case "Green":
            DoGreen()
        case "Purple":
            DoPurple()
        case "White":
            DoWhite()
        case "Magenta":
            DoMagenta()
        case "Orange":
            DoOrange()
        case "Azure":
            DoAzure()
        case "No color":
            DoNoColor()
        case _:
            DoUnknownColor()



def handle_controller(ctl):
    """Big switch statement on the controller's joystick state."""
    if ctl.left_up():
        left_state = "up"
    elif ctl.left_down():
        left_state = "down"
    else:
        left_state = "released"

    if ctl.right_up():
        right_state = "up"
    elif ctl.right_down():
        right_state = "down"
    else:
        right_state = "released"

    match left_state:
        case "up":
            DoLeftUp()
        case "down":
            DoLeftDown()
        case "released":
            DoLeftReleased()

    match right_state:
        case "up":
            DoRightUp()
        case "down":
            DoRightDown()
        case "released":
            DoRightReleased()



# --- Main loop -------------------------------------------------------------

def main():
    sensor = colorSensor()
    sensor.connect(card_serial=COLOR_SENSOR_CARD_SERIAL, card_color=COLOR_SENSOR_CARD_COLOR)

    ctl = controller()
    ctl.connect(card_serial=CONTROLLER_CARD_SERIAL, card_color=CONTROLLER_CARD_COLOR)

    sm.connect(card_serial=SINGLE_MOTOR_CARD_SERIAL, card_color=SINGLE_MOTOR_CARD_COLOR)
    dm.connect(card_serial=DOUBLE_MOTOR_CARD_SERIAL, card_color=DOUBLE_MOTOR_CARD_COLOR)

    try:
        while True:
            handle_color(sensor.detect_color())
            handle_controller(ctl)
            time.sleep(POLL_DELAY_S)
    except KeyboardInterrupt:
        pass
    finally:
        sm.stop()
        dm.stop()



if __name__ == "__main__":
    main()
