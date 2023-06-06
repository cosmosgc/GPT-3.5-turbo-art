import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("DOOM")
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Draw the background
canvas.create_rectangle(0, 0, 800, 600, fill="black")

# Draw the DOOM logo
canvas.create_text(400, 200, text="DOOM", fill="red", font=("Helvetica", 80, "bold"))

# Draw the character
canvas.create_rectangle(280, 250, 520, 450, fill="gray")

# Draw the character's head
canvas.create_oval(330, 160, 470, 300, fill="gray")

# Draw the character's eyes
canvas.create_oval(360, 190, 390, 220, fill="white")
canvas.create_oval(410, 190, 440, 220, fill="white")

# Draw the character's mouth
canvas.create_arc(370, 250, 430, 290, start=190, extent=160, fill="black", width=2)

# Draw the weapon
canvas.create_line(500, 310, 560, 270, fill="gray", width=5)
canvas.create_line(560, 270, 620, 320, fill="gray", width=5)
canvas.create_line(620, 320, 570, 360, fill="gray", width=5)

# Run the main loop
window.mainloop()
