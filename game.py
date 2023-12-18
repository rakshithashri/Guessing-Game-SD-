import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Custom Guessing Game")

        
        self.target_number = None
        self.attempts = 0

        
        self.target_label = tk.Label(master, text="Enter the number to be guessed:", font=("Helvetica", 14), fg="blue", bg="lightgray")
        self.target_label.pack(pady=10)

        self.target_entry = tk.Entry(master, font=("Helvetica", 12))
        self.target_entry.pack(pady=10)

        self.start_button = tk.Button(master, text="Start Game", command=self.start_game, bg="green", fg="white", font=("Helvetica", 12))
        self.start_button.pack(pady=10)

        self.label = tk.Label(master, text="", font=("Helvetica", 14), fg="blue", bg="lightgray")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Helvetica", 12))
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Make a Guess", command=self.make_guess, bg="green", fg="white", font=("Helvetica", 12))
        self.guess_button.pack(pady=10)

        self.end_button = tk.Button(master, text="End Game", command=self.end_game, bg="red", fg="white", font=("Helvetica", 12))
        self.end_button.pack(pady=10)

        # Bind the "Enter" key to the make_guess function
        self.entry.bind("<Return>", lambda event: self.make_guess())

    def start_game(self):
        try:
            self.target_number = int(self.target_entry.get())
            self.attempts = 0

            # Update the label to inform the user that the game has started
            self.label.config(text=f"Guess the number between 1 and 100. Number to guess: {self.target_number}")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the target.", icon="error")

    def make_guess(self):
        if self.target_number is None:
            messagebox.showwarning("Start Game", "Please start the game first by entering the target number.")
            return

        try:
            user_guess = int(self.entry.get())
            self.attempts += 1

            if user_guess == self.target_number:
                self.end_game()
                messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts!", icon="info")
            elif user_guess < self.target_number:
                messagebox.showinfo("Too Low", "Try a higher number.", icon="warning")
            else:
                messagebox.showinfo("Too High", "Try a lower number.", icon="warning")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for your guess.", icon="error")

    def end_game(self):
        self.target_number = None
        self.attempts = 0
        self.target_entry.delete(0, tk.END)
        self.label.config(text="")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="lightgray")  
    game = GuessingGame(root)
    root.mainloop()