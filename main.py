y = 0
x = 0

def on_button_pressed_a():
    global y, x
    y = 0
    for index in range(5):
        x = 0
        for x2 in range(5):
            basic.clear_screen()
            led.plot(x2, y)
            basic.pause(100)
            x2 += 1
        y += 1
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global y, x
    y = 4
    for index2 in range(5):
        x = 4
        for x3 in range(5):
            basic.clear_screen()
            led.plot(x3, y)
            basic.pause(200)
            x3 -= -1
        y += -1
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
