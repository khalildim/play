from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

class Window:
    def __init__(self, data):
        self.data_class = data
        self.words = self.data_class.get_word()
        self.deutsch = self.words[0]
        self.english = self.words[1]
        self.window = Tk()
        self.window.title("Language Game")
        self.window.config(bg=BACKGROUND_COLOR)

        # Frame to hold the canvas
        self.canvas_frame = Frame(self.window, bg=BACKGROUND_COLOR)
        self.canvas_frame.pack(expand=True, fill=BOTH)

        # Canvas to display the word
        self.canvas = Canvas(self.canvas_frame, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.pack(expand=True, fill=BOTH)

        # Buttons Frame
        self.buttons_frame = Frame(self.window, bg=BACKGROUND_COLOR)
        self.buttons_frame.pack()

        # Flip Button
        self.flip = Button(self.buttons_frame, text="Flip", bg="#64CCC5", command=self.flip_the_card)
        self.flip.grid(row=0, column=0, padx=10, pady=5)

        # Reset Button
        self.reset = Button(self.buttons_frame, text="Reset", bg="red", command=self.data_class.reset_all)
        self.reset.grid(row=0, column=1, padx=10, pady=5)

        self.show_word()
        self.window.mainloop()
    def show_word(self):
        # Clear canvas
        self.canvas.delete("all")

        # Display the word
        self.canvas.create_text(400, 150, text="Deutsch", fill="black", font=("Arial", 40, "italic"))
        self.canvas.create_text(400, 263, text=self.deutsch, fill="black", font=("Arial", 60, "bold"))

    def flip_the_card(self):
        # Clear canvas
        self.canvas.delete("all")

        # Display the flipped word
        self.canvas.create_text(400, 150, text="English", fill="white", font=("Arial", 40, "italic"))
        self.canvas.create_text(400, 263, text=self.english, fill="white", font=("Arial", 60, "bold"))


