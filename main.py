x3 = 0
y = 0
x2 = 0
def _2():
    basic.show_leds("""
        # # # # #
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                # # # # #
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                # # # # #
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                # # # # #
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # # # # #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)

def on_button_pressed_a():
    _1()
input.on_button_pressed(Button.A, on_button_pressed_a)

def _3():
    global x3, y
    x3 = 4
    for index in range(5):
        y = 4
        for y2 in range(5):
            basic.clear_screen()
            led.plot(x3, y2)
            basic.pause(200)
            y2 += 0 - -1
        x3 += -1
        basic.clear_screen()

def on_button_pressed_ab():
    for index2 in range(4):
        _2()
        _1()
        _3()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    _2()
input.on_button_pressed(Button.B, on_button_pressed_b)

def _1():
    global x2, y
    x2 = 0
    for index3 in range(5):
        y = 0
        for y3 in range(5):
            basic.clear_screen()
            led.plot(x2, y3)
            basic.pause(200)
            y3 += 1
        x2 += 1
        basic.clear_screen()