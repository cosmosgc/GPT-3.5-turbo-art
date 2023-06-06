import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Flamingo")
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Draw the flamingo's body
canvas.create_rectangle(300, 300, 500, 500, fill="pink")

# Draw the flamingo's neck and head
canvas.create_line(400, 250, 400, 300, width=10)  # Neck
canvas.create_oval(350, 200, 450, 250, fill="pink")  # Head

# Draw the flamingo's beak
canvas.create_polygon(450, 225, 500, 225, 500, 250, fill="orange")

# Draw the flamingo's legs
canvas.create_line(400, 500, 400, 600, width=10)  # Left leg
canvas.create_line(400, 500, 450, 600, width=10)  # Right leg

# Draw the flamingo's feet
canvas.create_oval(375, 575, 425, 600, fill="orange")  # Left foot
canvas.create_oval(425, 575, 475, 600, fill="orange")  # Right foot

# Run the main loop
window.mainloop()
