import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Shrek")
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Draw the background
canvas.create_rectangle(0, 0, 800, 600, fill="pale green")

# Draw the body
canvas.create_oval(200, 250, 600, 550, fill="green3")

# Draw the head
canvas.create_oval(250, 100, 550, 400, fill="green3")

# Draw the eyes
canvas.create_oval(320, 170, 380, 230, fill="white")  # Left eye
canvas.create_oval(420, 170, 480, 230, fill="white")  # Right eye

# Draw the pupils
canvas.create_oval(335, 185, 365, 215, fill="black")  # Left pupil
canvas.create_oval(435, 185, 465, 215, fill="black")  # Right pupil

# Draw the eyebrows
canvas.create_rectangle(285, 150, 385, 180, fill="black")  # Left eyebrow
canvas.create_rectangle(385, 150, 485, 180, fill="black")  # Right eyebrow

# Draw the mouth
canvas.create_rectangle(300, 300, 500, 350, fill="sienna4")

# Draw the teeth
canvas.create_rectangle(320, 310, 350, 340, fill="white")  # Left tooth
canvas.create_rectangle(380, 310, 410, 340, fill="white")  # Middle tooth
canvas.create_rectangle(440, 310, 470, 340, fill="white")  # Right tooth

# Draw the nose
canvas.create_polygon(400, 240, 450, 300, 350, 300, fill="light pink")

# Draw the ears
canvas.create_oval(230, 150, 290, 250, fill="green3")  # Left ear
canvas.create_oval(510, 150, 570, 250, fill="green3")  # Right ear

# Draw the horns
canvas.create_polygon(210, 160, 240, 190, 180, 190, fill="dark olive green")  # Left horn
canvas.create_polygon(590, 160, 620, 190, 560, 190, fill="dark olive green")  # Right horn

# Run the main loop
window.mainloop()
