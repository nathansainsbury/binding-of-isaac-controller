from pyautogui import press

class Controller:

    def __init__(self):
        self.commands = []
        self.console_is_open = False

    def set_command(self, command):
        self.commands.append(command)

    # shoot
    def shoot_left(self):
        press('left')
        self.set_command('shoot_left')

    def shoot_right(self):
        press('right')
        self.set_command('shoot_right')

    def shoot_up(self):
        press('up')
        self.set_command('shoot_up')

    def shoot_down(self):
        press('down')
        self.set_command('shoot_down')

    # move
    def move_left(self):
        press('a')
        self.set_command('move_left')

    def move_right(self):
        press('d')
        self.set_command('move_right')

    def move_up(self):
        press('w')
        self.set_command('move_up')

    def move_down(self):
        press('s')
        self.set_command('move_down')

    # items
    def use_item(self):
        press('space')
        self.set_command('use_item')

    def place_bomb(self):
        press('e')
        self.set_command('place_bomb')
    
    # boi debug console
    def toggle_console(self):
        press('`')
        self.console_is_open = not self.console_is_open
        self.set_command('toggle_console')

    def open_console(self):
        if not self.console_is_open:
            press('`')
            self.console_is_open = True
            self.set_command('open_console')

    def close_console(self):
        if self.console_is_open:
            press('`')
            self.console_is_open = False
            self.set_command('close_console')

    def command(self, command):
        self.open_console()
        typewrite(command)
        self.set_command('write_command')
