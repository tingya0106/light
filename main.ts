let x3 = 0
let y = 0
let x2 = 0
function _2 () {
    basic.showLeds(`
        # # # # #
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        # # # # #
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
}
input.onButtonPressed(Button.A, function () {
    _1()
})
function _3 () {
    x3 = 4
    for (let index = 0; index < 5; index++) {
        y = 4
        for (let y = 0; y <= 4; y++) {
            basic.clearScreen()
            led.plot(x3, y)
            basic.pause(200)
            y += 0 - -1
        }
        x3 += -1
        basic.clearScreen()
    }
}
input.onButtonPressed(Button.AB, function () {
    for (let index = 0; index < 4; index++) {
        _2()
        _1()
        _3()
    }
})
input.onButtonPressed(Button.B, function () {
    _2()
})
function _1 () {
    x2 = 0
    for (let index = 0; index < 5; index++) {
        y = 0
        for (let y = 0; y <= 4; y++) {
            basic.clearScreen()
            led.plot(x2, y)
            basic.pause(200)
            y += 1
        }
        x2 += 1
        basic.clearScreen()
    }
}
