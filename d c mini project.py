import tkinter as tk
import time
from datetime import datetime
import pytz

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")

        self.bg_color = "#333333"  # Default background color
        self.font = ('Helvetica', 72)  # Default font
        self.text_color = 'white'  # Default text color

        self.clock_label = tk.Label(root, font=self.font, fg=self.text_color, bg=self.bg_color)
        self.clock_label.pack(fill='both', expand=True, padx=20, pady=20)

        self.update_time()

        # Create a menu bar
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # Create dropdown menus for font, text color, and background color
        font_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Font", menu=font_menu)
        fonts = [('Arial', 72), ('Courier', 72), ('Times New Roman', 72), ('Verdana', 72), ('Impact', 72)]
        for font in fonts:
            font_menu.add_command(label=font[0], command=lambda f=font: self.change_font(f))

        color_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Text Color", menu=color_menu)
        colors = ['white', 'red', 'green', 'blue', 'yellow']
        for color in colors:
            color_menu.add_command(label=color, command=lambda c=color: self.change_text_color(c))

        bg_color_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Background Color", menu=bg_color_menu)
        bg_colors = ['black', 'darkgray', 'navy', 'purple', 'maroon']
        for bg_color in bg_colors:
            bg_color_menu.add_command(label=bg_color, command=lambda bg=bg_color: self.change_background_color(bg))

    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.clock_label.config(text=current_time)
        self.clock_label.after(1000, self.update_time)

    def change_font(self, new_font):
        self.font = new_font
        self.clock_label.config(font=self.font)

    def change_text_color(self, new_color):
        self.text_color = new_color
        self.clock_label.config(fg=self.text_color)

    def change_background_color(self, new_color):
        self.bg_color = new_color
        self.clock_label.config(bg=self.bg_color)

def main():
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()

