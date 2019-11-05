import toga
from colosseum import CSS
import Dice_Roller

BASECHARS = {'barb':{'name':'barb'},
            'wiz': {'name': 'wiz'},
            'elf': {'name': 'elf'},
            'cleric': {'name': 'cleric'}}

TEST_SET = {
    'dice_string': '3d6+5',
    'rolls': [3,5,2],
    'mods': [5],
    'total': 15,
}

        
def button_handler(widget):
    print('Hello World!')




def build(app):
    main_box = toga.Box()
    button_style = CSS(flex_direction = 'row', padding = 0)
    app_style = CSS(flex_direction = 'column', width = 100)


    def numbers_input(button):
        text_input.value += button.label
        print(button.label)

    def roll_dice(button):
        TEST_SET = Dice_Roller.dice_main(text_input.value)
        text_input.value = ''
        totals_label.text = TEST_SET['total']
        extra_label.text = TEST_SET['mods']
        results_label.text = TEST_SET['rolls']



    # Create buttons for buttons_box
    one_button = toga.Button('1', on_press = numbers_input)
    two_button = toga.Button('2', on_press = numbers_input)
    three_button = toga.Button('3', on_press = numbers_input)
    four_button = toga.Button('4', on_press = numbers_input)
    five_button = toga.Button('5', on_press = numbers_input)
    six_button = toga.Button('6', on_press = numbers_input)
    seven_button = toga.Button('7', on_press = numbers_input)
    eight_button = toga.Button('8', on_press = numbers_input)
    nine_button = toga.Button('9', on_press = numbers_input)
    zero_button = toga.Button('0', on_press = numbers_input)
    plus_button = toga.Button('+', on_press = numbers_input)
    minus_button = toga.Button('-', on_press = numbers_input)
    d_button = toga.Button('d', on_press = numbers_input)
    roll_button = toga.Button('Roll', on_press = roll_dice)
    
    # Create Buttons Box
    numbers_row_1 = toga.Box(style = button_style, children = [one_button, two_button, three_button])
    numbers_row_2 = toga.Box(style = button_style, children = [four_button, five_button, six_button])
    numbers_row_3 = toga.Box(style = button_style, children = [seven_button, eight_button, nine_button])

    buttons_right_top = toga.Box(style= button_style, children = [zero_button, plus_button])
    buttons_right_middle = toga.Box(style = button_style, children = [d_button, minus_button])

    buttons_left = toga.Box(children = [numbers_row_1, numbers_row_2, numbers_row_3])
    buttons_right = toga.Box(children = [buttons_right_top, buttons_right_middle, roll_button])

    # Create Input Box
    text_input = toga.TextInput(readonly = True )


    # Create items for display_box
    totals_label = toga.Label('totals', alignment=toga.LEFT_ALIGNED)
    extra_label = toga.Label('extra', alignment=toga.LEFT_ALIGNED)
    results_label = toga.Label('results', alignment = toga.RIGHT_ALIGNED)
    display_left_box = toga.Box(children = [totals_label, extra_label])


    # Create boxes for sc
    # reen grouping
    menu_box = toga.Box()
    display_box = toga.Box(style = button_style, children = [display_left_box, results_label])
    input_box = toga.Box(children = [text_input])
    input_box.add(text_input)
    buttons_box = toga.Box(style = button_style, children = [buttons_left, buttons_right])

    app_screen = toga.Box(children = [display_box, input_box, buttons_box])
    app_screen.style.set(padding_top = 20, width = 200)


    return app_screen

def main():
    return toga.App('First App', 'dice_app', startup = build)

if __name__ == '__main__':
    main().main_loop()