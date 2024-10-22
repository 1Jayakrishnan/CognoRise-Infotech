import tkinter as tk
from PIL import Image, ImageTk  # Pillow library for handling images

LARGE_FONT_STYLE = ("Arial", 36, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#A5D8FF"  # Light blue for "=" button
LIGHT_GRAY = "#E5E5E5"  # Light grey for buttons
LABEL_COLOR = "#25265E"
RED = "#FF4C4C"  # Red for "Cancel" button
BLACK = "#000000"  # Set black font color

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x650")  # Slightly adjusted size
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.create_back_button()  # Add back button
        self.create_division_button()  # Add division button here

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=WHITE,
                               fg=BLACK, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=WHITE,
                         fg=BLACK, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=200, bg=WHITE)  # Adjusted height
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=BLACK, font=DIGITS_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=LIGHT_GRAY, fg=BLACK, font=DEFAULT_FONT_STYLE,  # Light grey background for operators
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=RED, fg=WHITE, font=DEFAULT_FONT_STYLE,  # Red for "Cancel" button
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=LIGHT_GRAY, fg=BLACK, font=DEFAULT_FONT_STYLE,  # Light grey background
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=LIGHT_GRAY, fg=BLACK, font=DEFAULT_FONT_STYLE,  # Light grey background
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_back_button(self):
        """Creates a back button using the image provided."""
        back_image = Image.open("back.png")
        back_image = back_image.resize((50, 50))  # Resize image to fit the button
        back_image = back_image.rotate(-90, expand=True)
        back_photo = ImageTk.PhotoImage(back_image)

        button = tk.Button(self.buttons_frame, image=back_photo, bg=LIGHT_GRAY, borderwidth=0, command=self.backspace)
        button.image = back_photo  # Keep a reference to avoid garbage collection
        button.grid(row=0, column=4, sticky=tk.NSEW)

    def backspace(self):
        self.current_expression = self.current_expression[:-1]
        self.update_label()

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=BLACK, font=DEFAULT_FONT_STYLE,  # Light blue for "=" button
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, sticky=tk.NSEW)

    def create_division_button(self):
        button = tk.Button(self.buttons_frame, text="\u00F7", bg=LIGHT_GRAY, fg=BLACK, font=DEFAULT_FONT_STYLE,  # Light grey for operators
                           borderwidth=0, command=lambda: self.append_operator("/"))
        button.grid(row=4, column=4, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
