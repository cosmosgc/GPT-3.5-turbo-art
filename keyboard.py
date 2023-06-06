import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Keyboard")
canvas = tk.Canvas(window, width=800, height=300)
canvas.pack()

# Draw the main body of the keyboard
canvas.create_rectangle(50, 50, 750, 250, fill="gray")

# Draw the white keys
key_width = 50
key_height = 150
for i in range(13):
    x = 50 + i * key_width
    y = 50
    canvas.create_rectangle(x, y, x + key_width, y + key_height, fill="white")

# Draw the black keys
black_key_width = 30
black_key_height = 90
black_key_positions = [70, 120, 220, 270, 320, 470, 520, 570, 670, 720]
for position in black_key_positions:
    x = position
    y = 50
    canvas.create_rectangle(x, y, x + black_key_width, y + black_key_height, fill="black")

# Run the main loop
window.mainloop()
