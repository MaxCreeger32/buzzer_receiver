# #initialisation
radio.set_frequency_band(83)
radio.set_group(10)
radio.set_transmit_power(7)
is_question= False
preums = "?"
def on_forever():
    if not is_question :
        basic.show_icon(IconNames.ASLEEP)
    else :
        basic.show_string(preums)
    pass
basic.forever(on_forever)


# valide la réponse
def on_button_pressed_a():
    global is_question,preums
    if is_question:
        radio.send_value(preums, 1)
        preums = "?"
        is_question=True
        basic.show_string(preums)
input.on_button_pressed(Button.A, on_button_pressed_a)

# annule la réponse
def on_button_pressed_b():
    global is_question,preums
    if is_question:
        radio.send_value(preums, 0)
        preums = "?"
        is_question=True
        basic.show_string(preums)
input.on_button_pressed(Button.B, on_button_pressed_b)

#reset du receveur
def on_button_pressed_ab():
    global is_question,preums
    is_question=True
    preums="?"
    basic.show_string(preums)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_value(name, value):
    global is_question,preums
    if is_question and preums == "?":
        preums = name
    basic.show_string(preums)
radio.on_received_value(on_received_value)

def on_gesture_shake():
    radio.send_value("ALL", 0)
    basic.show_string(preums)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

