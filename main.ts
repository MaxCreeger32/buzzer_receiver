//  #initialisation
radio.setFrequencyBand(83)
radio.setGroup(10)
radio.setTransmitPower(7)
let is_question = false
let preums = "?"
basic.forever(function on_forever() {
    if (!is_question) {
        basic.showIcon(IconNames.Asleep)
    } else {
        basic.showString(preums)
    }
    
    
})
//  valide la réponse
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (is_question) {
        radio.sendValue(preums, 1)
        preums = "?"
        is_question = true
        basic.showString(preums)
    }
    
})
//  annule la réponse
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (is_question) {
        radio.sendValue(preums, 0)
        preums = "?"
        is_question = true
        basic.showString(preums)
    }
    
})
// reset du receveur
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    is_question = true
    preums = "?"
    basic.showString(preums)
})
radio.onReceivedValue(function on_received_value(name: string, value: number) {
    
    if (is_question && preums == "?") {
        preums = name
    }
    
    basic.showString(preums)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    radio.sendValue("ALL", 0)
    basic.showString(preums)
})
