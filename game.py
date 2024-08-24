import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk

# Initialize win counters
user_wins = 0
computer_wins = 0

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user's choice
def on_user_choice(user_choice):
    global user_wins, computer_wins

    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)
    
    user_result_label.config(text=f"You chose: {user_choice}")
    computer_result_label.config(text=f"Computer chose: {computer_choice}")

    # Update the computer window with the computer's choice
    update_computer_image(computer_choice)
    
    # Update win counters
    if result == "You win!":
        user_wins += 1
    elif result == "Computer wins!":
        computer_wins += 1

    # Update win count labels
    user_win_count_label.config(text=f"My Wins: {user_wins}")
    computer_win_count_label.config(text=f"Computer Wins: {computer_wins}")

    # Check if either player has reached 3 wins
    if user_wins == 3:
        messagebox.showinfo("Game Result", "Congratulations! You won 3 times! Better Luck next time Machine!!")
        reset_game()
    elif computer_wins == 3:
        messagebox.showinfo("Game Result", "Computer won 3 times. Better luck next time!")
        reset_game()
    else:
        # Show result in a pop-up window
        messagebox.showinfo("Game Result", result)

# Function to update the computer window with the appropriate image
def update_computer_image(choice):
    if choice == "rock":
        computer_choice_frame.config(image=comp_rock_img)
    elif choice == "paper":
        computer_choice_frame.config(image=comp_paper_img)
    elif choice == "scissors":
        computer_choice_frame.config(image=comp_scissors_img)

# Function to reset the choice images in the computer window
def reset_computer_choice_image():
    computer_choice_frame.config(image="")

# Function to reset the game
def reset_game():
    global user_wins, computer_wins
    user_wins = 0
    computer_wins = 0
    user_result_label.config(text="Make your choice!")
    computer_result_label.config(text="")
    user_win_count_label.config(text=f"My Wins: {user_wins}")
    computer_win_count_label.config(text=f"Computer Wins: {computer_wins}")
    # Reset the computer choice image
    reset_computer_choice_image()

# Load and display images
def load_image(path, size=(150, 150)):
    try:
        image = Image.open(path)
        image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image at {path}: {e}")
        return None

# Create the user window
user_window = tk.Tk()
user_window.title("User: Rock, Paper, Scissors")
user_window.geometry("400x450")  # Set a fixed size for the user window

# Load images for user
user_img = load_image(r"C:\Users\kambi\OneDrive\Documents\codsoft\user.png")
if user_img:
    user_image_label = tk.Label(user_window, image=user_img)
    user_image_label.pack()
else:
    print("Failed to load user image")

user_result_label = tk.Label(user_window, text="Make your choice!", font=("Helvetica", 14))
user_result_label.pack(pady=20)

# User win count label
user_win_count_label = tk.Label(user_window, text=f"My Wins: {user_wins}", font=("Helvetica", 12))
user_win_count_label.pack()

user_button_frame = tk.Frame(user_window)
user_button_frame.pack()

# Load images for buttons
rock_img = load_image(r"C:\Users\kambi\OneDrive\Documents\codsoft\rock.png", (100, 100))
paper_img = load_image(r"C:\Users\kambi\OneDrive\Documents\codsoft\paper.png", (100, 100))
scissors_img = load_image(r"C:\Users\kambi\OneDrive\Documents\codsoft\scissor.png", (100, 100))

rock_button = tk.Button(user_button_frame, image=rock_img, command=lambda: on_user_choice("rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(user_button_frame, image=paper_img, command=lambda: on_user_choice("paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(user_button_frame, image=scissors_img, command=lambda: on_user_choice("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

reset_button = tk.Button(user_window, text="Play Again", width=10, command=reset_game)
reset_button.pack(pady=20)

# Create the computer window
computer_window = tk.Toplevel(user_window)
computer_window.title("Computer: Rock, Paper, Scissors")
computer_window.geometry("400x450")  # Set the same size for the computer window

# Load images for computer choices
comp_rock_img = load_image(r"C:\Users\kambi\OneDrive\Documents\codsoft\rock.png", (100, 100))
comp_paper_img = load_image(r"C:\Users\kambi\OneDrive\Documents\codsoft\paper.png", (100, 100))
comp_scissors_img = load_image(r"C:\Users\kambi\OneDrive\Documents\codsoft\scissor.png", (100, 100))

# Computer Image
computer_image_label = tk.Label(computer_window)
computer_image_label.pack(pady=10)

# Load and display the computer image
computer_img = load_image(r"C:\Users\kambi\OneDrive\Documents\codsoft\computer.png", (150, 150))
if computer_img:
    computer_image_label.config(image=computer_img)
else:
    print("Failed to load computer image")

# Frame for computer choices
computer_choice_frame = tk.Label(computer_window)
computer_choice_frame.pack(pady=10)

computer_result_label = tk.Label(computer_window, text="", font=("Helvetica", 14))
computer_result_label.pack(pady=20)

# Computer win count label
computer_win_count_label = tk.Label(computer_window, text=f"Computer Wins: {computer_wins}", font=("Helvetica", 12))
computer_win_count_label.pack()

# Keep references to images to prevent them from being garbage collected
user_window.mainloop()
