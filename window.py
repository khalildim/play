from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


class Window:
    def __init__(self, data):
        self.data_class = data
        self.words = self.data_class.get_word()
        self.deutsch = self.words[0]
        self.english = self.words[1]
        self.window = Tk()
        self.window.title("language game")
        self.window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

        # images process
        self.canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

        # images create
        self.front_img = PhotoImage(file="images/card_front.png")
        self.back_img = PhotoImage(file="images/card_back.png")

        # show the chosen img
        self.img = self.canvas.create_image(410, 278, image=self.front_img)
        self.canvas.grid(row=0, column=0, columnspan=3)

        # text on the image
        self.language = self.canvas.create_text(400, 150, text="Deutsch", fill="black", font=("Ariel", 40, "italic"))
        self.word = self.canvas.create_text(400, 263, text=self.deutsch, fill="black", font=("Ariel", 60, "bold"))

        # wrong Buttons
        self.wrong_img = PhotoImage(file="images/wrong.png")
        self.wrong = Button(image=self.wrong_img, border=0, highlightthickness=0, cursor="hand2",
                            command=self.flip_back_card)
        self.wrong.grid(row=1, column=0)

        # right Button
        self.right_img = PhotoImage(file="images/right.png")
        self.right = Button(image=self.right_img, border=0, highlightthickness=0, cursor="hand2",
                            command=lambda: self.data_class.save_learned_word(self.flip_back_card))
        self.right.grid(row=1, column=2)

        # flip Button
        self.flip = Button(text="Flip", bg="#64CCC5", command=self.flip_the_card, highlightthickness=0, cursor="hand2",
                           width=10, font=("Ubuntu", 20, "bold"))
        self.flip.grid(row=1, column=1)

        # reset Button
        self.reset = Button(text="Reset", bg="red", highlightthickness=0, cursor="hand2",
                            width=10, font=("Ubuntu", 20, "bold"), command=self.data_class.reset_all)
        self.reset.grid(row=2, column=1)
        self.window.mainloop()

    def flip_the_card(self):
        # image modified
        self.canvas.itemconfig(self.img, image=self.back_img)
        # text modified
        self.canvas.itemconfig(self.language, text="English", fill="white")
        self.canvas.itemconfig(self.word, text=self.english, fill="white")

    # Inside flip_back_card method
    def flip_back_card(self):
        # image modified
        self.canvas.itemconfig(self.img, image=self.front_img)
        # Fetch new words
        self.words = self.data_class.get_word()
        self.deutsch, self.english = self.words
        # text modified
        self.canvas.itemconfig(self.language, text="Deutsch", fill="black")
        self.canvas.itemconfig(self.word, text=self.deutsch, fill="black")
