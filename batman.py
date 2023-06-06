import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Batman")
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Draw Batman's body
canvas.create_oval(200, 200, 600, 600, fill="black")

# Draw Batman's ears
canvas.create_polygon(300, 100, 400, 200, 500, 100, fill="black")

# Draw Batman's mask
canvas.create_arc(200, 250, 600, 650, start=220, extent=100, fill="black")

# Draw Batman's eyes
canvas.create_oval(320, 350, 380, 410, fill="white")  # Left eye
canvas.create_oval(420, 350, 480, 410, fill="white")  # Right eye

# Draw Batman's mouth
canvas.create_arc(300, 420, 500, 520, start=200, extent=140, fill="black")

# Draw Batman's symbol
canvas.create_polygon(350, 500, 400, 400, 450, 500, fill="yellow")

# Run the main loop
window.mainloop()
