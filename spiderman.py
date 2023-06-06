import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Spiderman")
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Draw Spiderman's head
canvas.create_oval(200, 200, 600, 600, fill="red")

# Draw Spiderman's eyes
canvas.create_oval(300, 300, 400, 400, fill="white")  # Left eye
canvas.create_oval(500, 300, 600, 400, fill="white")  # Right eye

# Draw Spiderman's web lines
canvas.create_line(300, 400, 600, 400, width=3)  # Horizontal line
canvas.create_line(450, 200, 450, 600, width=3)  # Vertical line

# Run the main loop
window.mainloop()
