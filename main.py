def on_forever():
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
    music.play(music.string_playable("C D E F G A B C5 ", 120),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    basic.show_leds("""
        # . # # #
        # . # . #
        # . # . #
        # . # . #
        # . # # #
        """)
    basic.show_leds("""
        # # # . .
        # . # . .
        # # # . .
        . . # . .
        # # # . .
        """)
    basic.show_leds("""
        # # # . .
        # . # . .
        # # # . .
        # . # . .
        # # # . .
        """)
    basic.show_leds("""
        # # # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        """)
    basic.show_leds("""
        # # # . .
        # . . . .
        # # # . .
        # . # . .
        # # # . .
        """)
    basic.show_leds("""
        # # # . .
        # . . . .
        # # # . .
        . . # . .
        # # # . .
        """)
    basic.show_leds("""
        # . # . .
        # . # . .
        # # # . .
        . . # . .
        . . # . .
        """)
    basic.show_leds("""
        # # # . .
        . . # . .
        . # # . .
        . . # . .
        # # # . .
        """)
    basic.show_leds("""
        # # # . .
        . . # . .
        # # # . .
        # . . . .
        # # # . .
        """)
    basic.show_leds("""
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . # # # .
        . # . # .
        """)
    basic.show_leds("""
        . . . . .
        . . # . .
        . # # # .
        . # . # .
        . . . . .
        """)
    basic.show_leds("""
        . . # . .
        . # # # .
        . # . # .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . # # # .
        . # . # .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . # . # .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
basic.forever(on_forever)