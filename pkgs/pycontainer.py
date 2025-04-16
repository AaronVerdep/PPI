import curses

class PyContainer:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.windows = []
        self.cursor_x = 1
        self.cursor_y = 1
        self.selected_window = None
        self.running = True

        curses.curs_set(0)  # Ocultar el cursor
        self.stdscr.keypad(1)  # Habilitar teclas especiales
        self.stdscr.timeout(100)  # Timeout para lectura no bloqueante

    def screen(self):
        # Pantalla principal
        while self.running:
            self.stdscr.clear()
            self.stdscr.addstr(self.cursor_y, self.cursor_x, 'X', curses.A_BOLD)
            for window in self.windows:
                window.draw(self.stdscr)
            self.stdscr.refresh()
            self.handle_input()

    def handle_input(self):
        key = self.stdscr.getch()

        if key == curses.KEY_UP:
            if self.cursor_y > 1:
                self.cursor_y -= 1
        elif key == curses.KEY_DOWN:
            self.cursor_y += 1
        elif key == curses.KEY_LEFT:
            if self.cursor_x > 1:
                self.cursor_x -= 1
        elif key == curses.KEY_RIGHT:
            self.cursor_x += 1
        elif key == 10:  # Enter
            self.check_click()
        elif key == 27:  # Escape to quit
            self.running = False

    def check_click(self):
        # Verifica si el cursor está sobre una ventana y clickea en la X
        for window in self.windows:
            if window.contains(self.cursor_x, self.cursor_y):
                if window.is_close_button(self.cursor_x, self.cursor_y):
                    window.close()
                    self.windows.remove(window)

    def window(self, title, x, y, width, height):
        new_window = Window(title, x, y, width, height)
        self.windows.append(new_window)
        return new_window

class Window:
    def __init__(self, title, x, y, width, height):
        self.title = title
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.elements = []

    def draw(self, stdscr):
        # Dibuja la ventana
        stdscr.addstr(self.y, self.x, '+' + '-' * (self.width - 2) + '+')
        for i in range(self.height - 2):
            stdscr.addstr(self.y + 1 + i, self.x, '|')
            stdscr.addstr(self.y + 1 + i, self.x + self.width - 1, '|')
        stdscr.addstr(self.y + self.height - 1, self.x, '+' + '-' * (self.width - 2) + '+')

        # Título de la ventana
        stdscr.addstr(self.y, self.x + 1, self.title[:self.width - 2])

        # Dibuja elementos dentro de la ventana
        for elem in self.elements:
            elem.draw(stdscr)

        # Dibuja la X de cierre
        stdscr.addstr(self.y, self.x + self.width - 2, 'X')

    def contains(self, cursor_x, cursor_y):
        return self.x < cursor_x < self.x + self.width and self.y < cursor_y < self.y + self.height

    def is_close_button(self, cursor_x, cursor_y):
        return cursor_x == self.x + self.width - 2 and cursor_y == self.y

    def close(self):
        pass

    def add_element(self, element):
        self.elements.append(element)

class Button:
    def __init__(self, window, text, command):
        self.window = window
        self.text = text
        self.command = command
        self.x = window.x + 1
        self.y = window.y + 1 + len(window.elements)
        window.add_element(self)

    def draw(self, stdscr):
        stdscr.addstr(self.y, self.x, f"[{self.text}]")

    def click(self):
        self.command()

class Label:
    def __init__(self, window, text):
        self.window = window
        self.text = text
        self.x = window.x + 1
        self.y = window.y + 1 + len(window.elements)
        window.add_element(self)

    def draw(self, stdscr):
        stdscr.addstr(self.y, self.x, self.text)

class Textbox:
    def __init__(self, window, prompt):
        self.window = window
        self.prompt = prompt
        self.text = ''
        self.x = window.x + 1
        self.y = window.y + 1 + len(window.elements)
        window.add_element(self)

    def draw(self, stdscr):
        stdscr.addstr(self.y, self.x, self.prompt + self.text)

    def add_text(self, char):
        self.text += char

def main(stdscr):
    container = PyContainer(stdscr)

    win1 = container.window("Ventana 1", 10, 5, 30, 10)
    Button(win1, "Click Me", lambda: print("Botón presionado!"))
    Label(win1, "Esto es una etiqueta.")
    textbox = Textbox(win1, "Ingrese algo: ")

    container.screen()

if __name__ == '__main__':
    curses.wrapper(main)
