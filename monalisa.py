import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Mona Lisa")
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Draw the background
canvas.create_rectangle(0, 0, 800, 600, fill="light gray")

# Draw the face
canvas.create_oval(200, 150, 600, 550, fill="bisque2")

# Draw the eyes
canvas.create_oval(300, 300, 400, 400, fill="white")  # Left eye
canvas.create_oval(500, 300, 600, 400, fill="white")  # Right eye

# Draw the eyebrows
canvas.create_rectangle(250, 250, 450, 290, fill="black")  # Left eyebrow
canvas.create_rectangle(550, 250, 750, 290, fill="black")  # Right eyebrow

# Draw the mouth
canvas.create_arc(300, 450, 600, 550, start=220, extent=100, style="arc", outline="black", width=5)

# Draw the nose
canvas.create_polygon(400, 400, 450, 500, 350, 500, fill="navajo white")

# Draw the hair
canvas.create_arc(150, 100, 650, 400, start=200, extent=140, style="arc", outline="black", width=5)

# Run the main loop
window.mainloop()
