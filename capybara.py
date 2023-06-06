import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Capybara")
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Draw the capybara's body
canvas.create_oval(300, 300, 500, 500, fill="tan")

# Draw the capybara's head
canvas.create_oval(350, 250, 450, 350, fill="tan")

# Draw the capybara's ears
canvas.create_polygon(370, 250, 380, 210, 390, 250, fill="tan")
canvas.create_polygon(410, 250, 420, 210, 430, 250, fill="tan")

# Draw the capybara's eyes
canvas.create_oval(380, 290, 390, 310, fill="black")
canvas.create_oval(410, 290, 420, 310, fill="black")

# Draw the capybara's nose
canvas.create_polygon(400, 310, 395, 320, 405, 320, fill="pink")

# Draw the capybara's legs
canvas.create_rectangle(330, 420, 370, 500, fill="tan")
canvas.create_rectangle(430, 420, 470, 500, fill="tan")

# Draw the capybara's feet
canvas.create_oval(320, 490, 380, 520, fill="tan")
canvas.create_oval(420, 490, 480, 520, fill="tan")

# Run the main loop
window.mainloop()
